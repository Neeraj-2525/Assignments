def digit(list1):
    # printing original list
    print("The original list is : " + str(list1))

    # checking all elements to be numeric using isdigit()
    res = all(ele.isdigit() for ele in list1)

    # printing result
    print("Are all strings digits ? : " + str(res))


def count_odd(list1):
    only_odd = [num for num in list1 if num % 2 == 1]
    odd_count = len(only_odd)

    print("Even numbers in the list: ", len(list1) - odd_count)
    print("Odd numbers in the list: ", odd_count)


def max_ele(list1):
    print("The original list : " + str(list1))

    # Longest String in list
    # using loop
    max_len = -1
    for ele in list1:
        if len(ele) > max_len:
            max_len = len(ele)
            res = ele

    # printing result
    print("Maximum length string is : " + res)


def main():
    print("enter 1 to check the list is numeric or not\n"
          "enter 2 to count the number of odd elements\n"
          "enter 3 to get the largest string\n"
          "enter 4 to reverse the list\n"
          "enter 5 to find the position of an element\n"
          "enter 6 to remove an element\n")

    list1 = eval(input('enter your list here: '))
    choice = int(input('enter your choice: '))
    while True:
        if choice == 1:
            digit(list1)
            break

        elif choice == 2:
            print('entered list is: ', count_odd(list1))
            break

        elif choice == 3:
            max_ele(list1)
            break

        elif choice == 4:
            print('the reverse list is: ', list1[::-1])
            break

        elif choice == 5:
            n = input('enter the element to be search: ')
            print('the position of elements is: ', list1.index(n))
            break

        elif choice == 6:
            x = input('enter the element to be removed: ')
            list1.remove(x)
            print('new list after element removed is: ', list1)
            break

        else:
            print('invalid')
            break


if __name__ == '__main__':
    main()