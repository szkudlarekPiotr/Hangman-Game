from hangman_art import stages, logo
from hangman_words import word_list
import random

display = []
game = True
lives = 6
random_number = random.randint(1, len(word_list))
chosen_word = word_list[random_number - 1]

print(logo)

for letter in chosen_word:
    display.append('_')

while game:

    print(stages[lives])

    guess = input('Guess the letter: ').lower()

    for n in range(0, len(chosen_word)):
        if guess == chosen_word[n]:
            if guess in display:
                print(f"You've already guessed {guess}.")
            display[n] = guess
    print(display)


    if guess not in chosen_word:
        print(f'The letter "{guess}" is not in the word, you lose life :(')
        lives -= 1
        if lives <= 0:
            game = False
            print(stages[0])
            print('You lost :(')
            print(f'The word was {chosen_word}.')
        elif '_' not in display:
            game = False
            print('You won!')
