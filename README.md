# 🧭 Interactive Arrow Key Menu in Python (Windows)

This project shows you how to build a **fully interactive console menu** in Python using just the standard library — no `input()`, no external packages, and no mouse required!

It’s designed for Windows (CMD or PowerShell) and uses `msvcrt` to detect **arrow key presses**, allowing the user to navigate a menu and select an option with Enter.

---

## 📜 Features

- Navigate options using ↑ and ↓ keys
- Real-time updates using `os.system("cls")`
- No need to press Enter after each key
- Simple, clean, and reusable

---

## 💻 Code Example

```python
import msvcrt
import os

options = ["Start", "Settings", "Exit"]
index = 0

def render():
    os.system('cls')  # Windows only
    for i, option in enumerate(options):
        prefix = "> " if i == index else "  "
        print(f"{prefix}{option}")

while True:
    render()
    key = msvcrt.getch()
    if key == b'\x00':  # Special keys
        arrow = msvcrt.getch()
        if arrow == b'H':  # Up arrow
            index = (index - 1) % len(options)
        elif arrow == b'P':  # Down arrow
            index = (index + 1) % len(options)
    elif key == b'\r':  # Enter key
        break

print(f"\nYou picked: {options[index]}")
