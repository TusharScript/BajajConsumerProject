# for i in range(1, 11):
#     if i == 7:
#         continue  # it will skip the code goes back to start point
#         print(i)

# write a program tht print numbres from 0-100. however for multiples of 3 print fizz and for multiples 5 print buzz
# for numbers that are of both 3 and 5 print fizzbuzz.

# for i in range(0,101):
#      # if 1%3 == 0:
#      #     print("fizz") # fizzz isnot printing ask mahesh
#     # if i%5 == 0:
#     #     print("buzz")
#     # if i%3 == 0 and i%5 == 0:
#     #     print("fizzbuzz")
#
for i in range(0,101, 3):
    print("fizz")
for i in range(0,101, 5):
    print("buzz")
for i in range(0,101, 3 and 5):
    print("fizzbuzz")
