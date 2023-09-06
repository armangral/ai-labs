
def count (x):
    y = 0
    for i in range(0,x+1):
        if(i % 2 != 0):
            y=y+1
    return y

 

def lowertriangle(x):
    for i in range(5,0,-2):
        n = x-i
        y = int(n/2)
        for j in range (0,y):
            print(" ",end=" ")
        for star in range(0,i):
            print("*",end=" ")
        
        for j in range (0,y):
            print(" ",end=" ")
        print("\n")


def lowershape(x,limit):
    n = x
    for i in range (limit,0,-1):
        n = n + 2
        for v in range(1,i):
            print(" ",end=" ")
        for j in range(0,n):
            print("*",end=" ")
        for v in range(1,i):
            print(" ",end=" ")
        print("\n")
    lowertriangle(n)
        


def uppershape(x,limit,lower):
    n = x
    for i in range(0,limit):
        for v in range(1,i+1):
            print(" ",end=" ")
        for j in range(0,n):
            print("*",end=" ")
        for v in range(1,i+1):
            print(" ",end=" ")
        n = n-2
        print("\n")
    if(lower == 1):
        lowerimit = limit - 1
    elif(lower == 0):
        lowerimit = limit

    lowershape(n + 2,lowerimit)



def uppertriangle(x,limit):
    n = x
    upper=0
    lower = 0
    for i in range(0,3):
        n = n-1
        y = n/2
        for j in range (0,n):
            if(j==y):
                for star in range(i,3*i+1):
                    print("*",end=" ")
            print(" ",end=" ")
        n = n-1
        print("\n")
    if(limit % 2 == 0):
        upper = int(limit / 2)
        lower = 0
    else:
        upper = int(limit/2)+1
        lower = 1

    uppershape(x,upper,lower)
        
        

    

x = int(input("Enter star number:"))


center =  count(x)
center =  center -3


# upper = int(center/2) + 1
# print(upper)
uppertriangle(x,int(center))


             

