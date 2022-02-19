# Name = Neeraj Kumar
# Roll No. = 21/73038
# L.C.M of two user input numbers

def compute_lcm(a, b):
    if a > b:
        greater = a                         # a,b : input numbers by the user
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater                   # lcm : least common multiple
            break
        greater += 1
    return lcm

print("To find the L.C.M")
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
print("LCM is", compute_lcm(a, b))