# *args fuction-- by using * infront of value in arugement we can pass multiple values

# def print_multiple_argu(*args):
#     #*args -> list
# for i in args:  # ask mahesh what is the error is about
#         print(i)
#
# print_multiple_argu("shaan")
# print_multiple_argu("shan","shantanu","tushar")
# print_multiple_argu("amit",10,True, False)

# write code for pizza toppings
# topping- mushroom,panner, olive, corn ,tomato

def make_pizza(*toppings):
        for i in toppings:
                print(i)

shaan=make_pizza("corn","paneer")
tushar=make_pizza("tomato","olive")
tanvi=make_pizza("mushroom")


