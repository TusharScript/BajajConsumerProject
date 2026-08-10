# Global and local variables

# Global variables
# global_var=20 # global variable which is define outside the function
# def function():
#     local_var=10  # local varaiable which is define inside a function
#     print(local_var)
#     print(global_var)
# function()


# global_var=20 # global variable which is define outside the function
# def function():
#     local_var=10  # local varaiable which is define inside a function
#     print(local_var)
#
# function()
# print(global_var)

#
# xy=200
# def fun():
#     global yz #here the global and varable name should mention before the value assinged
#     yz = 290
#     print(yz)
# fun()
# print(xy)


# gv=200
# def func():
#     global gv           #if same name of variable we should mention global
#     xy=100
#     print(xy)
#     print(gv)
#
# func()

xy=200
def func():
    global xy           #if same name of variable we should mention global
    xy=100
    print(xy)

func()      #100
print(xy)     # 100       #if we print global variable then it will consider local variable as global variable.






