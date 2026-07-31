# # split string to list:
# Q. count "a" in below string
# a = "my name is Mahesh And OTP is 1234"
# b = a.split()
# print(b)
# count= 0
# for i in b:
#     if "a" in i.lower():  # ask mahesh about this count -------------------------
#         count = count +1
#     print()
# print(count)
from turtle import clear

#  a= "Im batman and i live in dark"
# b=a.split()
# print(b) #['Im', 'batman', 'and', 'i', 'live', 'in', 'dark']

# # Q. find the number in string
# for i in b:
#     if i.isnumeric():
#         print(i)

# mylist1=[10,20,30,40] #also asked about this too -----------------------------------
# mylist2=["apple","banana","cherry"]
# mylist3=list()      #empty list
#
# # ex1: Accessing items from list
# print(mylist2[0])       #apple
# print(mylist2[2])       #cherry
# print(mylist2[-1])      #cherry:  count from the end
#
# a=["shantanu","tushar","mahesh"]
# print(a[1]) #tushar
# print(a[-1]) #mahesh

# ex 2: Range of indexes
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# print(mylist[2:5])      #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])       #['orange', 'kiwi', 'mango']

# mylist=["shantanu","tushar","mahesh","nachiket","saurabh","akshay"]
# print(mylist[1:4]) #['tushar', 'mahesh', 'nachiket']
# print(mylist[:-1]) #'shantanu', 'tushar', 'mahesh', 'nachiket', 'saurabh']


# ex 3: replace the item value
# mylist=["apple","banana","cherry"]
# mylist[0]="orange"
# print(mylist)       #['orange', 'banana', 'cherry']

# a=["shantanu","tushar","mahesh"]
# a[1]="saurabh"
# print(a) #['shantanu', 'saurabh', 'mahesh']

# ex 4: read the list by using loop:
# mylist=["apple","banana","cherry"]
#
# for i in mylist:
#     print(i)

# a=["shantanu","tushar","mahesh"]
#
# for i in a:
#     print(i)


# Ex 5: Check if the item is existed in the list or not:
# mylist=["apple","banana","cherry"]
#
# if "apple" in mylist:
#     print("apple is available")
# else:
#     print("apple is not available")

# a=["shantanu","tushar","mahesh"]
# if "shantanu" in a:
#     print("shantanu is present") #shantanu is present
# else:
#     print("shantanu is missing")

# ex 6: List length and type
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# print(len(mylist))      #7

# a=["shantanu","tushar","mahesh"]
# b=[1,2,3]
# print(len(a)) #3
# print(len(b)) #3
# print(type(a)) #<class 'list'>
# print(type(b)) #<class 'list'>

# ex 7: Add items in list:  By 'append()' and 'insert()'
# mylist=["apple","banana","cherry"]
# # mylist.append("orange")  # append class adds item at end of the list
# # print(mylist)       #['apple', 'banana', 'cherry', 'orange']
#
# mylist.insert(2,"orange") # to insert at specific place
# print(mylist)       #['apple', 'banana', 'orange', 'cherry']

# a=["shantanu","tushar","mahesh"]
# a.append("nachiket") # append class adds item at end of the list
# print(a) #['shantanu', 'tushar', 'mahesh', 'nachiket']
# a.insert(2,"saurabh")
# print(a) #['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']

# ex 8: Remove item from list: pop(), del(keyword), clear()
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]

# mylist.pop(3)       # item will be removed, according to index
# print(mylist)       #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'melon'

# del mylist[2]
# print(mylist)       #['apple', 'banana', 'orange', 'kiwi', 'mango', 'melon']


# mylist.clear()
# print(mylist)       #[], delete all item, but do not delete variable

# a=['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']
# a.pop() # will delete the last (or -1 index) value from list
# print(a) #['shantanu', 'tushar', 'saurabh', 'mahesh']
# a.pop(2)  # item will be removed, according to index
# print(a)  #['shantanu', 'tushar', 'mahesh']

# del a[3] # will delete according to index
# print(a) #['shantanu', 'tushar', 'saurabh', 'nachiket']

# a,clear()
# print(a) # ask it to mahesh --------------------------------------------------------

# ex 9: Copy list:
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# mylist1=list(mylist)
# print(mylist1)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']

# a=['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']
# b=list(a)
# print(b) #['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']

# ex 10:
# mylist=["apple","banana","cherry","orange","kiwi","mango","melon"]
# mylist1=mylist.copy()
# print(mylist1)   #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']
#
# a=['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']
# b=a.copy()
# print(b) #['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']


# ex 11: Joining of a list
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = ["orange","kiwi","mango","melon"]

# Using + operator.
# print(mylist1+mylist2)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']
#
# a=['shantanu', 'tushar', 'saurabh']
# b=[ 'mahesh', 'nachiket']

# print(a+b) #['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']

# by using a loop statement:
# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']

# for i in  b:
#  a.append(i)
# print(a)  #['shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket']

# By using extend() function:
# mylist1.extend(mylist2)
# print(mylist1)      #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']

## printing first letter of strings
# a = ["mahesh","ramesh","suresh","mayur","mangesh"]
# for i in a:
#     print(i[0])

# ## printing 3rd letter of strings
# a=['shantanu', 'tushar', 'saurabh']
# for i in a:
#  print(i[2])
#a
# s
# u


# print string values which start with "m"
# a = ["mahesh","ramesh","suresh","mayur","mangesh"]
#
# for i in a:
#     if i[0]=="m":
#         print(i)

# a=['shantanu', 'tushar', 'saurabh']
# for i in a:
#     if i[0]=="t":
#         print(i) #tushar


# print string values which ends with "h"
# a = ["mahesh", "ramesh", "suresh", "mayur", "mangesh"]
# for i in a:
#     if i[-1]=='h':
#         print(i)
#
# # or
# for item in a:
#     if item.endswith("h"):
#         print(item)
##
# a=['shantanu', 'tushar', 'saurabh']
# for k in a:
#     if k.endswith("h"):
#         print(k) #saurabh


## List comprehension : It is generally a single line of code enclosed in square brackets.
# ask about it to mahesh ---------------------------------------------------
# lst = [1,2,3,4,5,6,7,8,9,10]
#
# a = [x for x in lst]
# print(a)    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# lst = [1,2,3,4,5,6,7,8,9,10]
# a = [x for x in lst if x > 2]
# print(a)
#
# a = ["mahesh", "ramesh", "suresh", "mayur", "mangesh"]
#
# b = [x for x in a if x[-1] == 'h']
# print(b)    #['mahesh', 'ramesh', 'suresh', 'mangesh']
