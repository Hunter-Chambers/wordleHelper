#!/usr/bin/env python


VALID_WORDS = ["ABUSE", "ADULT", "AGENT", "ANGER", "APPLE", "AWARD",
               "BASIS", "BEACH", "BIRTH", "BLOCK", "BLOOD", "BOARD",
               "BRAIN", "BREAD", "BREAK", "BROWN", "BUYER", "CAUSE",
               "CHAIN", "CHAIR", "CHEST", "CHIEF", "CHILD", "CHINA",
               "CLAIM", "CLASS", "CLOCK", "COACH", "COAST", "COURT",
               "COVER", "CREAM", "CRIME", "CROSS", "CROWD", "CROWN",
               "CYCLE", "DANCE", "DEATH", "DEPTH", "DOUBT", "DRAFT",
               "DRAMA", "DREAM", "DRESS", "DRINK", "DRIVE", "EARTH",
               "ENEMY", "ENTRY", "ERROR", "EVENT", "FAITH", "FAULT",
               "FIELD", "FIGHT", "FINAL", "FLOOR", "FOCUS", "FORCE",
               "FRAME", "FRANK", "FRONT", "FRUIT", "GLASS", "GRANT",
               "GRASS", "GREEN", "GROUP", "GUIDE", "HEART", "HENRY",
               "HORSE", "HOTEL", "HOUSE", "IMAGE", "INDEX", "INPUT",
               "ISSUE", "JAPAN", "JONES", "JUDGE", "KNIFE", "LAURA",
               "LAYER", "LEVEL", "LEWIS", "LIGHT", "LIMIT", "LUNCH",
               "MAJOR", "MARCH", "MATCH", "METAL", "MODEL", "MONEY",
               "MONTH", "MOTOR", "MOUTH", "MUSIC", "NIGHT", "NOISE",
               "NORTH", "NOVEL", "NURSE", "OFFER", "ORDER", "OTHER",
               "OWNER", "PANEL", "PAPER", "PARTY", "PEACE", "PETER",
               "PHASE", "PHONE", "PIECE", "PILOT", "PITCH", "PLACE",
               "PLANE", "PLANT", "PLATE", "POINT", "POUND", "POWER",
               "PRESS", "PRICE", "PRIDE", "PRIZE", "PROOF", "QUEEN",
               "RADIO", "RANGE", "RATIO", "REPLY", "RIGHT", "RIVER",
               "ROUND", "ROUTE", "RUGBY", "SCALE", "SCENE", "SCOPE",
               "SCORE", "SENSE", "SHAPE", "SHARE", "SHEEP", "SHEET",
               "SHIFT", "SHIRT", "SHOCK", "SIGHT", "SIMON", "SKILL",
               "SLEEP", "SMILE", "SMITH", "SMOKE", "SOUND", "SOUTH",
               "SPACE", "SPEED", "SPITE", "SPORT", "SQUAD", "STAFF",
               "STAGE", "START", "STATE", "STEAM", "STEEL", "STOCK",
               "STONE", "STORE", "STUDY", "STUFF", "STYLE", "SUGAR",
               "TABLE", "TASTE", "TERRY", "THEME", "THING", "TITLE",
               "TOTAL", "TOUCH", "TOWER", "TRACK", "TRADE", "TRAIN",
               "TREND", "TRIAL", "TRUST", "TRUTH", "UNCLE", "UNION",
               "UNITY", "VALUE", "VIDEO", "VISIT", "VOICE", "WASTE",
               "WATCH", "WATER", "WHILE", "WHITE", "WHOLE", "WOMAN",
               "WORLD", "YOUTH"]


def check_guess(guess: list, current_filter: list = None) -> (list, dict):
    '''
    Finds which words are still possible based
    on the guess. Also finds which letters are
    the most common in each position in the
    words that are still valid.

    Precondition: 'guess' must represent the guess that
                  was made. Format should be as follows:
                  [{"letter": '<character>', "color": "<Color>"},...]

    Returns: A list that holds all of the words that are still valid
             and a dictionary that shows which letters are the most
             common in each position in the words that are still valid
    '''

    # check if a list of pre-filtered words was passed in
    if (current_filter):
        words = current_filter
    else:
        words = VALID_WORDS
    # end if

    position = 0

    # filter out words based on character color
    for letter in guess:
        # filter out words that have the 'Gray' letter
        if (letter["color"] == "Gray"):
            words = list(filter(lambda word: not letter["letter"] in word, words))
        # filter out words that do not have the 'Green' letter in the correct position
        elif (letter["color"] == "Green"):
            words = list(filter(lambda word: letter["letter"] == word[position], words))
        # filter out words that do not have the 'Yellow' letter
        else:
            words = list(filter(lambda word: letter["letter"] in word, words))
        # end if

        position += 1
    # end for

    counts = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}

    # this loop will count how many times each letter appears
    # in each position in the currently valid words
    for word in words:
        position = 0

        for letter in word:
            if (letter in counts[position]):
                counts[position][letter] += 1
            else:
                counts[position][letter] = 1
            # end if

            position += 1
        # end for
    # end for

    most_popular = find_max(counts)

    return (words, most_popular)
# end check_guess

def find_max(counts: dict) -> dict:
    '''
    Returns the letter with the highest count
    in each position in 'counts'. If multiple
    letters in the same position have the same
    count, then all letters with that count
    are returned.

    Precondition: 'counts' is a dictionary that has its keys
                  as the character positions in a word, and
                  the values are dictionaries that represent
                  how many times a letter has appeared in that
                  position. Format should be as follows:
                  {0: {'<character>': <count>,...},...}

    Returns: A dictionary whose keys are character positions
             in a word, and the values are lists of the
             character(s) that had the highest count
    '''

    most_popular = {}
    position_counter = 1

    for position in counts:
        highest = 0
        answer = []

        for letter in counts[position]:
            if (counts[position][letter] > highest):
                highest = counts[position][letter]
                answer = [letter]
            else:
                answer += letter
            # end if
        # end for

        most_popular[position_counter] = answer
        position_counter += 1
    # end for

    return most_popular
#end find_max

def display_help(most_popular: dict) -> None:
    '''
    A simple helper function
    '''

    print("Most popular letters in each position:")

    for position in most_popular:
        print(str(position) + ":", most_popular[position])
    # end for
# end display_help

if (__name__ == "__main__"):
    print("This is a simulation of a simplified",
          "version of the popular game 'Wordle'.")
    print("In this simulation, only a small set of",
          len(VALID_WORDS), "words are possible to guess.")
    input("The correct word to guess is 'ROUTE'.\n" +
          "Press 'Enter' to see the simulation...")

    print('-'*30)
    print("Guess 1 - BREAD")
    filtered_words, most_popular = check_guess([{"letter": 'B', "color": "Gray"},
                                                {"letter": 'R', "color": "Yellow"},
                                                {"letter": 'E', "color": "Yellow"},
                                                {"letter": 'A', "color": "Gray"},
                                                {"letter": 'D', "color": "Gray"}])
    display_help(most_popular)

    input("Press 'Enter' to continue...")

    print('-'*30)
    print("Guess 2 - PORER")
    filtered_words, most_popular = check_guess([{"letter": 'P', "color": "Gray"},
                                                {"letter": 'O', "color": "Green"},
                                                {"letter": 'R', "color": "Yellow"},
                                                {"letter": 'E', "color": "Yellow"},
                                                {"letter": 'R', "color": "Yellow"}],
                                                filtered_words)
    display_help(most_popular)

    input("Press 'Enter' to continue...")

    print('-'*30)
    print("Guess 3 - CORSE")
    filtered_words, most_popular = check_guess([{"letter": 'C', "color": "Gray"},
                                                {"letter": 'O', "color": "Green"},
                                                {"letter": 'R', "color": "Yellow"},
                                                {"letter": 'S', "color": "Gray"},
                                                {"letter": 'E', "color": "Green"}],
                                                filtered_words)
    display_help(most_popular)
# end if
