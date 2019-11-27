# Simple validation script for list presence.
import random

# Populate List
num1 = random.randint(1, 20)
num2 = random.randint(1, 20)
num3 = random.randint(1, 20)
num4 = random.randint(1, 20)
num5 = random.randint(1, 20)
num6 = random.randint(1, 20)

sample_list = [num1, num2, num3, num4, num5, num6]
#sample_set = set(sample_list)

print(sample_list)

# Take Input
selection = int(input("Choose a number from the list for validation:   "))

# Validate and return
if selection in sample_list:
    print("Yes")
else:
    print("No")