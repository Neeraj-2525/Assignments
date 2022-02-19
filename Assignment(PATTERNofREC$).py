# Name = Neeraj Kumar
# Roll No. = 21/73038
""""""
"""
                                        $ $ $ $ $
                                        $       $
To print the following pattern:-        $       $
                                        $       $
                                        $ $ $ $ $

"""

def print_rectangle(n,m):

    for i in range(1,n+1):
        for j in range(1,m+1):

            if (i ==1 or i == n or j ==1 or j ==m) :
                print("$", end="")
            else:
                print(" ", end="")
        print()

n = int(input("enter the number of rows: "))
m = int(input("enter the number of columns: "))
print_rectangle(n,m)

