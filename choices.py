import NarratorStrings
import textWriter
import time
#End import list
#Begin variable list
error = "Please enter a whole number. "
#End variable list
#Begin game code
choiceonestrings = [
"1. A Good Place", #0
"2. A Bad Place", #1
"3. A So-So Place", #2
"4. A Weird Place", #3
"5. A Random Place" #4
]
def choicespeed(string):
    while True:
        try:
            delay = int(string)
        except ValueError:
            print(error)
            string = input("Choose one, two, or three. ")
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
def choiceone(string, delay):
    while True:
        try:
            choice = int(string)
        except ValueError:
            print(error)
            string = input(NarratorStrings.strings[3])
            continue
        else:
            break
    modifier = 0
    if choice == 1:
        textWriter.textWriter(NarratorStrings.strings[4], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        modifier = 1
        time.sleep(1)
    elif choice == 2:
        textWriter.textWriter(NarratorStrings.strings[6], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        modifier = -1
        time.sleep(1)
    elif choice == 3:
        textWriter.textWriter(NarratorStrings.strings[7], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        modifier == 0
        time.sleep(1)
    elif choice == 4:
        textWriter.textWriter(NarratorStrings.strings[8], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        modifier = 1
        time.sleep(1)
    elif choice == 5:
        textWriter.textWriter(NarratorStrings.strings[9], delay)
        time.sleep(2)
        textWriter.textWriter(NarratorStrings.strings[5], delay)
        time.sleep(1)
    direction = choice
    return direction