
def example_a():
    print('\nExample A')
    print('~~~~~~~~~')

    color1 = input("\nWhat's your favourite color?: ")

    color2 = input("\nWhat's your second favourite color?: ")

    # String Join()
    message = 'Your favourite colors are: ' + " ".join([color1, color2])
    message2 = 'Your favourite colors are: ' + " and ".join([color1, color2])

    print(message)
    print(message2)


# Puzzle A - What's your name, baby?
#
# Write a program that asks for your first name.
# Have the program also ask for your second name
# Use join() to create the final sentence "Your full name is {first_name} {second_name}"
# Remember to have spaces between the strings when you join them.
def puzzle_a():
    print('\nPuzzle A')
    print('~~~~~~~~~')


def example_b():
    print('\nExample B')
    print('~~~~~~~~~~~')

    message = "I got married, had a few kids, paid a few bills, retired to Florida and died."
    print(message)

    print(message.replace("bills", "hookers"))


# Puzzle B - You are replaceable
#
# Write a program that asks the user to "Input a sentence with the word "and" in it: ".
# Replace every occurrence of the word "and" with the symbol &
# Remember to escape the backslashes around "and" or use raw string
def puzzle_b():
    print('\nPuzzle B')
    print('~~~~~~~~~~~')


def example_c():
    print('\nExample C')
    print('~~~~~~~~~~~')

    print("Lets join words onto a sentence!: ")

    sentence = input("\n Please enter a sentence: ")

    word1 = input("\n Enter a word: ")

    word2 = input("\n Enter another word: ")

    output = sentence + " " + " ".join([word1, word2])
    print(output)


# Puzzle C – Choose a word to replace
#
# Write a program that asks the user "Please enter a sentence: "
# Then ask the user "Which word will we replace?: "
# Then ask the user "Replace it with what?: "
# Output the original sentence with the word replaced.
# Don't worry if the user enters a word that is not in the sentence, we have not covered loops or error catching yet.
# Just to be clear, the program WILL crash if the user enters a word not in the sentence. That's ok for now.
def puzzle_c():
    print('\nPuzzle C')
    print('~~~~~~~~~~~')


if __name__ == '__main__':

    # Run the puzzles

    example_a()
    # puzzle_a()

    example_b()
    # puzzle_b()

    example_c()
    # puzzle_c()
