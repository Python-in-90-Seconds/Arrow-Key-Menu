import msvcrt
import os 

options = ["Start", "Settings", "Exit"]
index = 0

def render():
    os.system("cls")  # (Windows only)

    for i, option in enumerate(options):
        prefix = "> " if i == index else "  "
        print(f"{prefix}{option}")

while True:
    render()
    key = msvcrt.getch()

    if key == b"\x00":
        arrow = msvcrt.getch()

        if arrow == b"H":
            index = (index - 1) % len(options)
        elif arrow == b"P":
            index = (index + 1) % len(options)
    
    elif key == b"\r":  # Enter key
        break

print(f"\nYou picked: {options[index]}")