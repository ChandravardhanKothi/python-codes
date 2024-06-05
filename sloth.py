# cook your dish here
a = int(input())
for i in range (a):
    x,y,z = map(int,input().split())
    b,j,p = map(int,input().split())
    t1 = x+y+z
    t2 = b+j+p
    if(t1 < t2):
        print("SLOTH")
    if(t2 < t1):
        print("DRAGON")
    if(t1 == t2):
        if(x < b):
            print("SLOTH")
        if(b < x):
            print("DRAGON")
        if(x == b):
            if(y < j):
                print("SLOTH")
            if(j < y):
                print("DRAGON")
            if(y == j):
                print("TIE")
        #print("TIE")