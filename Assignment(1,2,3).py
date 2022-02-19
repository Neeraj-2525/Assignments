# # A = p*(1 + (R/100))**T        # Formula for compound amount payable
#
# def compound_amount(P, R, T):
#     A = P*(1 + R/100)**T
#     print("compound amount is ",A)
#     return A
# def main():
#     P = int(input("principle: "))
#     R = int(input("rate: "))
#     T = int(input("time(in_years): "))
#     compound_amount(P, R, T)
#
# main()


# """compute hypoteneuse"""
# import math
# def triangle(length, breadth):
#     hypo = math.sqrt(length**2 + breadth**2)
#     print("Hypoteneus: ", hypo)
#
# def main():
#     length = int(input("Enter the length of triangle: "))
#     breadth = int(input("Enter the breadth of triangle: "))
#     triangle(length, breadth)
#
# main()
#
#
# Leap Year

def check_year(year):
    """  Return true if year is a multiple
     of 4 and not multiple of 100.
     OR year is multiple of 400.
    """
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


year = int(input("Enter the year(in number format): "))
if (check_year(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")
#
#
