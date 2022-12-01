# First day of Advent Of Code 2022
# Problem formulation: Inputstream of series of numbers, find the max sequence

f = open("input_day_1.txt", "r")

line = " "
int_array = [0]
i = 0
while line != "":
    line = f.readline()
    if line == "":
        break
    elif line == '\n':
        int_array.append(0)
        i += 1
    else:
        int_array[i] += int(line)

a = max(int_array)
del int_array[int_array.index(max(int_array))]

b = max(int_array)
del int_array[int_array.index(max(int_array))]
c = max(int_array)
del int_array[int_array.index(max(int_array))]

print(a + b + c)