import random

def guessing_game():
    print("Welcome to the number guessing game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess from 1 to 100: "))
            attempts += 1

            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else: 
                print(f"Congratulations! You guessed! the number is {guess} and it took you {attempts} attempts")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100")
        
if __name__ == "__main__":
    guessing_game()