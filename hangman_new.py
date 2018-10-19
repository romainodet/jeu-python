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
# Author : Antoine Scherrer <antoine.scherrer@lecole-ldlc.com>
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
        ascii_output = "Bien joué ! Aucune faute."
    elif num == 1:  # 1st try Ascii ART
        ascii_output = """
                    1er essai...
==================================="""
    elif num == 2:  # 2d try
        ascii_output = """
          /  \\
         //  \\\\     2ème essai...
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
         //||\\\\     3ème essai...
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
         //||\\\\     4ème essai...
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
         //||\\\\     5ème essai...
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
         //||\\\\     6ème essai...
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
         //||\\\\     7ème essai...
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
         //||\\\\     8ème essai...
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
         //||\\\\     9ème et dernier essai...
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
def menu():
    name_player_bouffe = ["Tartiflette", "Raclette", "Fondue", "Mimolette", "Cantal", "Brie", "Compte",
                          "Gratin dauphinois", "Choucroute", "Aligot", "Couscous", "Nems", "Sushi", "Paëlla", "Crêpes"]
    name_player_medics = ["Doliprane", "Smecta", "Spasfon", "Stodal", "Toplexil", "Drill", "Lisopaine", "Antibiotique",
                          "Ultra levure", "Antadys", "NasoNex", "Ibuprofène", "Lamaline"]
    name_player_voiture = ["Multipla", "Mauricette la modus", "AMG", "TT", "C4", "Mégane", "Clio", "206", "Duster",
                           "Logan", "Twingo", "2CV"]
    name_player_animaux = ["Cochon", "Dinde", "Cochon dinde", "Dindon", "Oie", "Biquette", "Ornithrynque", "Opposum",
                           "Onyx", "Dodo", "Kiwi", "Chihuahua", "Rat", "Taupe", "Rat-Taupe", "Dragon du comodo",
                           "Loch Ness", "Ver de terre", "Tatou Rose"]
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
    hasard = input("Souhaitez vous un nom issu des plus grandes recherches de nom ? Répondez par oui ou non : ").lower()

    if hasard == "oui":
        nom_cat_choix = input(
            "Quel de type de nom souhaitez vous ? Tapez : voiture, animaux, bouffe, medicament : ").lower()

        if nom_cat_choix == "voiture":
            nom_choix = random.choice(name_player_voiture)

        elif nom_cat_choix == "animaux":
            nom_choix = random.choice(name_player_animaux)

        elif nom_cat_choix == "bouffe":
            nom_choix = random.choice(name_player_bouffe)

        elif nom_cat_choix == "medicament":
            nom_choix = random.choice(name_player_medics)

    elif hasard == "non":
        nom_choix = input("Quel nom souhaitez vous avoir ? :")
    else:
        nom_choix = "Gros débile qui sait pas tapez"

    if y == 1:
        hangman(nom_choix)

    elif y == 2:
        guess_my_number(nom_choix)

    else:
        exit("ERROR : NO CHOICE MADE")


def hangman(nom):
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
    print(
        "Salut %s, j'espère que tout va bien car aujourd'hui tu travaille pour Mr Robespierre. Tu doit pendre une personne. " % nom)
    print(
        "Cependant un complice peut t'aider à sauver la personne pendu qui est aussi ton meilleur ami. Pour cela tu doit deviner son mot en moins de 9 tentatives.")
    print("""

 _____ ____  ____  ____    _     _     ____  _  __
/  __//  _ \/  _ \/  _ \  / \   / \ /\/   _\/ |/ /
| |  _| / \|| / \|| | \|  | |   | | |||  /  |   / 
| |_//| \_/|| \_/|| |_/|  | |_/\| \_/||  \_ |   \ 
\____\\\\____/\____/\____/  \____/\____/\____/\_|\_\\
                                                  


""")
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

    print()  # print a carriage return
    print(nom, "tu as un mot avec %d lettres...." % nb_lettres, " :")  # indicates how much letters there is in a word
    print(word_display)  # print the underscores for the word

    while True:
        print("Si tu ne sait plus ton score tape score, si tu veux savoir quelle lettres tu as déjà essayé tape lettre")
        a = input(
            "Rentre la lettre que tu pense être dans le mot, si tu préfère tué ton ami tapes autre choses qu'une lettre :").lower()  # user type a letter

        if a == "score":  # if user type score, print the actual errors he makes
            print(nom, " Il te reste ", MAX_COUNT - missed_count, "essai avant la mort de ton ami...")
            print(ascii_art_hangman(missed_count))
        elif a == "lettre":
            print("Tu as essayé les lettres suivantes : ")
            display_list(missed_letters, ", ")
            print("")
        else:
            if len(a) != 1 or not a.isalpha():  # if it's not only one letter ASCII
                print(nom,
                      "tu viens de tapez autre chose qu'une lettre. Robespierre vous a repéré. Vous venez de vous tuer et de tuer votre ami. Adieu.")  # print the message bad input
                exit("Vous êtes mort... Game OVER")  # Quit the program

            if a in WORD_TO_GUESS:  # if the letter is in the word to guess
                print("Bravo", nom, ",", a, "est dans le mot!")
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
                    print("Bravo", nom, "!! le mot est bien", WORD_TO_GUESS,
                          ", tu viens de sauver ton meilleur ami...")  # say the player he win.
                    if missed_count == 0:  # if he find the word in one time
                        print(
                            "Tu as reussi à sauver ton ami très rapidement. Encore bravo tu viens de gagner mon respect éternel.")  # congrats the plater
                    else:  # else inform the number of error he made
                        print("Vous avez trouvez le mot en ", missed_count, " fois. Chapeau!")
                        print(ascii_art_hangman(missed_count))  # print the ascii art of the hangman
                    print(
                        "Petite anecdote : Robespierre ne pendait pas les personnes, mais les guillotiner. Juste que je j'avais aucune idée de bourreau qui pendait les personnes et que robespierre c'est bien badass.... ")
                    input()
                    menu()

            else:  # if the letter the user type is not in the word
                print("Perdu, réessaye", nom, "!")  # inform the user he missed
                missed_count += 1  # add one to the counter of the letter
                missed_letters.append(a)
                print("Tu as essayé les lettres suivantes : ")
                display_list(missed_letters, ", ")
                print("")
                if missed_count >= MAX_COUNT:  # if the counter of error is equal of the max error the user can make
                    print(ascii_art_hangman(missed_count))  # display the ascii art of the hangman of the loose
                    print("Tapez sur une touche pour recommencez")
                    input()

                    menu()

            print("Il te reste ", MAX_COUNT - missed_count, " essais")  # display the number of errors
            print(ascii_art_hangman(missed_count))  # display the ascii art of the number of missed count
            print(word_display)  # display the word the player find


def guess_my_number(nom):
    # Author : Antoine Scherrer <antoine.scherrer@lecole-ldlc.com>
    # Licence : GPL

    print(
        "Salut %s, j'espère que tout va bien, car aujourd'hui tu peux gagner un magnifique nombre ! Pour cela tu va devoir deviner le nombre choisi par ton supra ordinateur de la mort qui tue " % nom)
    print("""
 _____ ____  ____  ____    _     _     ____  _  __
/  __//  _ \/  _ \/  _ \  / \   / \ /\/   _\/ |/ /
| |  _| / \|| / \|| | \|  | |   | | |||  /  |   / 
| |_//| \_/|| \_/|| |_/|  | |_/\| \_/||  \_ |   \ 
\____\\\\____/\____/\____/  \____/\____/\____/\_|\_\\
                                                  
""")
    max_num = int(input("Entrez le nombre maximum à deviner : "))  # get the max number
    number = random.randint(1, max_num)  # choose the number to guess
    nb_trials = 0  # number of try

    print('Bienvenue,', nom,
          'essaye de trouver le nombre choisi par le supra ordinateur de la mort qui tue qui est compris entre 1 et ',
          end="")
    print(max_num)
    essai = int(
        input("Combien d'essai veux tu avant l'auto destruction du nombre ? : "))  # get the max try the user want
    i = 0
    while i < essai:  # while the number of try is not equal to the try the user do
        user_number = int(input('Alors quel nombre choisissez vous de tester ? : '))  # number the word think it's
        nb_trials = nb_trials + 1  # add 1 to the number of trial
        if user_number == number:  # if user type the same number as the AI
            # user won !
            print("Vous avez gagnez", nom, ", respect")
            print("Cela vous à pris %s essais" % nb_trials)
            print("Tapez sur une touche pour recommencez")
            input()
            menu()
        elif user_number < number:  # if user number is under the ai number
            print("Votre nombre est trop petit !")
        elif user_number > number:  # else if user number is upper of the ai number
            print("Votre nombre est trop grand !")
        i += 1


menu()
