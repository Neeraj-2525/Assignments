# Name = Neeraj Kumar
# Roll No. = 21/73038

# check if all elements are numbers or not

def numeric(Lst):
    flag = False
    for ele in Lst:
        if not (type(ele) == int or type(ele) == float):
            flag = True  # If non-numeric element is found
            print("1. All elements are not numbers!")
            break

    if flag == False:
        print("1. All the elements are numeric")

        print("________________________________________________")

        count = 0
        for i in Lst:
            if type(i) == int and i % 2 != 0:  # To count odd numbers
                count += 1
        print("2. Number of odd elements : ", count)

        print("________________________________________________")

        maxEle = Lst[0]
        for index in range(1, len(Lst)):  # To check the max number
            if Lst[index] >= maxEle:
                maxEle = Lst[index]
        print("3.(a) Maximum number: ", maxEle)

        print("________________________________________________")


def strings(Lst):
    # To check whether list is string or not

    flag = False
    for ele in Lst:
        if not (type(ele) == str):
            flag = True  # if numeric is found
            print("3(b). All elements are not strings!")
            break

    if flag == False:
        print("3(b). All elements are strings!")

        print("________________________________________________")

        maxStr = len(Lst[0])
        for index in range(1, len(Lst)):
            if len(Lst[index]) >= maxStr:  # to find the longest string
                maxStr = len(Lst[index])

        print("3.(b) Longest string is", "'",maxStr, "'")


        print("________________________________________________")

    if flag == False:
        def countAlpha_Dig(Lst):
            count = 0
            count1 = 0
            for i in Lst:
                if i.isalpha():
                    count += 1

                elif i.isdigit():
                    count1 += 1
            print("4.(a) The number of strings with alphabets only is:", count)
            print("4.(b) The number of numeric strings is:", count1)
            return count and count1
        countAlpha_Dig(Lst)

if __name__ == '__main__':
    while True:
        Lst = eval(input("Enter your list here: "))

        choice = int(input("Enter '1' to do numeric operations"
                           "Enter '2' to do string operations"))
        if choice == 1:
            numeric(Lst)

        elif choice == 2:
            strings(Lst)

        else:
            print('invalid input')