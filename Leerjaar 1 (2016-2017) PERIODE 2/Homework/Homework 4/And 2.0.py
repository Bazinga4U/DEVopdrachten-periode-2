left=lambda x,y:(x==0)
top=lambda x,y:(y==0)

AND=lambda ?,?:
    lambda ?,?:
        (?(?,?)and(?,?)?)

left_and_top=AND(left,top)

a=left_and_top(0,0)
b=left_and_top(0,1)
c=left_and_top(1,0)
d=left_and_top(1,1)
