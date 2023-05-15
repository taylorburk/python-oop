"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, location):
        self.location = location
        self.get_file()
    
    def get_file(self):
        with open(self.location, "r") as file:
            allText = file.read()
            self.words = list(map(str, allText.split()))
            len_file = len(self.words)
            print(f"{len_file} words read")
            

    def random(self):
        print(random.choice(self.words))

class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
