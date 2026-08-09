# sum of 3 nos from user input if user doesnt enter any no then use 100,200,300

num1=int(input("Enter a num1"))
num2=int(input("Enter a num2"))
num3=int(input("Enter num3"))

def sum_of_3(a=100,b=200,c=300):
    return num1+num2+num3
result=sum_of_3(num1,num2,num3)
print(result)
result=sum_of_3()
print(result)

