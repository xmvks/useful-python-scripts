import random

# Funkcja do gry w zgadywanie liczby
def play_game(range_min, range_max):
    number_to_guess = random.randint(range_min, range_max)
    attempts = 0
    guessed = False

    print(f"Zgadnij liczbę między {range_min} a {range_max}!")

    while not guessed:
        try:
            user_guess = int(input("Podaj swoją liczbę: "))
            attempts += 1

            if user_guess < number_to_guess:
                print(f"Ta liczba {user_guess} jest mniejsza od wylosowanej.")
            elif user_guess > number_to_guess:
                print(f"Ta liczba {user_guess} jest większa od wylosowanej.")
            else:
                guessed = True
                print(f"Gratulacje! Zgadłeś liczbę {number_to_guess} w {attempts} próbach!")
        except ValueError:
            print("Proszę podaj liczbę całkowitą.")

# Funkcja menu
def show_menu():
    print("Witaj w grze zgadywania liczby!")
    print("1. Łatwy (1-150)")
    print("2. Średni (1-650)")
    print("3. Trudny (1-1000)")
    print("4. Wyjście")

def main():
    while True:
        show_menu()
        choice = input("Wybierz poziom trudności (1-4): ")

        if choice == '1':
            play_game(1, 150)
        elif choice == '2':
            play_game(1, 650)
        elif choice == '3':
            play_game(1, 1000)
        elif choice == '4':
            print("Dziękujemy za grę! Made by nyski & xmvks")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
