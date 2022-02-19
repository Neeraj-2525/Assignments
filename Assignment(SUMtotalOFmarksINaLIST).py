def main():
    subjectMarks = eval(input("Enter the list: "))
    sumTotal = 0
    for sublist in subjectMarks:                              # sumtotal of list provided by user
        print(sublist[0],":", sublist[1])
        sumTotal += sublist[1]
    print("Total : ", sumTotal)


main()

