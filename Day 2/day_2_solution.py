# Decodes symbol and returns corresponding move
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
    totalScore = 0
    while line != "":
        line = f.readline()
        if line != "":
            # Removes leading newline char and splits on space
            line = line.strip("\n").split(' ')
            opponentMove = decodeMove(line[0])
            playerMove = decodeMove(line[1])
            
            # Find the score based on both moves per round
            totalScore += scoreCalc(opponentMove, playerMove)
    
    f.close()
    return totalScore

# Puzzle input stored in file with following name
filename = "day_2_input.txt"
totalScore = readFile(filename)
print(totalScore)