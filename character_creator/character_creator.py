import random as random

# Character Creator for DND style games. Character Creation rolls are set to 5E standards.

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

# Race list. Might incorporate later.
# races = []
    
# Create character class and constructor

class Character:

    # Assignment function for manual stat assignment

    def assign(self):
        
        #Assign stats RANDOM
        if self.std_set == "N":
            self.roll1 = stat_roll()
            self.roll2 = stat_roll()
            self.roll3 = stat_roll()
            self.roll4 = stat_roll()
            self.roll5 = stat_roll()
            self.roll6 = stat_roll()
        elif self.std_set == "Y":
            self.roll1 = 15
            self.roll2 = 14
            self.roll3 = 13
            self.roll4 = 12
            self.roll5 = 10
            self.roll6 = 8
        
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

        while remaining_totals > 0:
            print("Your remaining totals are "+ str(stats_list))
            total_select = int(input("Please choose a total to be assigned to a stat:   "))

            if total_select in stats_list:
                #chosen_total_index = stats_list.index(total_select)
                stats_list.remove(total_select)
                remaining_totals -= 1
                print("These are the stats available for assignment:")
                print(stats)
                

                
                success = 0

                while success == 0:
                    stat_choice = str(input("Please choose a stat for assignemnt:   "))
                    stat_choice.lower()

                    if stat_choice in stats:
                        stat_for_string = stat_choice

                        # Conditional assignments based on stat choice
                        if stat_choice == "strength":
                            self.Strength = total_select
                        elif stat_choice == "dexterity":
                            self.Dexterity = total_select
                        elif stat_choice == "constitution":
                            self.Constituion = total_select
                        elif stat_choice == "intelligence":
                            self.Intelligence = total_select
                        elif stat_choice == "wisdom":
                            self.Wisdom = total_select
                        elif stat_choice == "charisma":
                            self.Charisma = total_select

                        stat_choice_index = stats.index(stat_choice)
                        stats.remove(stat_choice)
                        stat_choice = stat_vars[stat_choice_index]
                        stat_choice = total_select
                        print("You have assigned "+str(total_select)+" as the value for "+stat_for_string+".")
                        success+=1
                    else:
                        print("Please check the spelling of your stat choice and ensure that you are entering the full word.")
                        success = 0
                        continue
                        
            else:
                print("Please choose a total from the provided list.")
                continue
                
        print("All stats assigned") 

        #Character Declaration

        print(self.name+" has the below stats.")
        print("Strength = "+str(self.Strength))
        print("Dexterity = "+str(self.Dexterity))
        print("Constitution = "+str(self.Constituion))
        print("Intelligence = "+str(self.Intelligence))
        print("Wisdom = "+str(self.Wisdom))
        print("Charisma = "+str(self.Charisma))   
    
    def __init__(self):
        self.name = str(input("What is your character's name?   "))
        self.Strength = 0
        self.Dexterity = 0
        self.Constituion = 0
        self.Intelligence = 0
        self.Wisdom = 0
        self.Charisma = 0
        self.std_set = input("Would you like to use the standard set for stat creation? Y or N   ")
        self.assign()

    # Write a requester for a namegen API, or develop namegen constructor later.

                
   

NewChar = Character()









