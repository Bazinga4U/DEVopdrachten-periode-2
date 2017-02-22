class Player:
    def __init__(self, name, score):
        self.Name = name
        self.Score = score

pl1 = Player(input("Please put in your name player 1: "),0)
pl2 = Player(input("Please put in your name player 2: "),0)

class PaperRockScissors:
    def __init__(self, player1, player2, winner):
        self.Player1 = player1
        self.Player2 = player2
        self.Winner = winner

pl1in = PaperRockScissors(input("Player 1: For Rock choose 0, for Paper choose 1, for Scissors choose 2: "),(input("Player 2: For Rock choose 0, for Paper choose 1, for Scissors choose 2: ")),0)

for pl1in in range (1):
    if (0,0,0):
        print("The game tied")
    elif (0,1,0):
        print("Player 2 won!")
    elif (0,2,0):
        print("Player 1 won!")
    elif (1,0,0):
        print("Player 1 won!")
    elif (1,1,0):
        print("The game tied")
    elif (1,2,0):
        print("Player 2 won!")
    elif (2,0,0):
        print("Player 2 won!")
    elif (2,1,0):
        print("Player 1 won!")
    elif (2,2,0):
        print("The game tied")
