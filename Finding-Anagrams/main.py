# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = set([i for i in first_word])
    anagram = set([i for i in second_word])
    if word == anagram:
        print(True)
    else:
        print(False)
first_word = input("Write the first word: ")
second_word = input("Write it's anagram: ")


find_anagram(first_word, second_word)