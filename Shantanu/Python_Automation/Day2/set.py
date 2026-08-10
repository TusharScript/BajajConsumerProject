# Set(): A Set in Python programming is an un`ordered collection data type that is iterable,
# mutable and has no duplicate elements. In a python set are written in curly brackets{}
# a set is mutable(changeable)


# ex 1: creating set
# myset1={"apple","banana","cherry"}
# print(myset1)        #{'banana', 'apple', 'cherry'} is unordered
#
# s={"shantanu","tushar","mahesh","nachiket"}
# print(s)

# ex 2: accessing items from a set.
# mylist={"apple","banana","cherry"}
# for i in mylist:
#     print(i)
# banana
# apple
# cherry

# s = {"shantanu", "tushar", "mahesh", "nachiket"}
# for i in s:
#     print(i)
# nachiket
# shantanu
# mahesh
# tushar

# ex 3: value exists in set or not.
# myset={"apple","banana","cherry"}
# print("banana" in myset)        #True
#
# s = {"shantanu", "tushar", "mahesh", "nachiket"}
# print("tushar" in s) # true
# print("akshay " in s) # false

# ex 4: adding items in set.        add()(for single item) and update()(for multiple items) function.
# myset={"apple","banana","cherry"}
# # myset.add("orange")
# print(myset)        #{'banana', 'apple', 'cherry', 'orange'}
#
# myset.update(["chiku","pineapple","greps"])
# print(myset)    #{'chiku', 'apple', 'banana', 'greps', 'pineapple', 'cherry'}
#
# s = {"shantanu", "tushar", "mahesh", "nachiket"}
# s.add("akshay")
# print(s) #{'shantanu', 'nachiket', 'mahesh', 'tushar', 'akshay'}
#
# s.update(["saurabh","shaan","jay"])
# print(s) #{'jay', 'shantanu', 'shaan', 'nachiket', 'mahesh', 'saurabh', 'tushar', 'akshay'}

# ex 5: find number of items in set:
# myset={"apple","banana","cherry"}
# print(len(myset))       #3
#
# s = {"shantanu", "tushar", "mahesh", "nachiket"}
# print(len(s)) #4

# ex 6: Remove items from set.   remove() and discard()
# myset={"apple","banana","cherry","chiku","pineapple","greps"}
# myset.remove("banana")
# print(myset)
#
# myset.discard("cherry")
# print(myset)
#
# s = {"shantanu", "tushar", "mahesh", "nachiket"}
# s.remove("nachiket")
# print(s) #{'mahesh', 'tushar', 'shantanu'}
#
# s.discard("tushar")
# print(s) #{'mahesh', 'shantanu'}

# difference between remove and discard is if we try to delete the item which is not available,
#   remove will through error
# but discard will not through any error.


# ex 7: Clear all the items from set.
# myset={"apple","banana","cherry","chiku","pineapple","greps"}
# # myset.clear()
# print(myset)        #set()
#
# # delete variable also
# del myset
# print(myset)

# s = {"shantanu", "tushar", "mahesh", "nachiket"}
# s.clear()
# print(s) #set()

# Ex 8: Joining 2 sets-  union()
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)     #{1, 2, 3, 'a', 'c', 'b'}

# update():
# set1.update(set2)
# print(set1)     #{1, 'b', 2, 3, 'c', 'a'}

# s1={1,2,3,}
# s2={4,5,6}
# #
# # s3=s1.union(s2)
# # print(s3) #{1, 2, 3, 4, 5, 6}
#
# s1.update(s2)
# print(s1) #{1, 2, 3, 4, 5, 6}
#
# ## a =[1,1,2,3,4,3,4,3,2,1,5,5,3,5,3,2,4,4,2,4] remove repeated value from list
# a =[1,1,2,3,4,3,4,3,2,1,5,5,3,5,3,2,4,4,2,4]
# print(set(a))       #{1, 2, 3, 4, 5}    # set returns only unique values