# Operators In Pythons
# Arithmetic Operators
# Assignment Operators(  = , += , -= , /= , ...)
# Comparison Operators
# Logical Operators  (  and , or , not)
# Identity operators  ( is , is not)
# Membership Operators  (  in , not in )
# Bitwise Operators

# *********************************

# Arithmetic Operators
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6)
# print("5 ** 3 is ", 5**3)
# print("5 % 5 is ", 5%5)
print("15 // 6 is ", 15 // 6)  # flour division operation (return floor of division)
#                               15 / 6 = 2.5     ,,,,   15 // 6 = 2

# *********************************

# Assignment Operators(  = , += , -= , /= , ...)
#
# x = 5
# print(x)
# x += 7     # x = x + 7
# x %= 7     # x = x % 7
# print(x)

# *********************************

# Comparison Operators
# i = 5
# print(i == 5)
# print(i != 5)
# print(i >= 5)
# *********************************

# Logical Operators
# a = True
# b = False

# x = 11
# print((x > 0) and (x < 10))  # Returns True if both statements are true
# print(x < 5 or x < 4)  # Returns True if one of the statements is true
# print(not (x < 5 and x < 10))  # Reverse the result, returns False if the result is true
# print(a and b)
# print(a or b)
# print(a or b)

# *********************************

# Identity operators  ( is , is not)

"""   Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location: """

# a = True
# b = False
# print(a is b)      # false , both are diff objects
# print(a is not b)  # true , both are not same objects

# ********
# ==  , !=          for content comparison
# is  , is not      for object possessivity comparison


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # returns True because z is the same object as x ( both are pointing to same object )

print(x is y)  # returns False because x is not the same object as y, even if they have the same content

print(x == y)  # to demonstrate the difference between "is" and "==": this comparison returns True
#                  because x is equal to y

print(x is not z)  # returns False because z is the same object as x

print(x is not y)  # returns True because x is not the same object as y, even if they have the same content

print(x != y)  # to demonstrate the difference between "is not" and "!=": this comparison returns False
#                   because x is equal to y

# *********************************

# Membership Operators  (  in , not in )

lst = [3, 3, 2, 2, 39, 33, 35, 32]
# print(32 in lst)
# print(324 not in lst)

x = ["apple", "banana"]

print("banana" in x)  # true
print("pineapple" not in x)  # true

# *********************************

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

# print(0 & 2)
# print(0 | 3)
