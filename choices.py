from strings import narrator, errorHandling
from textWriter import textWriter
from paths import twopath, threepath, fourpath, fivepath
import time
import random
#End import list
#Begin variable list
#End variable list
#Begin game code
def choicespeed(delay):
    textWriter("How fast should I talk?", delay)
    textWriter("1. this slow?", .15)
    textWriter("2. this mediocre?", .075)
    textWriter("3. this fast?", .01)

    speed = threepath(input(narrator[3]))
    textWriter("Thank you for choosing properly", delay)
    
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
    textWriter("1. Easy", delay)
    time.sleep(.5)
    textWriter("2. Normal", delay)
    time.sleep(.5)
    textWriter("3. Hard", delay)
    time.sleep(.5)
    textWriter("4. Why choose anything harder?", delay)
    time.sleep(.5)

    difficulty = fourpath(input(narrator[3]))

    if difficulty == 1:
        textWriter(narrator[14], delay)
        time.sleep(.75)
        textWriter(narrator[15], delay)
        modifier = .5
        return modifier
    elif difficulty == 2:
        textWriter(narrator[16], delay)
        time.sleep(.75)
        textWriter(narrator[17], delay)
        modifier = 1
        return modifier
    elif difficulty == 3:
        textWriter(narrator[18], delay)
        time.sleep(.75)
        textWriter(narrator[19], delay)
        modifier = 1.5
        return modifier
    elif difficulty == 4:
        textWriter(narrator[20], .2)
        time.sleep(.75)
        textWriter(narrator[21], delay)
        modifier = 2
        return modifier

def choiceworld(delay):
    textWriter("1. A Good Place", delay)
    time.sleep(.5)
    textWriter("2. A Bad Place", delay)
    time.sleep(.5)
    textWriter("3. A So-So Place", delay)
    time.sleep(.5)
    textWriter("4. A Weird Place", delay)
    time.sleep(.5)
    textWriter("5. A Random Place", delay)
    time.sleep(.25)

    choice = fivepath(input(narrator[3]))

    if choice == 1:
        textWriter(narrator[4], delay)
        time.sleep(2)
        textWriter(narrator[5], delay)
        time.sleep(1)
    elif choice == 2:
        textWriter(narrator[6], delay)
        time.sleep(2)
        textWriter(narrator[5], delay)
        time.sleep(1)
    elif choice == 3:
        textWriter(narrator[7], delay)
        time.sleep(2)
        textWriter(narrator[5], delay)
        time.sleep(1)
    elif choice == 4:
        textWriter(narrator[8], delay)
        time.sleep(2)
        textWriter(narrator[5], delay)
        time.sleep(1)
    elif choice == 5:
        choice = random.choice([1, 2, 3, 4])
        textWriter(narrator[9], delay)
        time.sleep(2)
        textWriter(narrator[5], delay)
        time.sleep(1)
        return choice

    return choice
