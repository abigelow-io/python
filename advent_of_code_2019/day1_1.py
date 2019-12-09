import pathlib

parent_folder = pathlib.Path("C:/Users/abigelow/Documents/GitHub/python/advent_of_code_2019")
data_file = parent_folder / "day1_1_input.txt"
data = open(data_file)

data_list = list(data.readlines())
data_ints = [int(i) for i in data_list]

def fuel_solve(mass):
    return (mass//3)-2
    
fuel_amounts = [fuel_solve(i) for i in data_ints]

print(sum(fuel_amounts))



