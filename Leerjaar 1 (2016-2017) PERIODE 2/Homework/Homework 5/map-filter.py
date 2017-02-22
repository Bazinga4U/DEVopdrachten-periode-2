class Empty:
    def IsEmpty(self):
        return True

    def __str__(self):
        return "[]"

    def __rlshift__(self, v):
        return Node(v, self)

    def Sum(self):
        return 0

    def Length(self):
        return 0

    def Map(self, f):
        return self

    def Filter(self, p):
        return self


class Node:
    def IsEmpty(self):
        return False

    def Head(self):
        return self.head

    def Tail(self):
        return self.tail

    def __init__(self, x, xs):
        self.head = x
        self.tail = xs

    def __rlshift__(self, v):
        return Node(v, self)

    def __str__(self):
        return str(self.head) + " <<" + str(self.tail)

    def Sum(self):
        return self.head + self.tail.Sum()

    def Length(self):
        return 1 + self.tail.Length()

    def Map(self, f):
        return Node(f(self.head), self.tail.Map(f))

    def Filter(self, p):
        xs = self.tail.Filter(p)
        if p(self.head):
            return Node(self.head, xs)
        else:
            return xs



Empty = Empty()
l = Node(5, Node(9, Node(-1, Empty)))
print(Node.IsEmpty(l))
print(Node.Length(l))
print(Node.Sum(l))
print(Node.Filter(l, lambda x: x % 3))
print(Node.Map(l, lambda x: x * 2))
