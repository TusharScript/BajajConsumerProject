#The terms parameter and argument can be used for the same thing: information that are passed into a function.
# without parameter/argument or no return type and no argument

# def fun():
#  print("hello world")
#
# fun()

# 2.no return type with argument
# def name(name):
#   print("hello", name)
#
# name("shantanu")

# # 3. no return type with default argument
# def default_argu(name="Shaan"):
#   print("hii", name)
#
# default_argu() # hii shaan -- will print whta is the default argument
# default_argu("shantanu") # hii shantanu -- will print the rgument which is passed here

## we can pass multiple arguments --
#
# def multi_argu(name1="a", name2="b"):
#     print("hello",name1,name2)
# multi_argu()
# multi_argu(name2="shaan")
# multi_argu(name1="shaan",name2="shaantanu")
# multi_argu(name1="boss")

# 4. argument with return tpe

# def sum_of_2(a,b):
#     return a+b
#
# result=sum_of_2(3,4)
# print(result)

def sum_of_2_default(a=100,b=200):
    return a+b
#print(sum_of_2_default())
result=sum_of_2_default(a=1,b=2)
print(result)
result=sum_of_2_default()
print(result)








