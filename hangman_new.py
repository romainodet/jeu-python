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


def display_list(name_of_the_list, sep):
    i = 0
    while i < (len(name_of_the_list)):
        print(name_of_the_list[i], end=sep)
        i += 1
    return 0


# this function permit to show the ascii art with the number of try.
def ascii_art_hangman(num):
    if num == 0:  # No try
        ascii_output = "Well done, you don't have make mistakes."
    elif num == 1:  # 1st try Ascii ART
        ascii_output = """
                    1st try...
==================================="""
    elif num == 2:  # 2d try
        ascii_output = """
          /  \\
         //  \\\\     2d try...
==================================="""
    elif num == 3:  # 3rd try
        ascii_output = """
           ||
           ||
           ||
           ||
           ||
           ||
          /||\\
         //||\\\\     3rd try...
==================================="""
    elif num == 4:  # 4th try
        ascii_output = """
           ||  /
           || /
           ||/
           ||
           ||
           ||
          /||\\
         //||\\\\     4th try...
==================================="""
    elif num == 5:  # 5th try
        ascii_output = """
           ,==============
           ||  /
           || /
           ||/
           ||
           ||
           ||
          /||\\
         //||\\\\     5th try...
==================================="""
    elif num == 6:  # 6th try
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/
           ||
           ||
           ||
          /||\\
         //||\\\\     6th try...
==================================="""
    elif num == 7:  # 7th try
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/        O
           ||         |
           ||         |
           ||
          /||\\
         //||\\\\     7th try...
==================================="""
    elif num == 8:  # 8th try
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/        O
           ||        /|\\
           ||         |
           ||
          /||\\
         //||\\\\     8th try...
==================================="""
    elif num == 9:  # 9th try
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/        O
           ||        /|\\
           ||        /|\\
           ||
          /||\\
         //||\\\\     9th try and the last...
==================================="""
    elif num == 10:  # 10th try
        ascii_output = """
                     _
                    | |
 _   _  ___  _   _  | | ___   ___  ___  ___
| | | |/ _ \| | | | | |/ _ \ / _ \/ __|/ _ \\
| |_| | (_) | |_| | | | (_) | (_) \__ \  __/_ _ _
 \__, |\___/ \__,_| |_|\___/ \___/|___/\___(_|_|_)
  __/ |
 |___/
           ,==========Y===
           ||  /      |
           || /       |
           ||/
           ||
           ||
           ||
          /||\ 
         //||\\\\    o-|-<
==================================="""
    else:  # other cases exit the program.
        exit(404)
    cr = """

    """  # Carriage return for the output
    return (cr + ascii_output + cr)  # output to the program with a carriage before and after the ascii output


# End of the function

print("""

        .__       .__                                       
  _____ |__| ____ |__|    _________    _____   ____   ______
 /     \|  |/    \|  |   / ___\__  \  /     \_/ __ \ /  ___/
|  Y Y  \  |   |  \  |  / /_/  > __ \|  Y Y  \  ___/ \___ \ 
|__|_|  /__|___|  /__|  \___  (____  /__|_|  /\___  >____  >
      \/        \/     /_____/     \/      \/     \/     \/ 

 _        ___  _          _ _                                                                
/ | ___  |_ _|| |_  ___  | | | ___ ._ _  ___ ._ _ _  ___ ._ _                                
| ||___|  | | | . |/ ._> |   |<_> || ' |/ . || ' ' |<_> || ' |                               
|_|       |_| |_|_|\___. |_|_|<___||_|_|\_. ||_|_|_|<___||_|_|                               
                                        <___'                                                
 ___       ___                        _    _                           _                     
<_  >___  /  _>  _ _  ___  ___ ___  _| |_ | |_  ___  ._ _  _ _ ._ _ _ | |_  ___  _ _         
 / /|___| | <_/\| | |/ ._><_-<<_-<   | |  | . |/ ._> | ' || | || ' ' || . \/ ._>| '_>_  _  _ 
<___>     `____/`___|\___./__//__/   |_|  |_|_|\___. |_|_|`___||_|_|_||___/\___.|_| <_><_><_>
                                                                                            
""")
y = int(input("Choisisez votre jeux : "))

if y == 1:
    # Functionalty start
    word_list = ["banana", "chapeau", "canapé", "ordinateur", "porte", "lampe", "photo", "soleil", "vert", "evier",
                 "frigo",
                 "internet"]  # list of the word

    nb_wordchoose = random.randint(0, len(word_list)) - 1  # Choose a word in the list with it numbers in the list

    WORD_TO_GUESS = word_list[nb_wordchoose]  # take the random word

    nb_lettres = len(WORD_TO_GUESS)  # have the number of letters

    word_display = ""  # init the var word display

    missed_letters = []

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
            print(ascii_art_hangman(missed_count))
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
                        print(ascii_art_hangman(missed_count))  # print the ascii art of the hangman
                    break

            else:  # if the letter the user type is not in the word
                print("missed, try again !")  # inform the user he missed
                missed_count += 1  # add one to the counter of the letter
                missed_letters.append(a)
                print("You try those letters : ")
                display_list(missed_letters, ", ")
                print("")
                if missed_count >= MAX_COUNT:  # if the counter of error is equal of the max error the user can make
                    print(ascii_art_hangman(missed_count))  # display the ascii art of the hangman of the loose

            print("You have", MAX_COUNT - missed_count, "tries left")  # display the number of errors
            print(ascii_art_hangman(missed_count))  # display the ascii art of the number of missed count
            print(word_display)  # display the word the player find
elif y == 2:
    # Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
    # Licence : GPL

    # Import the randint function from the random module
    from random import randint

    max_num = int(input("Entrez le nombre maximum à deviner : "))
    number = randint(1, max_num)
    nb_trials = 0

    print('Welcome, try to guess my secret number between 1 and ', end="")
    print(max_num)

    while True:
        user_number = int(input('Your guess ?'))
        nb_trials = nb_trials + 1
        if user_number == number:
            # user won !
            print("YOU WIN, Congratulations")
            print("It took you %s trials" % nb_trials)
            break
        elif user_number < number:
            print("too small !")
        elif user_number > number:
            print("too big !")
else:
    print("Error. Exiting...")
