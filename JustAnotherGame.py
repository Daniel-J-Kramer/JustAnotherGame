import time
import random
from textWriter import textWriter
from strings import narrator
from choices import choicedifficulty, choicespeed, choiceone
from paths import twopath, threepath, fourpath, fivepath
import character
#End import list
#Begin game
def main():
    #Begin variables list
    choice = 0
    path = 0
    savestate = 0
    modifier = 0
    delay = .03
    #End variables list
    #Begin game code
    delay = choicespeed(delay)
    time.sleep(.2)
    textWriter(narrator[0], delay)
    time.sleep(1)
    textWriter(narrator[1], delay)
    time.sleep(1)
    textWriter(narrator[2], delay)
    time.sleep(1)
    choice = choiceone(delay)
    path = fivepath()
    print("")
    textWriter(narrator[11], delay)
    time.sleep(1)
    textWriter(narrator[12], delay)
    time.sleep(1)
    textWriter(narrator[13], delay)
    modifier = choicedifficulty(delay)
    time.sleep(1)

if __name__ == "__main__":
    main()