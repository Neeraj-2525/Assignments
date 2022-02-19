# Name = Neeraj Kumar
# Roll No. = 21/73038

def count_vowel():
    """
    to count the frequency of vowels in a
    particular string
    :return:
    """
    content = input("enter the content to count vowels: ")
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    data = content.lower()
    for char in data:
        if char in vowels.keys():
            vowels[char] += 1
    print(vowels)

def count_char():
    """
    to count the frequency of characters used in
    a string
    :return:
    """
    content = input("enter the content to count the characters: ")
    character = {}
    data = content.lower()
    for char in data:
        if char not in character.keys():
            character[char] = 1
        else:
            character[char] += 1
    print("Characters count in the string: ")
    print(character)


def main():
    print("Enter 1 to count frequency of variables\nEnter 2 to count frequency of characters")
    choice = int(input("enter your choice: "))
    while choice == 1 or choice == 2:
        if choice == 1:
            count_vowel()
            break

        elif choice == 2:
            count_char()
            break

        else:
            print("invalid choice")
            break


if __name__ == '__main__':
    main()