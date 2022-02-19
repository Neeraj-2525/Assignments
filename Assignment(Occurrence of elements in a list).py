# Name = Neeraj Kumar | Roll No. = 21/73038
# 1.Write a program that takes a list of lists as an input from the user,
# where each sublist comprise subject name and corresponding marks.
# The program should display sum total of marks
# 2.Count the number of occurrences of a particular list
# 3.Count the number of odd elements in the list
# 4.Count the number of even elements in the list

def sub_marks():
    total = 0
    for ele in lst:
        print(ele[0], ":", ele[1])
        total = total + ele[1]
    return total


def countX(lst, x):
    count = 0
    for element in lst:
        if element == x:
            count = count + 1  # To count number of occurrence of an element in a list
    return count


def oddX(lst):
    count = 0
    for element in lst:
        if element % 2 != 0:
            count += 1
            print(f"Index of {element} is", lst.index(element))
    return count


def evenX(lst):
    count = 0
    for element in lst:
        if element % 2 == 0:
            count += 1
            print(f"Index of {element} is", lst.index(element))
    return count


if __name__ == '__main__':
    lst = eval(input("Enter your list here: "))

    while True:
        choice = int(input("Enter '1' to get the sum total of marks\n"
                           "Enter '2' to count occurrence of a number\n"
                           "Enter '3' to count occurrence of odd numbers\n"
                           "Enter '4' to count occurrence of even numbers\n"))
        if choice == 1:
            print("The subjects are:\n")
            print("total: ", sub_marks())
            break



        elif choice == 2:
            x = int(input("enter the element of which u want to find occurrence: "))
            print(x, 'has occurred', countX(lst, x), 'times')
            break

        elif choice == 3:
            print('odd numbers are occurred', oddX(lst), 'times')
            break

        elif choice == 4:
            print('even numbers are occurred', evenX(lst), 'times')
            break
