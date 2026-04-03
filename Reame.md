# 🎮 Controller-Based System Control Interface

A custom-built system that allows you to **fully control your computer using a game controller**, replacing traditional mouse and partially replacing keyboard input — enhanced with **analog control and haptic feedback**.

---

## 🚀 Features

### 🖱️ Mouse Replacement

* Smooth cursor movement using joystick
* Adjustable speed using trigger pressure
* Deadzone + exponential smoothing for precision
* Left click, right click, and drag support

### 🎚️ Analog Controls

* Trigger-based cursor acceleration
* Pressure-sensitive scrolling
* Fine-grained movement control (like a gaming mouse)

### 🧲 Drag & Drop Support

* Hold button to drag items
* Release to drop (exact mouse behavior)

### 🧭 Keyboard Navigation

* D-Pad → Arrow keys
* Buttons → Enter, Backspace, Escape
* Shoulder buttons → Ctrl / Shift
* Combo shortcuts (e.g. Alt + Tab)

### 🔊 Haptic Feedback (Vibration)

* Feedback on hover (edge detection)
* Feedback on click
* Continuous feedback during drag
* Cooldown-based system to prevent spam

---

## 🧠 Tech Stack

* **pygame** → Controller input
* **pynput** → Mouse & keyboard control
* **inputs** → Haptic feedback (vibration)
* **mss + numpy** → Pixel-based UI detection

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/controller-system-control.git
cd controller-system-control
```

### 2. Install dependencies

```bash
pip install pygame pynput inputs mss numpy
```

---

## ▶️ Running the Project

```bash
python system_control.py
```

⚠️ Make sure your script includes:

```python
if __name__ == "__main__":
    main()
```

---

## 🎮 Controls Mapping

| Controller Input   | Action            |
| ------------------ | ----------------- |
| Left Stick         | Cursor movement   |
| Right Trigger (RT) | Speed control     |
| Left Trigger (LT)  | Scroll control    |
| A                  | Left click / Drag |
| B                  | Right click       |
| X                  | Enter             |
| Y                  | Backspace         |
| L1                 | Ctrl              |
| R1                 | Shift             |
| D-Pad              | Arrow keys        |
| L1 + R1            | Alt + Tab         |

---

## 🔊 Haptic Feedback System

| Event        | Feedback                    |
| ------------ | --------------------------- |
| Hover edge   | Soft vibration              |
| Click action | Strong vibration            |
| Dragging     | Continuous subtle vibration |

---

## ⚠️ Limitations

* No direct OS-level detection of clickable elements
* Edge detection is based on pixel contrast (approximation)
* Full keyboard typing is not fully replaced (yet)

---

## 🔮 Future Improvements

* Radial / chorded typing system
* Gesture-based commands
* Cursor-type detection (text / link / pointer)
* ML-based UI interaction prediction
* Custom UI overlay for controller navigation

---

## 🧠 Motivation

This project explores:

* Alternative human-computer interaction models
* Analog input systems
* Multi-sensory feedback (visual + haptic)

---

## 🤝 Contributing

Feel free to fork the repo and experiment with:

* New control mappings
* Better haptic systems
* Performance improvements

---

## 📌 Author

**Ishant Verma**
Building systems that rethink how humans interact with machines 🚀

---

## ⭐ If you like this project

Give it a star and share your ideas!

---
