# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        matches = []
        for word in anagram_list:
            if sorted(self.word) == sorted(word):
                matches.append(word)
        return matches
    
anagram = Anagram('listen')
anagram_list = ['silent', 'enlists', 'google', 'inlets', 'banana']
matches = anagram.match(anagram_list)
print(matches)

anagram = Anagram('acts')
anagram_list = ['cats', 'tacos', 'act', 'acts', 'cast']
matches = anagram.match(anagram_list)
print(matches)
