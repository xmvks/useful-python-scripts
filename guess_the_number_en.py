import random

# Function to play the number guessing game
def play_game(range_min, range_max):
    number_to_guess = random.randint(range_min, range_max)
    attempts = 0
    guessed = False

    print(f"Guess the number between {range_min} and {range_max}!")

    while not guessed:
        try:
            user_guess = int(input("Enter your number: "))
            attempts += 1

            if user_guess < number_to_guess:
                print(f"The number {user_guess} is smaller than the target number.")
            elif user_guess > number_to_guess:
                print(f"The number {user_guess} is larger than the target number.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
        except ValueError:
            print("Please enter a valid integer.")

# Function to show the menu
def show_menu():
    print("Welcome to the number guessing game!")
    print("1. Easy (1-150)")
    print("2. Medium (1-650)")
    print("3. Hard (1-1000)")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select a difficulty level (1-4): ")

        if choice == '1':
            play_game(1, 150)
        elif choice == '2':
            play_game(1, 650)
        elif choice == '3':
            play_game(1, 1000)
        elif choice == '4':
            print("Thank you for playing! Made by nyski & xmvks")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
