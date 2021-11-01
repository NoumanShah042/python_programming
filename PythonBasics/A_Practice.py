# #
# # def factorial(n):
# #     result = 1
# #     for i in range(1,n+1):
# #         result = result*i
# #     return result
# #
# #
# # n = int(input('Enter a number: '))
# # result = factorial(n)
# # print(n, '! = ', result, sep="")
#
# def factor(num):  # todo factorial
#     fact = 1
#
#     if num < 0:
#         print("Sorry, factorial does not exist for negative numbers")
#         return
#     for i in range(num, 0, -1):
#         fact = i*fact
#     return fact   # todo work
#
#
# print(factor(6))
#


import math

#
# print(math.sin(0.5))
#
# pi = 22 / 7
# degree = math.sin(0.5)
# radian = degree * (pi / 180)
# print(radian)


# # a= float(input("num"))
# print(math.asin(-1))
# print(math.asin(1))



# mobile = input("enter Mobile as XXXX-XXXXXXX:")
# while len(mobile) != 12  and :
#     mobile = input("input Valid Mobile Number :")
# print("valid length")
# while mobile[4] != '-':
#     mobile = input("input Valid Mobile Number :")
# print("valid -")
# while mobile[:4].isdigit() is not True:
#     mobile = input("input Valid Mobile Number :")
# print("valid 0-4")
# while mobile[5:].isdigit() is not True:
#     mobile = input("input Valid Mobile Number :")
# print("valid 5:end")
# print(mobile)


def input_mail():
    email = input("Email as xxxxx@xxxx.com :")
    print(1 and 1)
    print(1 and 0)
    while (email.find('@') == -1) or (email[-4:] != ".com"):

        email = input("input Valid email:")
    print(email[-4:])
    print(email.find('@') != -1)
    print(email[-4:] == ".com")
    return email


print(input_mail())