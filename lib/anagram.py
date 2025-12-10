class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        matches = []
        for word in anagram_list:
            if sorted(self.word) == sorted(word):
                matches.append(word)
        return matches
