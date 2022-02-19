# Name = Neeraj Kumar | Roll No. = 21/73038
# To remove the duplicate elements from a list
def remove(old_list):
    final_list = []
    for num in old_list:
        if num not in final_list:
            final_list.append(num)
    return final_list


if __name__ == '__main__':
    duplicate = eval(input("Enter the list: "))
    print(remove(duplicate))