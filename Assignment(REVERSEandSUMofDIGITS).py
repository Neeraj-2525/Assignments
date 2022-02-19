# Name = Neeraj Kumar
# Roll No. = 21/73038
"""
Objective: To find the sum of digits and reverse of the number provided by the user
"""

import sys
def SumOfDigits(num):
    total = 0
    while num != 0:  # Sum total of digits 2
        digit = num % 10
        total += digit
        num = num // 10
    print(total)
    print()

def reverse(num):
    reverse = 0
    while num != 0:
        digit = num % 10
        reverse = reverse*10 + digit
        num = num//10
    print(reverse)
    print()


def main():
    choice = int(input("press 1 to find sum of digits \npress 2 to find the reverse \npress 0 to exit \n\nEnter your choice:"))
    print()

    while choice != 10:
        if choice == 1:
            num = int(input("Enter your number: "))
            SumOfDigits(num)

        elif choice == 2:
            num = int(input("Enter your number: "))
            reverse(num)

        elif choice == 0:
            break

        elif choice ==10:
            print("invalid choice, run again")
            sys.exit()

        choice = int(input("press 1 to find sum of digits \npress 2 to find the reverse \npress 0 to exit \n\nEnter your choice:"))

main()