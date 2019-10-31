import random

poem = """February. Get ink. Weep.
Write the heart out about it. Sing
Another song of February
While raucous slush burns black with spring. """

# Open file
f = open("february.txt", "r")
# Get list of all lines in file
file_poem = f.readlines()
# Close file
f.close()


def lines_printed_backwards():
    # TODO: reverse the list
    lines_list = poem.splitlines()
    lines_list.reverse()
    # print(lines_list)
    # TODO: Print items from list
    print(poem + "\n")
    print("-------------------\n")
    print(*lines_list, sep="\n")


def file_lines_printed_backwards():
    lines_list = file_poem
    lines_list.reverse()
    # print("-------------------\n")
    print(*lines_list)


def lines_printed_random():
    lines_list = poem.splitlines()
    # for i in range(len(lines_list)):
    #     random_line = random.randrange(len(lines_list))
    #     print(lines_list[random_line])
    # this method of randomizing the lines has a chance to and often does return the same line multiple times
    random.shuffle(lines_list)
    print(*lines_list, sep="\n")


def my_custom_function():
    pass


"""TODO: Stretch challanges 
Modify your program to read the poem from a file
Modify your program to read the poem from user input
Modify your program to randomly rearrange the words on each line"""


def test_poem():
    # TODO: test code here
    pass


file_lines_printed_backwards()
