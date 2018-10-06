# Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
# Licence : GPL
import random

#Liste de mots fonctionalité 1
word_list = ["banana","chapeau","canapé","ordinateur","porte","lampe","photo","soleil","vert","evier","frigo","internet"]

nb_wordchoose=random.randint(1,len(word_list))

WORD_TO_GUESS=word_list[nb_wordchoose]

nb_lettres=len(WORD_TO_GUESS)




word_display = ""
for i in range(nb_lettres):
    word_display = word_display + "_"
#debug a supprimer
print(nb_lettres)
print(WORD_TO_GUESS)
print(word_display)
#fin de debug
#Fin de la fonctionalité 1

missed_count = 0
MAX_COUNT = 4

print("Welcome to hangman 1.0, guess the word !")
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
            print("You LOOSE !!!")
            break

    print("You have",MAX_COUNT-missed_count,"tries left")
    print(word_display)

