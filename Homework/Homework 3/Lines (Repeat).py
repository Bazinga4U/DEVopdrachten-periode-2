def repeat (symbol,n):
    res = ""
    while ((n>0)):
        res=(res+symbol)
        n=(n-1)
    return(res)

res = repeat("#",3)
print(res)
