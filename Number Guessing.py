import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("You have to guess a number between 1 and 100.")
    print("You have 10 attempts to guess the correct number.\n")
    
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Initialize the number of guesses
    num_guesses = 0
    
    # Keep looping until the user runs out of guesses or guesses correctly
    while num_guesses < 10:
        # Ask the user to guess a number
        guess = int(input("Guess a number: "))
        
        # Check if the guess is out of bounds
        if guess < 1 or guess > 100:
            print("Your guess is out of bounds. Please try again.")
            continue
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Check if the guess is correct
        if guess == number:
            print(f"Congratulations! You guessed the correct number in {num_guesses} attempts.")
            break
        
        # Check if the guess is too high or too low
        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    
    # If the user runs out of guesses, reveal the correct number
    if num_guesses == 10:
        print(f"Sorry, you have run out of guesses. The correct number was {number}.")
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == '__main__':
    main()
