
# Name = Neeraj Kumar
# Roll No. = 21/73038

n=int(input("enter the number of lines: "))
numStars = n
numSpaces = 1
"""
print the pattern of a pyramid
                                   *******
                                    *****
                                     ***
                                      *
"""
for i in range(2*n,0,-1):
    print(" "*numSpaces + "* "*numStars)
    numSpaces +=1
    numStars -=1
