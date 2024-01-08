from words import words
import random
import string
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()
figlet.setFont(font='big')

def main():
    level = get_valid_level(int(input("Choose your level (1/2/3): ")))
    lives = get_lives(level)
    word = get_word(level).upper()
    
    hangman(word, lives)

def get_valid_level(n):
    while True:
        try:          
            #validating user input
            if n not in [1,2,3]:
                print("Not valid level, try again.")
                n = int(input("Choose your level (1/2/3): "))
                continue
            return n
        except ValueError:
            print("Not valid level, try again.")
            n = int(input("Choose your level (1/2/3): "))
            pass
    
def get_lives(level):
    if level == 1:
        lives = 7
    elif level == 2:
        lives = 5
    elif level == 3:
        lives = 3
    else:
        raise ValueError
    return lives

def get_word(level):
    #choose random word in list
    answer = random.choice(words)
    #selecting word length based on level
    while True:
        if level == 1:
            while len(answer) > 5:
                answer = random.choice(words)
        elif level ==2:
            while len(answer)>9 or len(answer)<6:
                answer = random.choice(words)
        elif level == 3:
            while len(answer) < 10:
                answer = random.choice(words)
        return answer

def hangman(answer, life):
    #retrieving word based on level
    word_letters = set(answer) #letters in word/answer
    alphabet = set(string.ascii_uppercase) #letters in alphabet
    guessed_letters = set() #letters that have been guessed

    while len(word_letters) > 0:

        #displaying used letters
        print(f"You have {life} lives left \nYou have used these letters: {'   '.join(guessed_letters)}\n")

        #displaying current word
        word_list = [letter if letter in guessed_letters else '-' for letter in answer]       
        print(f"Word: {' '.join(figlet.renderText(word_list))}")

        #getting user input/guess
        guess = input("Guess: ").upper()
        print()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                life -= 1
                if life == 0:
                    print("You ran out of lives! Try again next time!")
                    break

        #user enters same letter 
        elif guess in guessed_letters:
            print("You already guessed this! Try again.")

        #user enters invalid character
        else:
            print("Invalid character. Try again.")

    #print that user has solved the hangman puzzle
    if len(word_letters) == 0:
        print("Congratulations! You completed the puzzle!")

    print("Your word was", figlet.renderText(answer.upper()))

if __name__ == "__main__":
    main()
