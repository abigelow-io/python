import pathlib

parent_folder = pathlib.Path("C:/Users/abigelow/Documents/GitHub/python/advent_of_code_2019")
data_file = parent_folder / "day1_1_input.txt"
data = open(data_file)

data_list = list(data.readlines())
data_ints = [int(i) for i in data_list]

def fuel_solve(mass):
    return (mass//3)-2

fuel_amounts = [fuel_solve(i) for i in data_ints]

#The below line returned the answer for Part 1
print(sum(fuel_amounts))

# BEGIN PART 2

def fuel_two(mass):
    temp_total = 0
    target = mass
    while True:
        fuel_needed = fuel_solve(target)
        print(fuel_needed)
        if fuel_needed > 0:
            temp_total += fuel_needed
        target = fuel_needed
        if fuel_needed > 0:
            continue
        else:
            return temp_total
            return False

new_fuels = [fuel_two(i) for i in data_ints]
print(sum(new_fuels))

