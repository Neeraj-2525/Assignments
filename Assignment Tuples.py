# Name = Neeraj Kumar | Roll No. = 21/73038

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
def half():
    a = len(t1)
    midhalf = a//2
    for i in range(midhalf):
        print(t1[i], end=" ")
    print()
    for j in range(midhalf,a):
        print(t1[j], end=" ")

def even():
    for i in range(len(t1)):
        if t1[i] % 2 ==0 :
            print(t1[i], end=" ")


def conc():
    t2 = eval(input("enter your tuple here: "))
    print("original tuple is" + str(t1))
    print("tuple to be concatenated is" + str(t2))
    res = t1 + t2
    print("Tuples after concatenation: " + str(res))
    return res

def maxmin():
    Max = t1[0]
    Min = t1[0]
    for i in range(len(t1)):
        if t1[i] >=Max:
            Max  = t1[i]
        elif t1[i]<= Min:
            Min = t1[i]
    print("Maximum number in the tuple is", Max)
    print("Minimum number in the tuple is", Min)
    return Max, Min

if __name__ == '__main__':
    choice = int(input("Enter 1 to print first and second half elements of tuple\n"
                       "Enter 2 to print the even numbers of the tuple\n"
                       "Enter 3 to concatenate the tuples\n"
                       "Enter 4 to print the Max and Min numbers of the tuple\n"
                       "Enter your choice=> "))
    while True:
        if choice == 1:
            half()
            break
        elif choice == 2:
            even()
            break
        elif choice == 3:
            conc()
            break
        elif choice == 4:
            maxmin()
            break
        else:
            print("invalid choice")
            break
