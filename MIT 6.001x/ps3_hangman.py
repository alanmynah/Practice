# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
    guessedList = []
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedList.append(letter)
        else:
            guessedList.append("_")
    if "".join(guessedList) == secretWord:
        return True
    else:
        return False
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    myList = list(lettersGuessed)
    guessedList = []
    for letter in secretWord:
        if letter in myList:
            guessedList.append(letter)
        else:
            guessedList.append("_")
    return " ".join(guessedList)
       
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    emptyList = []
    import string 
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            emptyList.append(letter)
    return "".join(emptyList)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #New empty list for guessed letters
    lettersGuessed = []
   
    #Set mistakes counter
    guessesLeft = 8
    
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is %i letters long" % len(secretWord))
    
    #Set hangman condition with 8 mistakes max
    while isWordGuessed(secretWord, lettersGuessed) != True and guessesLeft > 0: 
        
        print ("-" * 11)
        print ("You have %i guesses left" % guessesLeft)
        #Ask for input
        print ("Available letters: " + getAvailableLetters(lettersGuessed)) 
        letter = input("Please guess a letter: ")
    
        #Add the letter to the guessed list if it wasn't guessed before
        if letter not in lettersGuessed:
            lettersGuessed.append(letter)
            #Check if the user guessed the letter correctly
            if letter in secretWord:
                print ("Good guess: " + 
                       getGuessedWord(secretWord, lettersGuessed))
                  
            #Else increase mistakes by one
            else:
                print ("Oops! That letter is not in my word: " + 
                       getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1
            #If it was guessed, ask to try another lette
        else:
            print ("Oops! you've already guessed that letter: " + 
                   getGuessedWord(secretWord, lettersGuessed))
            
            
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print ("-" * 11)
        print ("Congratulations you won!")
        
    #Inform user they've been hanged
    if guessesLeft == 0:
        print ("-" * 11)
        print ("Sorry, you've run out of guesses. The word was " + secretWord)
       
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

