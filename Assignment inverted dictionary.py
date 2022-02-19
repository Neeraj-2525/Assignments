# Name = Neeraj Kumar
# Roll No. = 21/73038

"""
_________________________________
To take dictionary as input from
user and inverting the dictionary
_________________________________
"""
print(__doc__)
dict1 = eval(input("Enter the dictionary: "))
invrtd_dict = {}
for key, value in dict1.items():
    if value not in invrtd_dict.keys():
        invrtd_dict[value] = [key]

    else:
        invrtd_dict[value].append(key)

print("original dictionary is", dict1)
print("inverted dictionary is", invrtd_dict)