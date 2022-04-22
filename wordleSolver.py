#!/usr/bin/env python

from wordleHelper import *


if (__name__ == "__main__"):
    with open("5LetterWords.txt", "r") as f:
        valid_words = f.read().split('\n')[0:-1]
        f.close()
    # end with open

    loop = "Y"
    while (loop == "Y"):
        word_guessed = input("Enter the word you guessed: ").upper()

        if (len(word_guessed) != 5):
            raise Exception("Word must be 5 letters long!")
        # end if

        colors = input("Enter the color for each letter separated only by one comma each. " +
                       "Colors should be Yellow, Green or Gray: ").upper().split(',')

        if (len(colors) != 5):
            raise Exception("Make sure to enter 5 colors separated by only one comma each!")
        # end if

        guess = []
        index = 0
        while (index < 5):
            if (colors[index] == "YELLOW" or colors[index] == "GREEN" or colors[index] == "GRAY"):
                guess.append({"letter": word_guessed[index], "color": colors[index]})

                index += 1
            else:
                raise Exception("You entered an invalid color:", colors[index])
            # end if
        # end for

        valid_words, most_popular = check_guess(valid_words, guess)
        display_help(most_popular)

        loop = input("Continue? (Y/N): ").upper()
    # end while
# end if
