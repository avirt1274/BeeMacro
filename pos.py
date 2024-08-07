import keyboard, pyautogui

keyboard.add_hotkey('alt + f3', lambda: print(pyautogui.displayMousePosition()))

while True:
    pass