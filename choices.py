import NarratorStrings
import textWriter
import time
import random
#End import list
#Begin variable list
choiceError = "Please enter a whole number. "
#End variable list
#Begin game code
def choicespeed(delay):
    string = ""
    textWriter.textWriter("How fast should I talk?", delay)
    textWriter.textWriter("1. this slow?", .1)
    textWriter.textWriter("2. this mediocre?", .05)
    textWriter.textWriter("3. this fast?", .01)
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
        textWriter.textWriter("Thank you for choosing properly", delay)
    elif delay == 2:
        delay = .05
        textWriter.textWriter("Thank you for choosing properly", delay)
    elif delay == 3:
        delay = .01
        textWriter.textWriter("Thank you for choosing properly", delay)
    else:
        print("You're kidding right? Oh well, I will choose for you")
        print("")
        delay = .05
    return delay
def savechoice(string, delay):
    save = 0
    return save
def choicedifficulty(delay):
    difficulty = 0
    modifier = 0
    string = ""
    textWriter.textWriter("1. Easy", delay)
    time.sleep(.5)
    textWriter.textWriter("2. Normal", delay)
    time.sleep(.5)
    textWriter.textWriter("3. Hard", delay)
    time.sleep(.5)
    textWriter.textWriter("4. Why choose anything harder?", delay)
    time.sleep(.5)
    while True:
        try:
            difficulty = int(string)
        except ValueError:
            print(choiceError)
            string = input(NarratorStrings.strings[3])
            continue
        else:
            break
    if difficulty == 1:
        textWriter.textWriter(NarratorStrings.strings[14], delay)
        time.sleep(.75)
        textWriter.textWriter(NarratorStrings.strings[15], delay)
        modifier = .5
    elif difficulty == 2:
        textWriter.textWriter(NarratorStrings.strings[16], delay)
        time.sleep(.75)
        textWriter.textWriter(NarratorStrings.strings[17], delay)
        modifier = 1
    elif difficulty == 3:
        textWriter.textWriter(NarratorStrings.strings[18], delay)
        time.sleep(.75)
        textWriter.textWriter(NarratorStrings.strings[19], delay)
        modifier = 1.5
    elif difficulty == 4:
        textWriter.textWriter(NarratorStrings.strings[20], delay)
        time.sleep(.75)
        textWriter.textWriter(NarratorStrings.strings[21], delay)
        modifier = 2
    else:
        difficultyList = [.5, 1, 1.5]
        textWriter.textWriter(NarratorStrings.strings[22], delay)
        time.sleep(.75)
        textWriter.textWriter(NarratorStrings.strings[23], delay)
        modifier = random.choice(difficultyList)
        if modifier == .5:
            print("Easy")
        elif modifier == 1:
            print ("Normal")
        elif modifier == 1.5:
            print ("Hard")
        time.sleep(.75)
        textWriter.textWriter(NarratorStrings.strings[24], delay)
    return modifier
def choiceone(delay):
    string = ""
    textWriter.textWriter("1. A Good Place", delay)
    time.sleep(.5)
    textWriter.textWriter("2. A Bad Place", delay)
    time.sleep(.5)
    textWriter.textWriter("3. A So-So Place", delay)
    time.sleep(.5)
    textWriter.textWriter("4. A Weird Place", delay)
    time.sleep(.5)
    textWriter.textWriter("5. A Random Place", delay)
    time.sleep(.25)
    while True:
        try:
            choice = int(string)
        except ValueError:
            print(choiceError)
            string = input(NarratorStrings.strings[3])
            continue
        else:
            break
    if choice == 1:
        textWriter.textWriter(NarratorStrings.strings[4], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        time.sleep(1)
    elif choice == 2:
        textWriter.textWriter(NarratorStrings.strings[6], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        time.sleep(1)
    elif choice == 3:
        textWriter.textWriter(NarratorStrings.strings[7], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        time.sleep(1)
    elif choice == 4:
        textWriter.textWriter(NarratorStrings.strings[8], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        time.sleep(1)
    elif choice == 5:
        textWriter.textWriter(NarratorStrings.strings[9], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        time.sleep(1)
    direction = choice
    return direction
