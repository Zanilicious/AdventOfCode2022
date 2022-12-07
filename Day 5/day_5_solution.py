import string

# Read the file and return the data divided into crate drawing and move instruction list
# Truncates the newline character
def read_file(file_name):
    f = open(file_name, "r")

    crate_drawing = []
    move_instructions = []
    for line in f:
        if line[0] != "m" and line != "\n" and line[1] != "1":
            crate_drawing.append(line.strip())
        else:
            move_instructions.append(line.strip())
    
    f.close()

    return crate_drawing, move_instructions

# Transforms the "crate drawing" into a matrix for easier handling
# Arrays contain stacks
def transform_drawing_to_matrix(crate_drawing):
    crate_matrix = [""]*9 # Should not be done manually
    

    for line in crate_drawing:
        index = 0
        for line_val in range(len(line)):
            if ((line_val-1)%4 == 0):
                if line[line_val] != " ":
                    crate_matrix[index].append(line[line_val])
                index += 1

    return crate_matrix

# Reduces instructions to numbers
def instruction_reduction(move_instructions):

    return reduced_instructions

# Moves crates as instructed in the reduced instructions
def move_cargo(crate_matrix, reduced_instructions):

    return new_matrix

# Prints the crates at the top of each stack
# def print_top_crates(new_matrix):


# Fun, optional function to visualize the movement of the crates
# def visualize_move():

file_name = "day_5_input.txt"

crate_drawing, move_instructions = read_file(file_name)

crate_matrix = transform_drawing_to_matrix(crate_drawing)

print(crate_matrix)