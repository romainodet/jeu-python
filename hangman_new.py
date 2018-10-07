"""
                 /
    |      /  |////:  o////  ./////    s`      y////-
    |         |       /      s-    s.  h`      h
    |         |////.  /      s-    s-  h`      d////`
    |         |       /      s-    s.  h`      h
    |////     |////:  o/::/  -o/::/o   y////.  d////-

        -mmmmm.   ymmmmmmmmmy-   ymmmm-       -ymmmmmmmo
        -mmmmm.   ymmmm+ohmmmm-  ymmmm-     :mmmmdo/+s+
        -mmmmm.   ymmm     hmmmo ymmmm-    hmmmm:
        -mmmmm:   hmmm     mmmm/ ymmmm/    ymmmmy:
        -mmmmmmmmmmmmmmmmmmmms   ymmmmmmmm  dommmmmmmmo
        -hhhhhhhhhhhhhhhhys+/    shhhhhhhhy  ./shddhh/
        
     file :hangman_new.py
     By: romain.odet <romain.odet@lecole-ldlc.com>           
     Created: 06/10/2018 12:11 by Romain ODET  
"""
# Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
# Licence : GPL

import random  # importing the library for random numbers
import ascii_art_library  # importing the file with the function for the ascii art.

# Functionalty start
word_list = ["banana", "chapeau", "canapé", "ordinateur", "porte", "lampe", "photo", "soleil", "vert", "evier", "frigo",
             "internet"]  # list of the word

nb_wordchoose = random.randint(0, len(word_list)) - 1  # Choose a word in the list with it numbers in the list

WORD_TO_GUESS = word_list[nb_wordchoose]  # take the random word

nb_lettres = len(WORD_TO_GUESS)  # have the number of letters

word_display = ""  # init the var word display

for i in range(nb_lettres):  # display underscores in function of the number of letters in the random word choose
    word_display = word_display + "＿"
# end of the additional functionalitie

missed_count = 0  # init the var of missed answer
MAX_COUNT = 10  # init the var of maximum errors
welcome_message = """
  _    _                                                                            
 | |  | |                                                                           
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __ _  __ _ _ __ ___   ___       
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   / _` |/ _` | '_ ` _ \ / _ \      
 | |  | | (_| | | | | (_| | | | | | | (_| | | | | | (_| | (_| | | | | | |  __/_ _ _ 
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \__, |\__,_|_| |_|_|_|\___(_|_|_)
                      __/ |  | | | |                __/ |           | |             
   __ _ _   _  ___  _|___/_  | |_| |__   ___  __   |___/___  _ __ __| |             
  / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ \ \ /\ / / _ \| '__/ _` |             
 | (_| | |_| |  __/\__ \__ \ | |_| | | |  __/  \ V  V / (_) | | | (_| |_            
  \__, |\__,_|\___||___/___/  \__|_| |_|\___|   \_/\_/ \___/|_|  \__,_(_)           
   __/ |                                                                            
  |___/                                                                             
"""  # init the var with the welcome message

print(welcome_message)  # display the welcome message
print()  # print a carriage return
print("You have a word with %d letters" % nb_lettres, " :")  # indicates how much letters there is in a word
print(word_display)  # print the underscores for the word


while True:
    a = input("Please enter a letter (something else to quit) :")  # user type a letter

    if a == "score":  # if user type score, print the actual errors he makes
        print("You have", MAX_COUNT - missed_count, "tries left")
        print(ascii_art_library.ascii_art_hangman(missed_count))
    else:
        if len(a) != 1 or not a.isalpha():  # if it's not only one letter ASCII
            print("Bad input, exiting")  # print the message bad input
            break  # Quit the program

        if a in WORD_TO_GUESS:  # if the letter is in the word to guess
            print("Well done, ", a, "is in the word !")
            # We need to convert the string to a list (since strings are immutable)
            wd = list(word_display)
            # We iterate over the letter of the word
            for i in range(len(WORD_TO_GUESS)):
                # If the letter is the same as the one just found, we update the wd variable
                if WORD_TO_GUESS[i] == a:
                    wd[i] = a

            # This allows to convert the list back to a string
            word_display = "".join(wd)

            if word_display == WORD_TO_GUESS:  # if the word wich is display is the same of the word display
                print("YOU WIN !! The word was", WORD_TO_GUESS)  # say the player he win.
                if missed_count == 0:  # if he find the word in one time
                    print("Congrats! You find the word in one time!")  # congrats the plater
                else:  # else inform the number of error he made
                    print("You find the word in", missed_count, "times")
                    print(ascii_art_library.ascii_art_hangman(missed_count))  # print the ascii art of the hangman
                break

        else:  # if the letter the user type is not in the word
            print("missed, try again !")  # inform the user he missed
            missed_count += 1  # add one to the counter of the letter

            if missed_count >= MAX_COUNT:  # if the counter of error is equal of the max error the user can make
                print(ascii_art_library.ascii_art_hangman(
                    missed_count))  # displat the ascii art of the hangman of the loose
                break

        print("You have", MAX_COUNT - missed_count, "tries left")  # display the number of errors
        print(ascii_art_library.ascii_art_hangman(missed_count))  # display the ascii art of the number of missed count
        print(word_display)  # display the word the player find
