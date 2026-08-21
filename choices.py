from strings import *
from paths import twopath, threepath, fourpath, fivepath
import time
import random
#End import list
#Begin variable list
#End variable list
#Begin game code
def choicespeed(delay):


    "Thank you for choosing properly"
    speed = 1
    if speed == 1:
        delay = .15
        return delay
    elif speed == 2:
        delay = .075
        return delay
    elif speed == 3:
        delay = .01
        return delay

def choicedifficulty(delay):
    difficulty = 0
    modifier = 0
    "1. Easy"
    time.sleep(.5)
    "2. Normal"
    time.sleep(.5)
    "3. Hard"
    time.sleep(.5)
    "4. Why choose anything harder?"
    time.sleep(.5)

    difficulty = 0

    if difficulty == 1:
        narrator[14]
        time.sleep(.75)
        narrator[15]
        modifier = .5
        return modifier
    elif difficulty == 2:
        narrator[16]
        time.sleep(.75)
        narrator[17]
        modifier = 1
        return modifier
    elif difficulty == 3:
        narrator[18]
        time.sleep(.75)
        narrator[19]
        modifier = 1.5
        return modifier
    elif difficulty == 4:
        narrator[20]
        time.sleep(.75)
        narrator[21]
        modifier = 2
        return modifier

def choiceworld(delay):
    "1. A Good Place"
    time.sleep(.5)
    "2. A Bad Place"
    time.sleep(.5)
    "3. A So-So Place"
    time.sleep(.5)
    "4. A Weird Place"
    time.sleep(.5)
    "5. A Random Place"
    time.sleep(.25)

    choice = narrator[3]

    if choice == 1:
        narrator[4]
        time.sleep(2)
        narrator[5]
        time.sleep(1)
    elif choice == 2:
        narrator[6]
        time.sleep(2)
        narrator[5]
        time.sleep(1)
    elif choice == 3:
        narrator[7]
        time.sleep(2)
        narrator[5]
        time.sleep(1)
    elif choice == 4:
        narrator[8]
        time.sleep(2)
        narrator[5]
        time.sleep(1)
    elif choice == 5:
        choice = random.choice([1, 2, 3, 4])
        narrator[9]
        time.sleep(2)
        narrator[5]
        time.sleep(1)
        return choice

    return choice

def getText(name: str, strings: list):
    if name == "MAINTEXT":
        return strings[0]
    elif name == "QUESTIONTEXT":
        return narrator[3]
    elif name == "STRINGONE":
        return strings[1]
    elif name == "STRINGTWO":
        return strings[2]
    elif name == "STRINGTHREE":
        return strings[3]
    elif name == "STRINGFOUR":
        return ""
    return ""