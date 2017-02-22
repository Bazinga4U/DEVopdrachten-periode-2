class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

def Length(x):
    l = x
    lenght = 0
    while not(l.IsEmpty):
        lenght = lenght + 1
        l = l.Tail
    return lenght

def Sum(x):
    l = x
    sum = 0
    while not(l.IsEmpty):
        sum = sum + l.Value
        l = l.Tail
    return sum

x = Node(5, Node(9, Node(-1, Empty())))

while not(x.IsEmpty):
    print(x.Value)
    x = x.Tail

print('sum: ', Sum(x))
print('lenght: ', Length(x))
