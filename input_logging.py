import pygame

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()

print("Controller Name:", controller.get_name())
print("Number of Axes:", controller.get_numaxes())
print("Number of D-pad", controller.get_numhats())
print("Listening inputs...")

prev_axes = [0] * controller.get_numaxes()
prev_buttons = [0] * controller.get_numbuttons()

def normalize_axis(value):
    return round((value + 1 )/ 2,3)

while True:
    pygame.event.pump()  # Process event queue  

    for i in range(controller.get_numaxes()):
        val = controller.get_axis(i)    
        if abs(val - prev_axes[i]) > 0.01:
            if i >= controller.get_numaxes() - 2:  # Last 2 axes are triggers
                pressure = normalize_axis(val)
                print(f"Trigger {i} : raw={round(val,3)} | pressure={pressure}")
            else:
                print(f"Axis {i} : {round(val,3)}")
            prev_axes[i] = val

    #buttons
    for i in range(controller.get_numbuttons()):
        val = controller.get_button(i)
        if val != prev_buttons[i]:
            state = "Pressed" if val else "Released"
            print(f"Button {i} : {state}")
            prev_buttons[i] = val

    # D-pad (hats)
    for i in range(controller.get_numhats()):
        val = controller.get_hat(i)

        if val != (0, 0):
            print(f"D-pad {i} : {val}")