import pyautogui
import random
import time

while True:
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)
    pyautogui.moveTo(x, y, duration=0.25)
    time.sleep(5)
