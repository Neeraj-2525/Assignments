# Write a function to determine whether a number is prime or not!
# Name : NEERAJ KUMAR
# Roll No : 21/73038

def prime(num):
    if num > 1:                            # As 1 is not a prime number
        for i in range(2, num + 1):
            if num % i == 0:
                print(num, "is not prime number")
                break

        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")

    print("prime numbers till", num)
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


def main():
    print("To check whether a number is prime or not")
    num = int(input("Enter the number: "))
    prime(num)


main()