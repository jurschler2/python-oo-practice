"""Word Finder: finds random words from a dictionary.

    >>> words = WordFinder("text.txt")
    5 words read

"""


from random import choice


class WordFinder:
    """Takes in a word document and immediately returns the count
    of words (1 word per line).

    open_file() launches on __init__ and populates words list

    random() will return a random word from the text file.
    """

    def __init__(self, file):
        "launches open_file method to populate words list"
        self.file = file
        self.words = []
        self.open_file()

    def __repr__(self):
        return f"<WordFinder - words = {self.words}>"

    def open_file(self):
        "opens file, fills words list with each word, prints total"
        file_opened = open(self.file, "r")  # place in init
        for line in file_opened:
            self.words.append(line.rstrip("\n"))
        print(f"{len(self.words)} words read")

    def random(self):
        "imports random module for choice(), returns random word"

        return choice(self.words)


words = WordFinder("text.txt")
