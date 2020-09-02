import random
import time
import pyautogui
import pydirectinput

pyautogui.click()
pyautogui.FAILSAFE = True
def walk():
    x = 5
    listBottoms = ['a', 'd', 'w', 's']
    while True:
     pydirectinput.keyDown('a')
     time.sleep(x)
     pydirectinput.keyUp('a')
     pydirectinput.keyDown('d')
     time.sleep(x)
     pydirectinput.keyUp('d')
     pydirectinput.keyDown('w')
     time.sleep(x)
     pydirectinput.keyUp('w')
     pydirectinput.keyDown('s')
     time.sleep(x)
     pydirectinput.keyUp('s')
     pydirectinput.press('enter', presses= 10)

     newDirection = random.choice(listBottoms)

     pydirectinput.keyDown(newDirection)
     time.sleep(x)
     pydirectinput.keyUp(newDirection)


walk()

