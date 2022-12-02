# Decodes symbol and returns corresponding move
# For part 1
def decodeMove(encodedMove):
    move = ""
    # move according to problem formulation
    if encodedMove == "A" or encodedMove == "X":
        move = "Rock"
    elif encodedMove == "B" or encodedMove == "Y":
        move = "Paper"
    elif encodedMove == "C" or encodedMove == "Z":
        move = "Scissors"
    return move

# Find the player move based on end condition (win/draw/lose)
# For part 2
def findCorrectMove(symbol, opponentMove):
    if symbol == "X":
        if opponentMove == "Rock":
            move = "Scissors"
        elif opponentMove == "Paper":
            move = "Rock"
        elif opponentMove == "Scissors":
            move = "Paper"
        
    elif symbol == "Y":
        if opponentMove == "Rock":
            move = "Rock"
        elif opponentMove == "Paper":
            move = "Paper"
        elif opponentMove == "Scissors":
            move = "Scissors"
        
    elif symbol == "Z":
        if opponentMove == "Rock":
            move = "Paper"
        elif opponentMove == "Paper":
            move = "Scissors"
        elif opponentMove == "Scissors":
            move = "Rock"
    return move

# Calculates the score for a round
def scoreCalc(opponentMove, playerMove):
    score = 0
    # Different cases depending on opponent and player moves
    if playerMove == "Rock":
        score += 1
        if opponentMove == "Rock":
            score += 3
        elif opponentMove == "Paper":
            score += 0
        elif opponentMove == "Scissors":
            score += 6
    if playerMove == "Paper":
        score += 2
        if opponentMove == "Rock":
            score += 6
        elif opponentMove == "Paper":
            score += 3
        elif opponentMove == "Scissors":
            score += 0
    if playerMove == "Scissors":
        score += 3
        if opponentMove == "Rock":
            score += 0
        elif opponentMove == "Paper":
            score += 6
        elif opponentMove == "Scissors":
            score += 3
    
    return score

# Reads and parses the inputs stored in file
def readFile(filename):
    f = open(filename, "r")

    line = " "
    # Modified to fit part 2
    # [part 1 score, part 2 score]
    totalScore = [0,0]
    while line != "":
        line = f.readline()
        if line != "":
            # Removes leading newline char and splits on space
            line = line.strip("\n").split(' ')
            opponentMove = decodeMove(line[0])
            playerMove = decodeMove(line[1])
            
            # Find the score based on both moves per round
            # Slight modification to calculate part 2 score
            totalScore[0] += scoreCalc(opponentMove, playerMove)
            playerMove = findCorrectMove(line[1], opponentMove)
            totalScore[1] += scoreCalc(opponentMove, playerMove)
    
    f.close()
    return totalScore

# Puzzle input stored in file with following name
filename = "day_2_input.txt"
totalScore = readFile(filename)
print("Score for part 1: ", totalScore[0])
print("Score for part 2: ", totalScore[1])