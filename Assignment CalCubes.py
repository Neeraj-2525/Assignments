# Name = Neeraj Kumar
# Roll No. = 21/73038

def cube():
    """
    to count cubes of integers
    1,2,3,4,5
    :return:
    """
    cubes = {}
    for i in range(1, 5+1):
        cubes[i] = i**3

    print(cubes)

if __name__ == '__main__':
    cube()

# cubes = {i:i**3 for i in range(1,6)}
# print(cubes)