import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = 6
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
for char in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
guessed_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print(f"\nYou've already guessed {guess}! Please try again.")
        print(display)
        continue
    guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
    else:
        print(display)

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN!!!****************************")

    print(hangman_art.stages[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print("Word to guess: " + display)
