import random
import hangman_stages  # Assuming hangman_stages.py has a variable 'stages'

# List of words
word_list = ["phone", "handle", "tube_light"]
lives = 6
chosen_word = random.choice(word_list)
print(f"Chosen word (for debugging): {chosen_word}")  # Optional: for debugging

# Initialize display with underscores
display = ['_'] * len(chosen_word)
print(display)

game_over = False

# Main game loop
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    # Check if guessed letter is in the word
    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = guessed_letter  # Replace underscore with the correct letter
    else:
        lives -= 1  # Reduce lives only for wrong guesses
        print(f"Wrong guess! Lives remaining: {lives}")
    
    print(display)
    
    # Check for win
    if '_' not in display:
        game_over = True
        print("Well done, you won!")
    
    # Check for loss
    if lives == 0:
        game_over = True
        print(f"You lose! The word was '{chosen_word}'.")
    
    # Print the hangman stage based on lives remaining
    print(hangman_stages.stages[lives])  # Assumes hangman_stages has a list 'stages'
