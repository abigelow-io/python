import random

crit_threshold = 10
counter = 0
roll_counter = 0
new_crit_alert = 0

while counter != 5:
    if roll_counter > 7:
        crit_threshold = 15
    
    if crit_threshold == 15 and new_crit_alert == 0:
        print("You must now roll higher than a 15.")
        new_crit_alert += 1
        counter = 0
    
    roll = random.randint(1,20)
    
    roll_counter += 1
    
    print("You rolled "+str(roll))
    
    if roll > 10:
        counter += 1
        print("You rolled above "+str(crit_threshold))
    else:
        None