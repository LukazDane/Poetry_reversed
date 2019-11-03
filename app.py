import random
import re

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


def lines_printed_backwards_class():
    lines_list = poem.split("\n")
    i = 1
    for line in lines_list:
        print(str(i) + " " + line)
        i = i+1
    print("-------------------\n")
    i = len(lines_list)
    lines_list.reverse()
    for line in lines_list:
        print(str(i) + " " + line)
        i = i-1


def file_lines_printed_backwards():
    lines_list = file_poem
    lines_list.reverse()
    print(*lines_list)


def lines_printed_random():
    lines_list = poem.splitlines()
    # for i in range(len(lines_list)):
    #     random_line = random.randrange(len(lines_list))
    #     print(lines_list[random_line])
    # this method of randomizing the lines has a chance to and often does return the same line multiple times
    random.shuffle(lines_list)
    print(*lines_list, sep="\n")


def file_lines_printed_random():
    lines_list = file_poem
    random.shuffle(lines_list)
    print(*lines_list)


def sollux_quirkify():
    """I'm going to chain some dot functins here. I know it looks crazy, and bad practice, but I've checked with engineers MUCH better than me, and short of doing a thing i don't know how to do, this is how it was suggested to me. It's also faster than the other suggested methods. """
    quirk = poem.replace("s", "2").replace("S", "2").replace(
        "i", "ii").replace("to", "two").replace("too", "two")
    lines_list = quirk.splitlines()
    print(*lines_list, sep="\n")


def file_sollux_quirkify():
    quirk = file_poem
    for i in range(len(quirk)):
        print(str(quirk[i]).replace("s", "2").replace("S", "2").replace(
            "i", "ii").replace("to", "two").replace("too", "two").replace("\n", ""))
    # lines_list = quirk

    # print(*lines_list)


"""TODO: Stretch challanges 
Modify your program to read the poem from a file ✔
Modify your program to read the poem from user input
Modify your program to randomly rearrange the words on each line
"""


def test_poem():
    # TODO: test code here
    pass


def choice():
    print("""
    Choices:
    1 - Print poem backwards
    2 - Print poem backwards: numbered
    3 - print poem from file backwards
    4 - print poem random
    5 - print poem from file random
    6 - Quirkify poem
    7 - Quirkify poem from file
    """)
    prompt = input("Choice: ")

    if prompt == "1":
        lines_printed_backwards()
    elif prompt == "2":
        lines_printed_backwards_class()
    elif prompt == "3":
        file_lines_printed_backwards()
    elif prompt == "4":
        lines_printed_random()
    elif prompt == "5":
        file_lines_printed_random()
    elif prompt == "6":
        sollux_quirkify()
    elif prompt == "7":
        file_sollux_quirkify()
    else:
        print("that doesn't appear to be one of the choice...")
    choice()


choice()
