#loop examples and practice

given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total = 0

t = -1

while True:
    total += given_list[t]
    t += -1
    if given_list[t] >= 0:
        break

print(total)


###


integers = list(range(1, 100))
total = 0
check_list = []

for int in integers:
    if int % 3 == 0 or int % 5 ==0:
        total += int
        check_list.append(int)

print(total)
print(check_list)