# Program1: swapping of two numbers
# Approach1
# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)

# Aproach2
# num1=10
# num2=20
# temp=0
# temp=num1
# num1=num2
# num2=temp
# print(num1)
# print(num2)
# ============================================================================

# Program 2 How to check number is  prime
# number should be natural
# factors should be two 1, selfnum
# num=int(input("enter a number"))
# count=0
# if num>1:
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         print("Number is prime")
#     else:
#         print("Number is not prime")

# ===========================================================================

# Program 3: How to find factorial of a number 5*4*3*2*1
# Apraoch1 Using Ternary operator
# def factorial(n):
#     return 1 if (n==0 or n==1) else n*factorial(n-1)
# print(factorial(5))

# input - m@phasi*s output - s@isahp*m
# a="@"
# b= "*"
# string="m@phasi*s"
# change=string[::-1]
# a,b=b,a
# print(change)
#
# print(type(change))


s=input("Enter a stirng = ")
s=s[::-1]
s=s.replace('@','*').replace("#","@").replace('@',"*")
print(s)