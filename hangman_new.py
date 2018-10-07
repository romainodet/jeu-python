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

import random
import ascii_art_library


#Liste de mots fonctionalité 1
word_list = ["banana", "chapeau", "canapé", "ordinateur", "porte", "lampe", "photo", "soleil", "vert", "evier", "frigo",
             "internet"]

nb_wordchoose = random.randint(0, len(word_list)) - 1
print(nb_wordchoose)
WORD_TO_GUESS=word_list[nb_wordchoose]

nb_lettres=len(WORD_TO_GUESS)

word_display = ""

for i in range(nb_lettres):
    word_display = word_display + "＿"
#debug a supprimer
print(nb_lettres)
print(WORD_TO_GUESS)
print(word_display)
#fin de debug
#Fin de la fonctionalité 1

missed_count = 0
MAX_COUNT = 10
ascii_output = ""
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
"""

print(welcome_message)
print()
print("You have a word with %d letters" % nb_lettres, " :")
print(word_display)


while True:
    a = input("Please enter a letter (something else to quit) :")

    if len(a) != 1 or not a.isalpha():
        print("Bad input, exiting")
        break

    if a in WORD_TO_GUESS:
        print("Well done, ", a,"is in the word !")
        # We need to convert the string to a list (since strings are immutable)
        wd = list(word_display)
        # We iterate over the letter of the word
        for i in range(len(WORD_TO_GUESS)):
            # If the letter is the same as the one just found, we update the wd variable
            if WORD_TO_GUESS[i] == a:
                wd[i] = a

        # This allows to convert the list back to a string
        word_display = "".join(wd)

        if word_display == WORD_TO_GUESS:
            print("YOU WIN !! The word was", WORD_TO_GUESS)
            if missed_count == 0:
                print("Congrats! You find the word in one time!")
            else:
                print("You find the word in", missed_count, "times")
            break

    else:
        print("missed, try again !")
        missed_count += 1

        if missed_count >= MAX_COUNT:
            print(ascii_art_library.ascii_art_hangman(missed_count))
            break

    print("You have", MAX_COUNT - missed_count,"tries left")
    print(ascii_art_library.ascii_art_hangman(missed_count))
    print(word_display)