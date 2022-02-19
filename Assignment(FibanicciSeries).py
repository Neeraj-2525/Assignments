"""FIBONACCI SERIES"""
"""first=0
second=1
third=first+second              0,1,1,2,3,5,8...
print(third)"""

#Generate first n terms of fibonacci series

n = int(input("Enter the number of times you want to print: "))
first = 0
second = 1
third = first + second
print(first, second, third, end=" ")

for i in range(0,n-3,1):      #as 3 out of 7 terms are printed so n-3=4
    first = second
    second = third
    third = first + second
    print(third, end=" ")

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# number = int(input("enter the number: "))
# print(fib(number))
