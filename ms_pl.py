import random
import json
import os

# Funkcja do zapisania stanu gry
def save_game(data):
    with open("data.gs", "w") as f:
        json.dump(data, f)
    print("Stan gry zapisany!")

# Funkcja do załadowania stanu gry
def load_game():
    if os.path.exists("data.gs"):
        with open("data.gs", "r") as f:
            data = json.load(f)
        print("Stan gry załadowany!")
        return data
    else:
        print("Brak zapisanego stanu gry.")
        return {"money": 0, "items": []}

# Funkcja pracy
def work(data):
    earnings = random.randint(2, 31)
    if random.random() < 0.1:  # 10% szans na przedmiot
        item_value = random.randint(20, 43)  # przedmiot
        print(f"Zyskałeś przedmiot o wartości {item_value}$!")
        data["items"].append(item_value)
    else:
        print(f"Zyskałeś {earnings}$ za pracę.")
        data["money"] += earnings

# Funkcja sprzedaży
def sell(data):
    if len(data["items"]) > 0:
        item_value = data["items"].pop()  # sprzedajemy ostatni przedmiot
        sale_value = random.randint(20, 30)
        print(f"Sprzedałeś przedmiot o wartości {item_value}$ za {sale_value}$.")
        data["money"] += sale_value
    else:
        print("Błąd: Nie masz przedmiotów do sprzedaży.")

# Funkcja inwestycji
def invest(data):
    investment = float(input("Podaj kwotę do inwestycji (min. 15$): "))
    if investment >= 15:
        earnings = investment * 2
        print(f"Zainwestowałeś {investment}$ i otrzymałeś {earnings}$!")
        data["money"] += earnings
    else:
        print("Kwota inwestycji musi być co najmniej 15$.")

# Funkcja allegro (scam)
def allegro(data):
    if random.random() < 0.12:  # 12% szans na stracenie pełnej kwoty
        print("Zostałeś oszukany! Straciłeś pełną kwotę produktu.")
        scam_loss = random.randint(20, 30)
        data["money"] -= scam_loss
    else:
        item_value = random.randint(34, 43)
        scam_value = random.randint(10, 33)
        print(f"Zasymulowałeś scam i zdobyłeś przedmiot o wartości {item_value}$ oraz {scam_value}$ za scam!")
        data["money"] += scam_value
        data["items"].append(item_value)

# Menu główne
def main():
    data = load_game()
    
    while True:
        print("\nWybierz opcję:")
        print("1. Praca")
        print("2. Sprzedaż")
        print("3. Inwestycja")
        print("4. Allegro (scam)")
        print("5. Zapisz grę")
        print("6. Wyjdź")
        
        choice = input("Wybierz opcję (1-6): ")
        
        if choice == '1':
            work(data)
        elif choice == '2':
            sell(data)
        elif choice == '3':
            invest(data)
        elif choice == '4':
            allegro(data)
        elif choice == '5':
            save_game(data)
        elif choice == '6':
            print("Dziękujemy za grę!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()