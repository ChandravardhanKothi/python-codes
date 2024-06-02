name = input("please enter student name : ")
m = int(input("please enter your marks of maths  "))
p = int(input("physics  "))
c = int(input("chemistry  "))
total = m+p+c
per = total/3
print("marks are ",m,p,c)
print("total marks = ",total,"percentage is ",per,"%")
if(per >= 90):
    print("your grade is O ")
elif(per >= 80 and per < 90):
    print("your grade is A+")
elif(per >= 70 and per < 80):
     print("your grade is A")
elif(per >= 60 and per < 70):
    print("your grade is B")
else:
    print("fail")