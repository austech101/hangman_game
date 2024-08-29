import random
from randomwords import rndm_words
# print(rndm_words)

def valid_word(rndm_words):
    word = random.choice(rndm_words) #randomly choose a word from the randomwords list
    while "-" in word or " " in word:
        word = random.choice(rndm_words) # We get a word that doesn't have a dash or space in it when it stops iterating
    return word
# we need to be able to keep track of which letters we've guessed and which letters in the word, we've correctly guessed
# We need a way to keep track of what is a valid letter and what it is

import string
def hangman():
    word = valid_word(rndm_words)#Keep track of what's already been guessed
    word_letters = set(word) # get letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #track what's been guessed

    while len(word_letters) > 0:
        #The letters used
        print("Letters used are: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Enter a Letter: ").upper()
        print(user_letter)    
        if used_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if used_letters in word_letters:        
                word_letters.remove(user_letter)     

        elif user_letter in used_letters:
         print("Word already guessed. Try again.")
        else:
            print("Invalid Character. Please try again.")
# We loop to keep the user guessing until the right word is guessed



    
        

 
