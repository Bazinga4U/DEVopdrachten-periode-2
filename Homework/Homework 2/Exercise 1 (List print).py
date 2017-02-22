class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self,value,tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

node1 = Node(11,Empty)
node2 = Node(22,node1)
node3 = Node(33,node2)

list = Empty()
for i in range(x):
    list = Node(i, list)

while not(list.IsEmpty):
    print(list.Value)
    list = list.PrevNode
