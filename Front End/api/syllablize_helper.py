# API to take input from Puzzle Poems frontend
import sys
from hyphen import Hyphenator
from hyphen.dictools import is_installed, install

language = 'en_US'

def syllablize(poem):
    # syllablizer setup
    if not is_installed(language): install(language)
    hyph = Hyphenator(language)

    # output dict to send back through API
    output = []

    for line in poem:
        # list of words in line
        words = line.split()
        syllablized_line = []

        for word in words:
            syls = hyph.syllables(word)

            new_word = ""

            if len(syls) == 0:
                new_word = word
            else:
                for syl in syls:
                    new_word += syl
                    new_word += " "

            syllablized_line.append(new_word.strip())

        if len(syllablized_line) > 0:
            output.append(syllablized_line)

    return output
