poem = """February. Get ink. Weep.
Write the heart out about it. Sing
Another song of February
While raucous slush burns black with spring. """


def lines_printed_backwards():
    # TODO: reverse the list
    lines_list = poem.splitlines()
    lines_list.reverse()
    # print(lines_list)
    # TODO: Print items from list
    print(poem + "\n")
    print("-------------------\n")
    print(*lines_list, sep="\n")


def lines_printed_random():
    pass


def my_custom_function():
    pass


"""TODO: Stretch challanges 
Modify your program to read the poem from a file
Modify your program to read the poem from user input
Modify your program to randomly rearrange the words on each line"""


def test_poem():
    # TODO: test code here
    pass


lines_printed_backwards()
