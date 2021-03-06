import time

# ************************************
# while loop =  a statement that will execute it's block of code,
#                        as long as it's condition remains true

# name = ""       # name=None
#
# # while not name:
#
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello " + name)

# *************************************

# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#                     while loop = unlimited
#                     for loop = limited

# **********

# for i in range(10):  # 0 - 9
#     print(i + 1, end=" ")

# **********

#     range (start, end , step)   # start in inclusive , end is exclusive

for i in range(50, 100 + 1, 2):
    print(i)

# **********

# for i in "Bro Code":
# print(i)   #   Bro Code

# **********

# phone_number = "123-456-7890"
# for i in phone_number:
#     print(i, end="")

# **********

for seconds in range(10, 0, -1):   # 10 to 1
    print(seconds)
    time.sleep(1)
print("Happy New Year!")

# ***************************************


# nested loops =    The "inner loop" will finish all of it's iterations before
#                               finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
