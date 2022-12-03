# Takes an item and returns its priority
def item_to_prio(item_letter):
    if item_letter.isupper(): return ord(item_letter) - 38
    else: return ord(item_letter) - 96

# Takes each item from the first half
# and compares it to every item in the second half
def find_shared_item(lines):
    for i in lines[0]:
        index = lines[1].find(i)
        if index != -1:
            return lines[1][index]

# Receives the contents of a rucksack
# Divides it into two
def parser(line):
    line = line.split()[0]
    lines = [line[:len(line)//2], line[len(line)//2:]]
    return lines

# Opens the rucksack
# Looks into rucksack
# Divides the contents into two halves - one for each compartment
# Finds the item in both compartments
# Gives the priority for the item and adds it to the total prio
# Finally closes the rucksack and writes down the total prio
def read_file(file_name):
    line = " "
    f = open(file_name, "r")
    prio = 0

    while line != "":
        line = f.readline()
        if line != "":
            lines = parser(line)
            shared_item_letter = find_shared_item(lines)
            prio += item_to_prio(shared_item_letter)
    
    f.close()
    print("The sum priority of all items is:", prio)

file_name = "day_3_input.txt"
read_file(file_name)