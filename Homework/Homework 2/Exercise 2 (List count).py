class Empty:
    def __init__(self):
        self.IsEmpty = empty

class Node:
    def __init__(self,empty,value,tail):
        self.IsEmpty = empty
        self.Value = value
        self.Tail = tail

node1 = Node(11,Empty)
node2 = Node(22,node1)
node3 = Node(33,node2
