# Read puzzle input and return 2D array with all pairs cleaning sections
def read_file(file_name):
    state = True
    f = open(file_name, "r")
    input = []
    line = ""
    while state:
        line = f.readline()
        if line != "":
            input.append(line.strip().split(","))
        else:
            state = False
    f.close()
    return input

# Generates arrays with all numbers for given input
def generate_arrays(input):
    arrays = input
    m = 0
    for i in arrays:
        n = 0
        for j in i:
            j = j.split("-")
            arrays[m][n] = list(range(int(j[0]), int(j[-1])+1))
            n += 1
        m += 1
    return arrays

# Finds if either of two arrays in a pair is fully contained in the other
def find_fully_contained(arrays):
    amount_fully_contained = 0

    for i in arrays:
        if(all(x in i[0] for x in i[1]) or all(x in i[1] for x in i[0])):
            amount_fully_contained += 1

    return amount_fully_contained

if __name__ == "__main__":
    file_name = "day_4_input.txt"
    input = read_file(file_name)
    arrays = generate_arrays(input)
    amount = find_fully_contained(arrays)

    print(amount)