import re


def the_basics():
    """
    Prints basic Python string manipulations using a familiar classic
    """
    hello_message = 'Hello World'
    print("The Classic:")
    print(hello_message)
    new_line()

    print("Length:")
    print(len(hello_message))
    new_line()

    print("Slicing:")
    print(hello_message[:5])
    print(hello_message[6:])
    new_line()

    print("Regex:")
    match_object = re.match(r'(.*)World', hello_message, re.I)
    print(match_object.group())
    new_line()

    print("Reverse Sort via slicing:")
    reversed_message = hello_message[::-1]
    print(reversed_message)
    new_line()

    print("Reverse Sort via reversed join")
    reversed_message_again = ''.join(reversed(reversed_message))
    print(reversed_message_again)
    new_line()

    print("Print the number of 'o's")
    print(hello_message.count('o'))


def new_line():
    print("\n")


the_basics()
