import math
# a=10;
# b=20;
# c=30;

# temp=a;
# a=c;
# c=b;
# b=temp;
# print(a,b,c);


# practical 2 a

# a=int(input("enter the first number \n"));
# b=int(input("enter the second number\n"))

# c= pow(a,2) + pow(b,2);
# result = math.sqrt(c)
# print(c);

#practical 2 b

# a= int(input("enter the first number "))
# b= int(input("enter the second number "))

# c= a+b;
# print("the sum of the number is  ",c);

# practical 3
# a = int(input("enter the number you want to check for the odd and even "))

# if(a%2==0):
#     print("the numbre is even")

# else:
#     print("the number is odd")

# practical 3 b
# for i in range(2,10):
#     result  =float(1/i)
#     print(" the floating value of ", "1/",i,"is",f"{result :.2f}","\n")

#practical 3 c
# arr=[1,2,3]
# for i in arr :
#     print(i) 

# practical 3d 
# a= int(input("enter the number "))

# while(a>=0): 
#     print(a)
#     a=a-1

# a = 3 + 5j
# print(a)
# print(a.real) # 3.0
# print (a.imag)# 5.0

# b= 67/10
# c= 67//10 # float division give 
# print(b)
# print(c)

# a='abcdefghi'

# print(a[2:9:2]) # slicing

# a="computer science and Engineering"
# print(a.capitalize()); # only first elem
# print(a.title()) # elem after spaces also

 # LIST
# x=["abc",10]
# print(x[0])
# print(x)

#TUPLE
# a=(10,"x",30.144)
# print(a)
# print(a[0])
# print(type(a))

#dictionary
# a ={
#     "name": "sahil",
#     "clas": 12
# }
# print(a.keys())
# print(a.items())
# print(type(a))

# arr1=[2,5,7,9]
# arr2=[2,1,12,6]

# for i in arr1:
#     print(arr1[i])

# a=20;
# b=12;
# print(a+b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)
# print(a**b)

# a=10
# b=5
# c=a^b #xor
# print(a<<2) #left shift by 2

#membership operators
# a=[10,20,30]
# b=20
# print( b in a)

# z="computer"
# c="h"
# print("z" not in z)

# identity operator
# a=[10,20,30]
# b=[10,20,30]
# print( a is  b)

#teranary operator
# a=10
# b=5
# print(a if a>b else b)
# print(b if a>b else a) # gives left value

# control statement 
# decision statement - if , elif, else
# conditional 
# if statement (:) and indentation (4 white spaces )
# age = int(input("ente ryour age : "))
# if age >= 18:
#     print("Eligible")
# else:
#     print("In-Eligible")


# if - else 
# attendence = float(input("Enter yor attendence : "))
# if attendence >= 75:
#     print("Eligible to give exams ")
# else :
#     print("In Elligble to give exams .")


# if elif else:
# age = int(input("enter your age : "))
# if age >= 18:
#     print("Eligible")
# elif age<0:
#     print("Invalid")
# else:
#     print("In eligible")


# nested if else :

# at=int(input("enter your attendence "))
# marks=int(input("enter your marks "))

# if marks>30:
#     if at>75:
#         print("eligible")
#     else:
#         print("your attendence is low")    
# else:
#     print("not eligible because of low marks")     


# iterative statement - loops - for , while 
# for loop = if the condition is known
# for i in range (2,6,3):
#     print(i)
# # while loop = if the condition is not known
# i=1
# while  i<6:
#     print(i)
#     i+=1

# nested loop

# for i in range(1,4):
#     for a in range(1,4):
#         print(i,a)
       



# loop control statement - 
# break 
# for i in range (6):
#     print(i)
#     if i==3:
#         break

# continue 
# for i in range (6):
#     if i == 2:
#         continue
#         print(i)


# pass 
# eat fivestar do nothing 

# a="computers"
# print(a)

# print(a.upper())
# print(count(a))

# for i in range(1,5):
#     print(i,end = " ")

# for i in range(1,5):
#     for j in range (5,i,-1):
#         print("*",end = " ")
#     print()

# function arguments types 
# 1.positional argument
# 2. keyword argument(age=20,name ="gauravv")
# 3. default argumaent defaulty defined in the function if not passed by the argument
x=20
def func(a):
    x=22
    print("hello by func ",)


func(x)