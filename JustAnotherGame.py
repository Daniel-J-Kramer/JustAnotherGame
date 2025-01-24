import time
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
textWriter.textWriter("How fast should I talk?", delay)
textWriter.textWriter("1. this slow?", .1)
textWriter.textWriter("2. this mediocre?", .05)
textWriter.textWriter("3. this fast?", .01)
delay = .03
delay = choices.choicespeed(input("Choose one, two, or three "))
time.sleep(.2)
textWriter.textWriter(NarratorStrings.strings[0], delay)
time.sleep(1)
textWriter.textWriter(NarratorStrings.strings[1], delay)
time.sleep(1)
textWriter.textWriter(NarratorStrings.strings[2], delay)
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
    modifier = 1
    path = 1
    time.sleep(1)
elif choice == 2:
    path = 2
    modifier = -1
    time.sleep(1)
elif choice == 3:
    path = 3
    modifier == 0
    time.sleep(1)
elif choice == 4:
    path = 4
    modifier = 1
    time.sleep(1)
elif choice == 5:
    path = 5
    time.sleep(1)
print("")
if path != 5:
    textWriter.textWriter(NarratorStrings.strings[11], delay)
    time.sleep(1)
    textWriter.textWriter(NarratorStrings.strings[12], delay)
elif path == 5:
    textWriter.textWriter(NarratorStrings.strings[13], delay)
    time.sleep(1)
    textWriter.textWriter(NarratorStrings.strings[14], delay)
    choices.savechoice(input(NarratorStrings.strings[15]), delay)