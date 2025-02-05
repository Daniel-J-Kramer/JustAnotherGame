import time
import random
import textWriter
import narrator
import choices
import paths
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
textWriter.textWriter(narrator.strings[0], delay)
time.sleep(1)
textWriter.textWriter(narrator.strings[1], delay)
time.sleep(1)
textWriter.textWriter(narrator.strings[2], delay)
time.sleep(1)
choice = choices.choiceone(delay)
path = paths.pathone(choice)
print("")
textWriter.textWriter(narrator.strings[11], delay)
time.sleep(1)
textWriter.textWriter(narrator.strings[12], delay)
time.sleep(1)
textWriter.textWriter(narrator.strings[13], delay)
modifier = choices.choicedifficulty(delay)
time.sleep(1)
