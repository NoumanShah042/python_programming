# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# lambda  parameters: return_expression

"""
PEP stands for Python Enhancement Proposal. A PEP is a design document
providing information to the Python community, or describing a new feature
for Python or its processes or environment. The PEP should provide a concise
technical specification of the feature and a rationale for the feature.

PEP8 is for humans but your program will run even if you do not follow it.
If you do not share your code and do not plan to do so, do whatever you want.
If you plan to share some part of your code someday, then you should follow PEP8.

"""
# -----------------------------------
#  by using simple function

# def double(x):
#     return x*2
# print(double(1))

# ------------
# do same by using lambda function

double = lambda x: x * 2             # here we are not following PEP8
print(double(1))

# -----------------------------------

multiply = lambda x, y: x * y
print(multiply(1, 2))

add = lambda x, y, z: x + y + z
print(add(1, 2, 3))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Bro", "Code"))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))
