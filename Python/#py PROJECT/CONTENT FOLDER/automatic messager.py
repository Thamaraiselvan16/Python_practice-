import random
import pyautogui as pg
import time

words=("____","good","simply")
time.sleep(8)

for i in range(20):
    a=random.choice(words)
    pg.write("you are a"+a)
    pg.press("enter")
