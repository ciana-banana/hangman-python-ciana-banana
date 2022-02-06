import random
import sys

#import countried from .txt file
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

lives = ["♡","♡","♡","♡","♡","♡","♡"]
num_of_lives = ""

def start_menu() :
    lvl_choice = input("Choose a level: 1. Easy, 2. Medium, 3. Hard ")
    if lvl_choice == "1":
        num_of_lives = 3
        print("Difficulty EASY: you start with 3 lives")
        return (1)
    elif lvl_choice == "2":
        num_of_lives = 5
        print("Difficulty MEDIUM: you start with 5 lives")
        return (2)
    elif lvl_choice == "3":
        num_of_lives = 7
        print("Difficulty HARD: you start with 7 lives")
        return (3)
    else: 
        print("Error: You didn't choose a difficulty level")



def game():
    word = random_word()
    level = start_menu()
    #if level == 1:
        #return (word)
    #elif level == 2:
        #return (word)
    #elif level == 3:
        #return (word)
    print("Guess the country: ", len(word)*"_ ")
    correct_letters = split(word)
    guessed_letters = []
    game_over = game_result()
    
    
game()

def split(word):
    return list(word)


def guessing_process():
    while num_of_lives > 0 and not game_over: 
        print(lives[:num_of_lives])
        letter = input("Input a letter or type QUIT to finish the game")
        letter = letter.lower()
        while True:
            letter = raw_input(':')
            if len(letter) == 1 or letter == "quit":
                break
                print('Please enter only one character or QUIT to exit the game')
        
            if letter == "quit":
                sys.exit("Goodbye :)")
            elif letter in guessed_letters:
                print(f"This letter was already used before {letter}")
                print(guessed_letters)
            elif letter not in guessed_letters and letter not in correct_letters:
                print("Wrong guess, try again")
                print(guessed_letters)
                guessed_letters.append(letter)
                num_of_lives -=1
                print(lives[:num_of_lives])
            elif letter in correct_letters
                ...
                ...
            else:
                print("Wrong input, enter one character or QUIT to exit the game")
        game_result()
        play_again()  
        
def game_result():
    check =  all(item in correct_letters for item in guessed_letters)
    if check is True:
        print("Congratulations, you won!")
    else:
        print("You ran out of lives, you lost!")
                
#asking to user wether he wants to play again
def quit():
    print("Do you want to play again?\nType 'yes' or 'quit' ")
    user_answer = input()
    if user_answer == "quit":
        print("Good-Bye!")
        sys.exit
    else:
        # def play()
        print("ok")

quit()
                

if __name__ == '__main__':
    while True :
        os.system("cls")
        guess_word = random_word()
        num_of_lives = start_menu()
        play (guess_word, num_of_lives)      

        

