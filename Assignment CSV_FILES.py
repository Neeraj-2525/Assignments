# Neeraj Kumar
# roll no. 21/73038

import csv


def Student_Marks():
    file_name = input("Enter your file name: ")
    with open(file_name + ".csv", "w") as file:
        write = csv.writer(file)
        write.writerow(['1', 'Neeraj', '99'])
        write.writerow(['2', 'Maddy', '99'])
        write.writerow(['3', 'Samy', '98'])
        write.writerow(['4', 'Manthan', '100'])
        write.writerow(['5', 'Prashant', '95'])
        write.writerow(['6', 'Aman', '95'])


def Print_3_lines():
    file_name = input("Enter your file name: ")
    with open(file_name + ".csv", "r") as file:
        read = csv.reader(file)
        count = 0
        for line in read:
            count += 1
            if count % 3 == 0:
                print(line)


def main():
    choice = int(input("press 1 to make a new file for student marks\n"
                       "press 2 to display the list of every third student\n"
                       ">>>Enter your choice: "))

    if choice == 1:
        Student_Marks()

    elif choice == 2:
        Print_3_lines()

    else:
        print("invalid choice")


if __name__ == '__main__':
    main()