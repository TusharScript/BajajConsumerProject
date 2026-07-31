#tuple() is ordered, immutable(cannot change it), faster than list and used in fixed data

# Tuple:A tuple is a collection that is ordered and unchangeable.
# Tuple::: ()
# tuple is immutable.(Change, Append, Insert, remove is not possible)

# ex 1: create tuple:
# mylist3="apple", "banana", "cherry"
# mylist1 = ("apple", "banana", "cherry")
# print(mylist1)

# vari1 = "apple"  #datatype- string
# var2 = "apple",   # datatype- tuple
# var3 = ("apple")  # datatype- string
# var4 = ("apple", "banana")    # datatype- tuple

# ex 2: Access tuple items:
# mylist1 = ("apple", "banana", "cherry")
# print(mylist1[1])       #banana
# print(mylist1[-1])      #cherry

# t=(10,20,30)
# print(t)
# print(t[0])
# print(t[-1])


# ex 3: rang of indexes:
# mylist1 = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# print(mylist1[2:5])     #('cherry', 'orange', 'kiwi')
# print(mylist1[-4:-1])       #('orange', 'kiwi', 'mango')

# t=(10,20,30,4,50,60)
# print(t[1:4]) #(20, 30, 4)
# print(t[:2]) #(10, 20)
# print(t[-3:-1]) #(4, 50)
# print(t[::2]) #(10, 30, 50) --ask mahesh about o/p----------------------------------------
# print(t[-1:-4]) # () --ask mahesh why isnot printing anything

# ex 4: Change the tuple values: It is not possible due it is immutable
# mylist1 = ("apple", "banana", "cherry","orange","kiwi","mango","melon")

# to change, Tuple>> List>> Tuple
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# mylist=list(mytuple)
# print(mylist)       #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']
## mylist.append("Watermelon")
# print(mylist)       #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon', 'Watermelon']
#
# mytuple1=tuple(mylist)
# print(mytuple1)     #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon', 'Watermelon')

# t=(10,20,30,4,50,60)
# b=list(t) # coverted the tuple into list
# print(b) # [10, 20, 30, 4, 50, 60]
# print(type(b)) #<class 'list'>
# b.append(70) # add the value in list
# print(b) #[10, 20, 30, 4, 50, 60, 70]
# c=tuple(b) #converted the list into tuple again\
# print(c) #(10, 20, 30, 4, 50, 60, 70)
# print(type(c)) #<class 'tuple'>


# # ex 5: reading tuple using loop:
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# for i in mytuple:
#     print(i)

# t = (10, 20, 30, 4, 50, 60)
# for i in t:
#      print(i)

# ex 6: Check item in tuple:
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
#
# if "banana" in mytuple:
#     print("Yes")
# else:
#     print("NO")

# t=('shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket')
# if "shantanu" in t:
#  print("shantanu is present")
# else:
#  print("shantanu is not present")

# ex 7: tuple length:
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# print(len(mytuple))  # 7

# t=('shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket')
# print(len(t)) #5


# ex 8: Add items (Not possible)

# ex 9: Copy tuple
# mytuple = ("apple", "banana", "cherry","orange","kiwi","mango","melon")
# mytuple1=mytuple
# print(mytuple1)     #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon')

# t=('shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket')
# tuple=t
# print(tuple)


# ex 10: Removing/Delete items from tuple is Not possible.

# ex 11: Joining of tuple:
# mytuple = ("apple", "banana", "cherry")
# mytuple1= ("orange","kiwi","mango")
# print(mytuple + mytuple1)       #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango')
#
# tuple1=('shantanu', 'tushar')
# tuple2=('saurabh', 'mahesh', 'nachiket')
# print(tuple1+tuple2) #('shantanu', 'tushar', 'saurabh', 'mahesh', 'nachiket')

#ex11 - Swapping of tuple
# tuple1=('shantanu', 'tushar')
# tuple2=('saurabh', 'mahesh', 'nachiket')
# tuple1,tuple2=tuple2,tuple1
# print(tuple1) #('saurabh', 'mahesh', 'nachiket')
# print(tuple2) #('shantanu', 'tushar')

#tuple methods
# t=(1,2,3,4)
# print(t.count(4)) #ask mahesh about it --------------------------------
# print(t.index(3)) #2

#ex12- avg of tuple
t=(10,20,30,40,30)
avg=sum(t)/len(t)
print("average=", avg) #average= 26.0

#tuple unpacking
# t=(1,2,3)
# x,y= point #ask mahesh about this method
# print(x,y)
