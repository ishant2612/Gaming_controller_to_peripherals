def main():
    import pygame
    import time
    from pynput.mouse import Controller as MouseController, Button
    from pynput.keyboard import Controller as KeyboardController, Key
    import mss 
    import numpy as np
    from inputs import devices
    # INIT
    pygame.init()
    pygame.joystick.init()

    controller = pygame.joystick.Joystick(0)
    controller.init()
    gamepad = devices.gamepads[0]
    mouse = MouseController()
    keyboard = KeyboardController()

    sct = mss.mss()

    # ===== TUNING =====
    BASE_SPEED = 800
    MAX_SPEED = 2000
    DEADZONE = 0.1

    vx, vy = 0, 0
    last_time = time.time()

    prev_a = 0
    prev_b = 0
    prev_x = 0
    prev_y = 0

    prev_hat = (0, 0)

    dragging = False

    scroll_accum = 0

    def vibrate(strength, duration):
        gamepad.set_vibration(int(strength * 65535), int(strength * 65535), duration)
        time.sleep(duration)
        


    def get_pixel_intensity(x, y):
        region = {"top":int(y), "left":int(x), "width":1, "height":1}
        img = sct.grab(region)
        return np.mean(np.array(img))

    def detect_edge(x,y):
        center = get_pixel_intensity(x, y)
        right = get_pixel_intensity(x + 3, y)
        down = get_pixel_intensity(x, y + 3)
        diff = abs(center - right) + abs(center - down)

        return diff > 20  # Threshold for edge detection

    def normalize_trigger(val):
        return (val + 1) / 2 if val < 0 else val

    def apply_deadzone(val):
        return 0 if abs(val) < DEADZONE else val

    def expo(val):
        return val * abs(val)

    while True:
        pygame.event.pump()

        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        # 🎯 JOYSTICK → MOUSE
        x = apply_deadzone(controller.get_axis(0))
        y = apply_deadzone(controller.get_axis(1))

        x = expo(x)
        y = expo(y)

        last_vibrate = 0
        vib_delay = 0.5  # Vibrate every 0.5 seconds on edge

        if detect_edge(mouse.position[0], mouse.position[1]):
            if time.time() - last_vibrate > vib_delay:  # Vibrate every 0.5 seconds on edge
                vibrate(0.1,0.2)
                last_vibrate = time.time()

        rt = normalize_trigger(controller.get_axis(5))
        lt = normalize_trigger(controller.get_axis(4))

        speed = BASE_SPEED + (rt * (MAX_SPEED - BASE_SPEED))

        vx = x * speed
        vy = y * speed

        move_x = vx * dt
        move_y = vy * dt

        if abs(move_x) < 0.4:
            move_x = 0
        if abs(move_y) < 0.4:
            move_y = 0

        if move_x != 0 or move_y != 0:
            mouse.move(int(move_x), int(move_y))

        # 🔘 LEFT CLICK + DRAG
        a = controller.get_button(0)

        if a == 1 and prev_a == 0:
            mouse.press(Button.left)
            vibrate(0.8, 0.04)
            dragging = True
            if dragging:
                vibrate(0.1,0.01)

        if a == 0 and prev_a == 1:
            mouse.release(Button.left)
            dragging = False

        prev_a = a

        # 🔘 RIGHT CLICK
        b = controller.get_button(1)
        if b == 1 and prev_b == 0:
            mouse.click(Button.right, 1)
        prev_b = b

        # 🧭 SCROLL (pressure based)
        scroll_velocity = (rt - lt)
        scroll_pixels = scroll_velocity * 200 * dt
        scroll_accum += scroll_pixels

        if abs(scroll_accum) >= 1:
            mouse.scroll(0, int(scroll_accum))
            scroll_accum -= int(scroll_accum)

        # =========================
        # ⌨️ KEYBOARD SYSTEM
        # =========================

        # 🎮 D-PAD → ARROWS
        hat = controller.get_hat(0)

        if hat != prev_hat:
            # release previous
            if prev_hat == (0, 1):
                keyboard.release(Key.up)
            elif prev_hat == (0, -1):
                keyboard.release(Key.down)
            elif prev_hat == (1, 0):
                keyboard.release(Key.right)
            elif prev_hat == (-1, 0):
                keyboard.release(Key.left)

            # press new
            if hat == (0, 1):
                keyboard.press(Key.up)
            elif hat == (0, -1):
                keyboard.press(Key.down)
            elif hat == (1, 0):
                keyboard.press(Key.right)
            elif hat == (-1, 0):
                keyboard.press(Key.left)

            prev_hat = hat

        # 🎯 X → ENTER
        x_btn = controller.get_button(2)
        if x_btn == 1 and prev_x == 0:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        prev_x = x_btn

        # 🎯 Y → BACKSPACE
        y_btn = controller.get_button(3)
        if y_btn == 1 and prev_y == 0:
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        prev_y = y_btn

        # 🎯 L1 / R1 → MODIFIERS
        l1 = controller.get_button(4)
        r1 = controller.get_button(5)

        if l1:
            keyboard.press(Key.ctrl)
        else:
            keyboard.release(Key.ctrl)

        if r1:
            keyboard.press(Key.shift)
        else:
            keyboard.release(Key.shift)

        # 🔥 L1 + R1 → ALT TAB
        if l1 and r1:
            keyboard.press(Key.alt)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.release(Key.alt)
            time.sleep(0.3)
        # Example: press Y + B together → voice typin
        # 
        if controller.get_button(3) and controller.get_button(1):
            keyboard.press(Key.cmd)  # Windows key
            keyboard.press('h')
            keyboard.release('h')
            keyboard.release(Key.cmd)
            time.sleep(0.5)
        time.sleep(0.005)

if __name__ == "__main__":    main()