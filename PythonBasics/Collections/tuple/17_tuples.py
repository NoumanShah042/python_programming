# tuple =   collection which is ordered and unchangeable
#           used to group together related data

# for tuple of single element, we need an extra comma after element i.e. a=(1,)


# Tuples in Python :
a = ()    # It's an example of empty tuple
x = (1,)   # Tuple with single value i.e. 1
tup1 = (1, 2, 3, 4, 5)
tup1 = ('harry', 5, 'demo', 5.8)

# ********************************


student = ("Bro", "Bro", "male")

print(student[2])              # return item at specific index of tuple
print(student.count("Bro"))    # count of Bro in tuple (2)
print(student.index("male"))  # return index of element  (3)
print(student.__sizeof__())    # 56

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")


# To change value in tuple, first converted into list and then again in tuple
x = ("a", "b", "c")
y = list(x)
y [2] = "h"
x = tuple (y)

