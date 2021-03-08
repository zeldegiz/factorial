def factorial(x,y):
    m = y-x
    if(m==0):
        return x
    elif(m==1):
        return x*(x+1)
    else:
        k = int(m/2)
        return factorial(x,x+k)*factorial(x+k+1,y)
