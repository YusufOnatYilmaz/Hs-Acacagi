import os
import pyautogui
import time
from pywinauto import Desktop

os.startfile(r"C:\Program Files (x86)\Hearthstone\Hearthstone Beta Launcher.exe")

while True:
    windows = Desktop(backend="uia").windows()
    a = [w.window_text() for w in windows]
    #print(windows)
    if "Battle.net" in a:
        #print(2)
        time.sleep(3)
        pyautogui.moveTo(10, 10)
        pyautogui.moveRel(1200, 100)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(10, 10)
        pyautogui.moveRel(1000, 550)
        pyautogui.click()   
        break
    
os.system("taskkill /im Battle.net.exe")
