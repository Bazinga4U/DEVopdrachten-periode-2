class Player:
    def __init__(self,name,x,y):
        self.Name = name
        self.Position = Position(x,y)

class Position:
    def __init__(self,x,y):
        self.X = x
        self.Y = y

pl1 = Player("Tim", 3.0, 5.5)
pl2 = Player("Tom", 1.2, 3.0)
