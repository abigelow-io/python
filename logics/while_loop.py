# Roll 1d100 until you've beaten the threshhold 3 times

import random

threshhold = 50
kill_switch = 0

while kill_switch != 3:
    result = random.randint(1, 100)

    if result >= threshhold:
        print("You have rolled "+str(result))
        print("You have rolled over 25")
        kill_switch += 1
    elif result < threshhold:
        print("You have rolled "+str(result))
        print("Rolling again.")