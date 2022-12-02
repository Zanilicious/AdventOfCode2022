# Input stored in file
# Open file
f = open("input_day_1.txt", "r")

# Set up parameters
line = " "
int_array = [0]
i = 0
# Read line by line, add inputs into array until empty space
# New array entry starts following that
while line != "":
    line = f.readline()
    if line == "":
        break
    elif line == '\n':
        int_array.append(0)
        i += 1
    else:
        int_array[i] += int(line)

# For problem two, simple solution of finding max and adding for top three max values
a = max(int_array)
del int_array[int_array.index(max(int_array))]
b = max(int_array)
del int_array[int_array.index(max(int_array))]
c = max(int_array)
del int_array[int_array.index(max(int_array))]

# Present added max top three values
print(a + b + c)