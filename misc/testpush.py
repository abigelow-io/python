print("What is 2 + 2?")
answer = input()
if answer == 4:
    print("Correct")
else:
    print("Incorrect")

print("Please type any string")
answer2 = input()

try:
    answer2_str = str(answer2)
except ValueError:
    print("You didn't provide a string")

var1 = 10
