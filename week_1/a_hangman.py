'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
import random

def print_header():

    print("**********************************************")
    print("******* Welcome to the Hangman Game! *********")
    print("************** HA HA HA HA!! *****************")
    print("**********************************************")

def choose_word():
    
    dictio = ['tree', 'banana', 'future', 'inteligence', 'artificial', 'wisdom', 'dictionary']
    word = dictio[random.randrange(len(dictio))]
    print("Here we go!! The secret word has {} letters!".format(len(word)))
    print("Descubra a palavra antes que voce seja enforcado!")
    temp = ["_" for l in word]
    print(temp)    

    return word, temp

def guess(secret_word, word, error):

    shot = input("Choose a letter: ").strip()
    index = 1
    no_exist = True

    for letter in secret_word:
        if (shot.lower() == letter):
            print("Yeah!! The letter '{}' is in the position {}".format(shot, index))
            word[index-1] = shot
            no_exist = False
        elif (no_exist and index == len(secret_word)):
            print("Oh No! The there isn't the letter '{}' in the word!".format(shot))
            error += 1

        index += 1
    
    return word, error

def response(word, temporary_word, error):
    itsright = False
    itshanged = False
    
    if ("_" in temporary_word):
        if (error < 6):
            i_know = input("Do you already know the answer? (y/n): ").lower().strip()
        else:
            i_know = "y"

        if (i_know == "y"):
            shot = input("What is the word?: ").lower()
            if (shot == word):
                winner()
                print("Congratulations!! You're right!")
                itsright = True
            else:
                error += 1
    else:
        winner()
        print("Congratulations! You're right!")
        itsright = True
   
    if (error > 6 and itsright == False):
        print("Oh no! You were hanged!")
        print("The secret word was '{}'!".format(word))
        hanged()
        itshanged = True
    elif (itsright == False):
            gibbet(error)
            print("You have {} chances!".format((6-error)))
    
    return itsright, itshanged, error

def gibbet(erros):
    
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def hanged():

    print("  ___________________    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXX       XXX   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \___________/       ")

def winner():
    print()
    print("    ___________  ")
    print("   '._==_==_=_.' ")
    print("   .-\\:      /-.")
    print("  | (|:.     |) |")
    print("   '-|:.     |-' ")
    print("    \\::.    /   ")
    print("      '::. .'    ")
    print("        ) (      ")
    print("      _.' '._    ")
    print("     '-------'   ")
    
def play():

    print_header()
    secret_word, temporary_word = choose_word()
    error = 0
    itshanged = False
    itsright = False

    while (not itsright and not itshanged) :  
        
        temporary_word, error = guess(secret_word, temporary_word, error)
        print(temporary_word)
        itsright, itshanged, error = response(secret_word, temporary_word, error)
      
    print("Hangman Game is ended")

    answer = input("Do you wanna play again? (y/n): ").lower().strip()
    if (answer == "y"):
        play()




if (__name__ == "__main__"):
    play()