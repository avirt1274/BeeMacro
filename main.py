# -*- coding: utf-8 -*-
import pydirectinput, time, keyboard, threading, os
from requests import get, post
from random import randint
from bs4 import BeautifulSoup
from cmd_lib import CMD
# import lxml

#settings
prefix = '[BM-STATUS]' + ' '
github = 'https://github.com/avirt1274/BeeMacro.git'
main_raw = 'https://raw.githubusercontent.com/avirt1274/BeeMacro/main/main.py'
#VersionFlag1
version = 0.0001 #Do not change!!!
#VersionFlag1

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
Welcome to the BeeMacro! v{version} | By Avirt :)
------------------------------------------------
Alt + F1 - Start/Stop {module_AGinger}
Alt + F2 - Start/Stop {module_FarmDandelion}
Alt + F3 - Start/Stop {module_Autoclicker}
------------------------------------------------
Alt + F5 - Primary Update!
"""

def Update():
    st_accept = "text/html" # tell web, 
    # imatate web connecting
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36/537.36'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36/537.36'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'
    ]
    # formatting header
    headers = {
        "Accept": st_accept,
        "User-Agent": user_agents[randint(0, len(user_agents) - 1)]
    }

    print('Checking updates!')
    timed_html = get(main_raw, headers=headers)
    raw_src = timed_html.text
    html = BeautifulSoup(raw_src, 'lxml')

    m = html.p.text.partition("#VersionFlag1")[2].partition("#VersionFlag2")[0] # Getting info between flags
    i = 11
    version_from_git = ''
    for sdsdd in range(6):
        version_from_git += m[i]
        i+=1
    
    version_from_git = float(version_from_git)

    if version_from_git > version:
        print('Update found!')
        updated_file = open('main.py', 'w')
        updated_file.write(html.p.text)
        print('Updated!')
        time.sleep(2)
        exit(0)
    else:
        print('You are have an actual version!!')
    time.sleep(2)


def AHKCheck():
    if os.path.exists('C:/Program Files/AutoHotkey'):
        return True
    else:
        if os.path.exists(f'{os.getcwd()}/AHK/AutoHotkey_1.1.37.02_setup.exe'):
            if os.startfile(f'{os.getcwd()}/AHK/AutoHotkey_1.1.37.02_setup.exe'):
                return False
            else:
                return False
        else:
            return 'AutoHotkey_1.1.37.02_setup.exe is not in AHK!'


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


def farm():
    status = False
    AntiAFK_thread = threading.Thread(target=AntiAFK)

    while True:
        if enabled:
            if status == False:
                RunAHKScript('BeeMacro-AutoGingerbread.ahk')
                AntiAFK_thread.run()
                status = True
                
            pydirectinput.press('n')
            time.sleep(2)

            # time.sleep(7200) # 7200 seconds = 2h
        elif enabledFarmDandelion:
            pydirectinput.click(x=32, y=42)
            time.sleep(3)
            pydirectinput.click(x=960, y=880)
            time.sleep(3)
            pydirectinput.click(x=850, y=480)
        elif enabledAutoclicker:
            pydirectinput.click(button='left')
            time.sleep(1)

    
def UpdateWithInstruction():
    Update()
    print('\n' + instruction + '\n')

def RunAHKScript(path):
    if AHKCheck():
        CMD.call(command=f'start AHK/{path}')
        

def main():
    Update()
    print('\n')
    print('Checking AHK.')
    print('Checking AHK..')
    print('Checking AHK...')
    if AHKCheck():
        print('AHK is already installed')
    else:
        print('Success Installed!')
        
    print('\n' + instruction + '\n')
    farm_thread = threading.Thread(target=farm)
    keyboard.add_hotkey('alt + f1', EnabledChanger)
    keyboard.add_hotkey('alt + f2', EnabledChangerFarmDandelion)
    keyboard.add_hotkey('alt + f3', EnabledChangerAutoclicker)
    keyboard.add_hotkey('alt + f5', UpdateWithInstruction)
    farm_thread.run()

main()