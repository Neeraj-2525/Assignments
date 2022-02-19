# Name = Neeraj Kumar | Roll No. = 21/73038

def linear_search(t, val):
    """
    To search an element linearly
    and display it
    :param t:
    :param val:
    :return:
    """
    for i in range(0,len(t)):
        # i is random
        if t[i] == val:
            return i


def main():
    t = eval(input("enter the tuple: "))
    val = int(input("enter the element: "))
    i = linear_search(t, val)
    print("value found at index", i)

# calling the function
if __name__ == '__main__':
    main()