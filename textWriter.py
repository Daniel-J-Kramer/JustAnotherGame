import time
def textWriter(string, delay):
    length = len(string)
    char = ""
    finalstring = ""
    for c in range(0, length):
        char = string[c]
        finalstring += char
        time.sleep(delay / 2)
        if c < (length - 1):
            print(finalstring, end='\r')
        else:
            print(finalstring)