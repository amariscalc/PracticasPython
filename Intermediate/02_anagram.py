# Anagram
'''
An anagram is a word or phrase formed by changing the order of the letters in another word or phrase.
'''

# A function that check if two words are same
def same_word (word_a, word_b):
    if word_a == word_b:
        return True
    else:
        return False

# A function that check if it´s a anagram
def is_anagram (word_a,word_b):
    pass

# main ()
word_a = input ("Enter the first word: ")
word_b = input ("Enter the second word: ")

# Check if the first and second word is the same
if same_word (word_a.lower(),word_b.lower()):
    print ("%s is not a anagram of %s."%(word_b,word_a))
else:
    # check if word_b is a anagram of word_a
    if is_anagram (word_a.lower(),word_b.lower()):
        print ("%s is a anagram of %s."%(word_b,word_a))
    else:
        print ("%s is not a anagram of %s."%(word_b,word_a))