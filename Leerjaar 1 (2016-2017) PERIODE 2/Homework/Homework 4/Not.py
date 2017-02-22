def draw_grid(x_dim,y_dim,p):
    res =""
    x =0
    y =0
    while ((y<y_dim)):
        while ((x<x_dim)):
            if (p(x,y)):
                res=(res+"#")
            else:
                res=(res+" ")
            x=(x+1)
        res=(res+"\n")
        x=0
        y=(y+1)
    return res

NOT=lambda p:lambda x,y:(not p(x,y))

left=lambda x,y:(x ==0)
right=NOT (left)
res=draw_grid (2,2,right)

#Answer 1 = 3
#Answer 2 = 3
#Answer 3 = "  "
#Answer 4 = "*"
#Answer 5 = " "
#Answer 6 = null
#Answer 7 = 3
#Answer 8 = "***"
#Answer 9 = ""
#Answer 10 = 3
#Answer 11 = "*****"
#Answer 12 = ""
#Answer 13 = "*****\n"
#Answer 14 = " ***\n*****\n "
#Answer 15 = "  *\n ***\n*****\ n "
#Answer 16 = null
