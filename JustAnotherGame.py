import time
import random
import NarratorStrings
import choices
import textWriter
#End import list
#Begin variables list
choice = 0
path = 0
savestate = 0
modifier = 0
delay = .03
#End variables list
#Begin game code
delay = choices.choicespeed(delay)
time.sleep(.2)
textWriter.textWriter(NarratorStrings.strings[0], delay)
time.sleep(1)
textWriter.textWriter(NarratorStrings.strings[1], delay)
time.sleep(1)
textWriter.textWriter(NarratorStrings.strings[2], delay)
time.sleep(1)
choice = choices.choiceone(delay)
while (choice < 1) or (choice > 5):
    textWriter.textWriter(NarratorStrings.strings[10], delay)
    time.sleep(1)
    textWriter.textWriter(choices.choiceonestrings[0], delay)
    time.sleep(.5)
    textWriter.textWriter(choices.choiceonestrings[1], delay)
    time.sleep(.5)
    textWriter.textWriter(choices.choiceonestrings[2], delay)
    time.sleep(.5)
    textWriter.textWriter(choices.choiceonestrings[3], delay)
    time.sleep(.5)
    textWriter.textWriter(choices.choiceonestrings[4], delay)
    time.sleep(.25)
    choice = choices.choiceone(input(NarratorStrings.strings[3]), delay)
if choice == 1:
    path = 1
    time.sleep(1)
elif choice == 2:
    path = 2
    time.sleep(1)
elif choice == 3:
    path = 3
    time.sleep(1)
elif choice == 4:
    path = 4
    time.sleep(1)
if choice == 5:
    pathlist = [1, 2, 3, 4]
    path = random.choice(pathlist)
print("")
textWriter.textWriter(NarratorStrings.strings[11], delay)
time.sleep(1)
textWriter.textWriter(NarratorStrings.strings[12], delay)
time.sleep(1)
textWriter.textWriter(NarratorStrings.strings[13], delay)
modifier = choices.choicedifficulty(delay)
time.sleep(1)
