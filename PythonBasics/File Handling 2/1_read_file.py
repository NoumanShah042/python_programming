f = open("C:\\Users\\Syed Numan Rehman\\Desktop\\test.txt", "rt")
#                                           open wil return file handler or file pointer

# ***************************
# content = f.read()         #  read complete file and store as string

# content = f.read(34455)    #  read  34455 characters as string
content = f.read(3)          # read  3 characters

# print(type(content))      # <class 'str'>
# print(type(f))            # <class '_io.TextIOWrapper'>
print(content)

# ***************************

# for i in content:       # iterate through file char by char
#     print(i)

# ***************************

# for i in f:              # iterate through file line by line
#     print(i, end="")

# ***************************

# print(f.readline(), end="")  # read next line with new line character at the end of that line
# print(f.readline(), end="")
# print(f.readline(), end="")

# ****************************

# print(f.readlines())   # makes a list of lines of the complete file ( start from the location of pointer f)

# ****************************


f.close()
