# Name = Neeraj Kumar | Roll No. = 21/73038

def StrToSet(x, y):
    """
    To convert the given string to separate sets
    and display the distinct and common elements
    :param x:
    :param y:
    :return:
    """
    x = set(x)  # converting x string to a set
    y = set(y)  # converting y string to a set

    print("(a). First set is: ", x)
    print("(b). Second set is: ", y)
    print("(c). Common characters in both the sets are", x.intersection(y))
    print("(d). Distinct characters in both the sets are", x.union(y))


def main():
    x = input("Enter the first string: ")  # string input from the user
    y = input("Enter the second string: ")  # string input from the user
    StrToSet(x, y)


if __name__ == '__main__':
    main()
