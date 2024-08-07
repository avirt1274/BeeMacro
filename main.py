import pydirectinput, time, keyboard, asyncio, pyautogui, threading

#settings
prefix = '[BM-STATUS]' + ' '
github = ''
version = 0.0001

#modules
module_AGinger = 'Auto Gingerbread'
module_FarmDandelion = 'Farm Dandelion'
module_Autoclicker = 'Autoclicker'

#vars
global enabled
enabled = False
global enabledFarmDandelion
enabledFarmDandelion = False
global enabledAutoclicker
enabledAutoclicker = False

instruction = f"""
Alt + F1 - Start/Stop {module_AGinger}
Alt + F2 - Start/Stop {module_FarmDandelion}
Alt + F3 - Start/Stop {module_Autoclicker}
"""

def EnabledChanger():
    global enabled
    if enabled == False:
        enabled = True
    else:
        enabled = False
    print(prefix + f'{module_AGinger} : {enabled}!')

def EnabledChangerFarmDandelion():
    global enabledFarmDandelion
    if enabledFarmDandelion == False:
        enabledFarmDandelion = True
    else:
        enabledFarmDandelion = False

    print(prefix + f'{module_FarmDandelion} : {enabledFarmDandelion}!')

def EnabledChangerAutoclicker():
    global enabledAutoclicker
    if enabledAutoclicker == False:
        enabledAutoclicker = True
    else:
        enabledAutoclicker = False
    print(prefix + f'{module_Autoclicker} : {enabledAutoclicker}!')


def AntiAFK():
    while True:
        if enabled:
            pydirectinput.click(button='left')
            time.sleep(1)


def AGinger_farm():
    status = False
    AntiAFK_thread = threading.Thread(target=AntiAFK)

    while True:
        if enabled:
            if status == False:
                AntiAFK_thread.run()
                status = True
                
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')
            time.sleep(7200) # 7200 seconds = 2h
        elif enabledFarmDandelion:
            pydirectinput.click(x=32, y=42)
            time.sleep(3)
            pydirectinput.click(x=960, y=880)
            time.sleep(3)
            pydirectinput.click(x=850, y=480)

    



def main():
    print('Welcome to the BeeMacro! | By Avirt :)')
    print('\n' + instruction + '\n')
    farm_thread = threading.Thread(target=AGinger_farm)
    keyboard.add_hotkey('alt + f1', EnabledChanger)
    keyboard.add_hotkey('alt + f2', EnabledChangerFarmDandelion)
    keyboard.add_hotkey('alt + f3', EnabledChangerAutoclicker)
    farm_thread.run()

main()