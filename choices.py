from strings import narrator
from textWriter import textWriter
import time
import random
#End import list
#Begin variable list
choiceError = "Please enter a whole number. "
#End variable list
#Begin game code
def choicespeed(delay):
    string = ""
    textWriter("How fast should I talk?", delay)
    textWriter("1. this slow?", .1)
    textWriter("2. this mediocre?", .05)
    textWriter("3. this fast?", .01)
    while True:
        try:
            delay = int(string)
        except ValueError:
            print(choiceError)
            string = input("Choose one, two, or three: ")
            continue
        else:
            break
    if delay == 1:
        delay = .1
        textWriter("Thank you for choosing properly", delay)
    elif delay == 2:
        delay = .05
        textWriter("Thank you for choosing properly", delay)
    elif delay == 3:
        delay = .01
        textWriter("Thank you for choosing properly", delay)
    else:
        print("You're kidding right? Oh well, I will choose for you")
        print("")
        delay = .05
    return delay
def savechoice(delay):
    save = 0
    return save
def choicedifficulty(delay):
    difficulty = 0
    modifier = 0
    string = ""
    textWriter("1. Easy", delay)
    time.sleep(.5)
    textWriter("2. Normal", delay)
    time.sleep(.5)
    textWriter("3. Hard", delay)
    time.sleep(.5)
    textWriter("4. Why choose anything harder?", delay)
    time.sleep(.5)
    while True:
        try:
            difficulty = int(string)
        except ValueError:
            print(choiceError)
            string = input(narrator[3])
            continue
        else:
            break
    if difficulty == 1:
        textWriter(narrator[14], delay)
        time.sleep(.75)
        textWriter(narrator[15], delay)
        modifier = .5
    elif difficulty == 2:
        textWriter(narrator[16], delay)
        time.sleep(.75)
        textWriter(narrator[17], delay)
        modifier = 1
    elif difficulty == 3:
        textWriter(narrator[18], delay)
        time.sleep(.75)
        textWriter(narrator[19], delay)
        modifier = 1.5
    elif difficulty == 4:
        textWriter(narrator[20], delay)
        time.sleep(.75)
        textWriter(narrator[21], delay)
        modifier = 2
    else:
        difficultyList = [.5, 1, 1.5]
        textWriter(narrator[22], delay)
        time.sleep(.75)
        textWriter(narrator[23], delay)
        modifier = random.choice(difficultyList)
        if modifier == .5:
            print("Easy")
        elif modifier == 1:
            print ("Normal")
        elif modifier == 1.5:
            print ("Hard")
        time.sleep(.75)
        textWriter(narrator[24], delay)
    return modifier
def choiceone(delay):
    string = ""
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
    while True:
        try:
            choice = int(string)
        except ValueError:
            print(choiceError)
            string = input(narrator[3])
            continue
        else:
            break
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
    elif (choice >= 5) or (choice < 1):
        choice = 5
        textWriter(narrator[9], delay)
        time.sleep(2)
        textWriter(narrator[5], delay)
        time.sleep(1)
    direction = choice
    return direction