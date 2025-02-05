import time
import random
import narrator
import textWriter
#End import list
#Begin variables list
path = 0
#End variables list
#Begin game code
def pathone(choice):
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
    elif choice == 5:
        pathonelist = [1, 2, 3, 4]
        path = random.choice(pathonelist)
    return path