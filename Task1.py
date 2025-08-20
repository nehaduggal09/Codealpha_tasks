import random

# 1. Predefined list of 5 words
word_list = ['apple', 'banana', 'cherry', 'grape', 'orange']

# 2. Randomly choose a word
secret_word = random.choice(word_list)

# 3. Initialize game state
guessed_letters = []       # letters guessed by the player
incorrect_guesses = 0      # count of wrong guesses
max_guesses = 6

# 4. Create display version of the word (with underscores)
display_word = ['_'] * len(secret_word)

# 5. Main game loop
while incorrect_guesses < max_guesses and '_' in display_word:
    print("\nCurrent word: ", ' '.join(display_word))
    print("Guessed letters: ", ' '.join(guessed_letters))
    print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")
    
    guess = input("Guess a letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in secret_word:
        print("Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# 6. Game over - win or lose
if '_' not in display_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nYou ran out of guesses. The word was:", secret_word)
