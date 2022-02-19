# Name = Neeraj Kumar
# Roll No. = 21/73038
"""
To solve the quadratic equation ax**2 + bx + c = 0
"""

import cmath

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = b ** 2 - (4 * a * c)
print("Discriminant of the quadratic equation is", d)

if d > 0:
    print("This quadratic equation has two real solutions")
    x = (-b + cmath.sqrt(d)) / (2 * a)
    y = (-b + cmath.sqrt(d)) / (2 * a)
    print("x = ", x)
    print("y = ", y)
elif d == 0:
    print("This quadratic equation has only one real solution ")
    p = -b / (2 * a)
    print("x=", p)
else:
    print("This quadratic equation has complex solutions")
    x = (-b + cmath.sqrt(d)) / (2 * a)
    y = (-b - cmath.sqrt(d)) / (2 * a)
    print("x =", x)
    print("y =", y)
