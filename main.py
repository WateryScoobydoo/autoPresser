import time, random, keyboard
from random import randint
from pynput.keyboard import Key, Controller

key = Controller()

time.sleep(5)

def type(string):
    for character in string:
        key.type(character)
        delay = random.uniform(0, 20)
        time.sleep(0.12)

type("WASD WASD WASD ")

def main():
    x = 0
    while x == 0:
        try:
            if keyboard.is_pressed('8'):
                x = 1
        except:
            x = 0
    while x == 1:
        if keyboard.is_pressed('9'):
            break
        try:
            time.sleep(randint(2,30))
            keyboard.press('0')
        except:
            break

main()



