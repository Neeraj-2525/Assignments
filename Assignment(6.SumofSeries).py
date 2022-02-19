# Name = Neeraj Kumar
# Roll No. = 21/73038
# Objective : 1 - 1/1! + 1/2! - 1/3! + ... + 1/n!

def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def Sum(n):
    sum = 1

    for i in range(1, n + 1):
        division = 1 / fact(i)
        if i % 2 != 0:
            division -= division
        sum += division
    print(sum)

print("Sum of series: 1 - 1/1! + 1/2! - 1/3! + ... + 1/n!")
if __name__ == '__main__':
    print("Sum of series: 1 - 1/1! + 1/2! - 1/3! + ... + 1/n!")
    n = int(input("Enter the number of terms: "))

    Sum(n)
