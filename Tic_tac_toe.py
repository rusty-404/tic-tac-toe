def drawfield(field): #row = input(), column = input()):
    for row in range(5):
        if row % 2 == 0:
            practicalrow = int(row / 2)
            for column in range(5):
                if column % 2 == 0:
                    praticalcolumn = int(column / 2)
                    if column != 4:
                        print(field[praticalcolumn][practicalrow], end="")
                    else:
                        print(field[praticalcolumn][practicalrow])
                else:
                    print("|", end="")
        else:
            print("------")
    return True


currentfield = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
drawfield(currentfield)
player = 1
while True:
    print("playerturn: ", player)
    moverow = int(input("Enter row here\n"))
    movecolumn = int(input("Enter column here\n"))
    if player == 1 :
        # make move for player 1
        if currentfield[movecolumn][moverow] == " ":
            currentfield[movecolumn][moverow] = "X"
            player = 2
    else:
        # make move for player 2
        if currentfield[movecolumn][moverow] == " ":
            currentfield[movecolumn][moverow] = "O"
            player = 1
    drawfield(currentfield)



