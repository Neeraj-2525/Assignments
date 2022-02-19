# Name = Neeraj Kumar | Roll No. = 21/73038
"""
OBJECTIVE: Write a function that takes a list of numbers as input from the user and produces
the corresponding cumulative list where each element in the list at index i is the
sum of elements at index j <= i
"""
def cumulative_sum(lst):
    new_list = []
    j = 0
    for i in range(0, len(lst)):
        j += lst[i]
        new_list.append(j)
    return new_list

if __name__ == '__main__':
    lst = eval(input("enter the list: "))
    print(cumulative_sum(lst))
