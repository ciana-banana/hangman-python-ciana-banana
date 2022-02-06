
# TODO
# def random word()
# def quit()


import random
import sys


def quit():
    print("Do you want to play again?\nType 'yes' or 'quit' ")
    user_answer = input()
    if user_answer == "quit":
        print("Good-Bye!")
        sys.exit
    else:
        # def play()
        print("ok")

# quit()

def random_word():
    word_collection_file = open("countries-and-capitals.txt")
    list_of_countries = []

    for line in word_collection_file:
        strip_line = line.strip().split(" | ", 1)
        list_of_countries.append(strip_line[0])

    pick_random_word = str(random.choice(list_of_countries))
    guess_word = pick_random_word.lower()
    # print(guess_word)
    return guess_word

random_word()




