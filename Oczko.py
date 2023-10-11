import random

# Odbieranie danych
liczbakart = int(input("Podaj liczbę kart: "))

# Dane o kartach
mozliwe_karty = [4, 3, 2, 10, 11]
karty_gracza = []
karty_przeciwnika = random.randint(3, 35)
# Tworzenie kart
for i in range(liczbakart):
  nowa_karta = random.choice(mozliwe_karty)
  karty_gracza.append(nowa_karta)

# Obliczanie sumy wszystkich kart
sumaLiczb = sum(karty_gracza)
print(f"Twoja suma: {sumaLiczb}")
print(f"Suma przeciwnika: {karty_przeciwnika}")
# Wysyłanie wiadomości o Wygranej / Przegranej
if karty_przeciwnika == 21:
   print("Twój przeciwnik wygrał!")


if  sumaLiczb == karty_przeciwnika or (sumaLiczb > 21 and karty_przeciwnika > 21):
    print("Remis! ")

elif sumaLiczb <= 21 and karty_przeciwnika > 21:
    print("Wygrałeś")
  
elif karty_przeciwnika <= 21 and sumaLiczb > 21:
   print("Przegrałeś!")

elif karty_przeciwnika < 21 and sumaLiczb < 21:
    if sumaLiczb > karty_przeciwnika:
      print("Wygrałeś!")
    else:
      print("Przegrałeś!")
else:
    print("Wystąpił błąd!")
