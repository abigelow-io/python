import requests as req
import random as random
import tkinter as tk

#window = tk.Tk()

#window.mainloop()

# Character Creator for DND style games. Character Creation rolls are set to 5E standards.
# Written by Adam Bigelow

# Assign Vars

# Build Rolling Function

def stat_roll():
    #Init Rolls list
    roll = [0, 0, 0, 0]

    #Roll 4 times
    roll[0] = random.randint(1, 6)
    roll[1] = random.randint(1, 6)
    roll[2] = random.randint(1, 6)
    roll[3] = random.randint(1, 6)

    #Sort so that the lowest roll is in the [0] position
    roll.sort()

    #Add remaning rolls together and return.
    sum_total = roll[1] + roll[2] +roll[3]
    return sum_total

# Race list
races = []
    
# Create character class and constructor

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.Strength = 0
        self.Dexterity = 0
        self.Constituion = 0
        self.Intelligence = 0
        self.Wisdom = 0
        self.Charisma = 0
        self.std_set = input("Would you like to use the standard set for stat creation? Y or N   ")
        self.assignment_method = input("Auto assign stats? (Yes or No)    ")

    # Write a requester for a namegen API, or develop namegen constructor later.

    # Assignment function for manual stat assignment


    def assign(self):
        
        #Assign stats RANDOM
        
        self.roll1 = stat_roll()
        self.roll2 = stat_roll()
        self.roll3 = stat_roll()
        self.roll4 = stat_roll()
        self.roll5 = stat_roll()
        self.roll6 = stat_roll()
        
        stats_list = [self.roll1, self.roll2, self.roll3, self.roll4, self.roll5, self.roll6]


        stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

        strength = self.Strength
        dexterity = self.Dexterity
        consitution = self.Constituion
        intelligence = self.Intelligence
        wisdom = self.Wisdom
        charisma = self.Charisma

        stat_vars = [strength, dexterity, consitution, intelligence, wisdom, charisma]

        remaining_totals = 6

        print("Rolls:")
        print("Roll 1: "+str(self.roll1))
        print("Roll 2: "+str(self.roll2))
        print("Roll 3: "+str(self.roll3))
        print("Roll 4: "+str(self.roll4))
        print("Roll 5: "+str(self.roll5))
        print("Roll 6: "+str(self.roll6))

        # While stats_list is longer than 0 entries, continue

        while remaining_totals > 0 and True:
            print("Your remaining totals are "+ str(stats_list))
            total_select = input("Please choose a total to be assigned to a stat:   ")

            if total_select in stats_list:
                chosen_total_index = stats_list.index(total_select)
                stats_list.remove(chosen_total_index)
                remaining_totals -= 1
                stat_choice = input("Please choose a stat for assignemnt")
                stat_choice.lower()
                success = 0

                while success == 0:
                    if i in stats != stat_choice:
                        print("Please choose a valid stat by typing the whole word")
                        success = 0
                    else:
                        stat_choice_index = stats.index(stat_choice)
                        stat_choice = stat_vars[stat_choice_index]
                        stat_choice = total_select
                        print("You have assigned "+total_select+" as the value for "+stat_choice+".")
            else:
                print("Please choose a total from the provided list.")
                return True
                

        print("All stats assigned")                
    # Roll Stats

    def roll_stats(self):
        if str(self.std_set) == "Y" or str(self.std_set) == "Yes" and self.assignment_method == "Yes":
            self.Strength = 15
            self.Dexterity = 14
            self.Constituion = 13
            self.Intelligence = 12
            self.Wisdom = 10
            self.Charisma = 8
        elif self.std_set == "N" or self.std_set == "No" and self.assignment_method == "Yes":
            print("Rolling...")
            self.Strength = stat_roll()
            self.Dexterity = stat_roll()
            self.Constituion = stat_roll()
            self.Intelligence = stat_roll()
            self.Wisdom = stat_roll()
            self.Charisma = stat_roll()
        elif str(self.std_set) == "Y" or str(self.std_set) == "Yes" and self.assignment_method == "No":
            stats_list = [15, 14, 13, 12, 10, 8]
            # run outer scope assignment func
        elif str(self.std_set) == "N" or str(self.std_set) == "No" and self.assignment_method == "No":
            assign(self)
        else:
            print("Did not receive valid response regarding stat creation. Proceeding with standard stats.")
            self.Strength = 15
            self.Dexterity = 14
            self.Constituion = 13
            self.Intelligence = 12
            self.Wisdom = 10
            self.Charisma = 8

    def declare(self):
        print(self.name+" is a "+self.char_class+" with the below stats.")
        print("Strength = "+str(self.Strength))
        print("Dexterity = "+str(self.Dexterity))
        print("Constitution = "+str(self.Constituion))
        print("Intelligence = "+str(self.Intelligence))
        print("Wisdom = "+str(self.Wisdom))
        print("Charisma = "+str(self.Charisma))


adam = Character("Adam", "idiot")
adam.assign()
adam.declare()









