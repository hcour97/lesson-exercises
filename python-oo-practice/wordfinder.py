'''Word Finder: finds random words from a dictionary'''
import random


class WordFinder():
    '''class for finding random words from a given dictionary

     >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    '''

    def __init__(self, path):
        '''reads file and reports how many items read'''
        word_file = open(path)

        self.words = self.parse(word_file)

        print(f"{len(self.words)} words read")
        # print(self.words)
    
    def parse(self, word_file):
        '''turns the file into a list of words'''

        return [word.strip() for word in word_file]
        
    def random(self):
        '''picks a random word'''
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    def parse(self, word_file):
        '''parses the lists of words, ignoring '#' and blank spaces'''
        # for word in word_file:
        #     if word.strip() and not word.startswith("#"):
        #         return word.strip()
        return [word.strip() for word in word_file if word.strip() and not word.startswith("#")]
    