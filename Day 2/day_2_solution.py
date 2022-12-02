# Decodes symbol and returns corresponding move
def decodeMove(encodedMove):
    move = ""
    if encodedMove == "A" | encodedMove == "X":
        move = "Rock"
    elif encodedMove == "B" | encodedMove == "Y":
        move = "Paper"
    elif encodedMove == "C" | encodedMove == "Z":
        move = "Scissors"
    return move

# Calculates the score for a round
def scoreCalc(opponentMove, playerMove):
    score = 0

    return score

# Reads and parses the inputs stored in file
def readFile(filename):
    f = open(filename, "r")

    line = " "
    totalScore = 0
    while line != "":
        line = f.readline()
        line.split(" ")
        opponentMove = decodeMove(line[0])
        playerMove = decodeMove(line[1])
        totalScore += scoreCalc(opponentMove, playerMove)
    
    return totalScore

filename = "day_2_input.txt"
totalScore = readFile(filename)
