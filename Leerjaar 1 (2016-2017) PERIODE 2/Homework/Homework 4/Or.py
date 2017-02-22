up = lambda x,y: (y==0)
left = lambda x,y: (x==0)
OR = lambda x,y: lambda x,y: (up(x,y) or left (x,y))

top_or_left = OR(up,left)

a = top_or_left(0,0)
b = top_or_left(0,1)
c = top_or_left(1,0)
d = top_or_left(1,1)
print(a,b,c,d)
