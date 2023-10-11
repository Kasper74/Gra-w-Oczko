import random

# Odbieranie danych
liczbakart = int(input("Podaj liczbę kart: "))

# Dane o kartach
mozliwe_karty = [4, 3, 2, 10, 11]
karty_gracza = []

# Tworzenie kart
for i in range(liczbakart):
  nowa_karta = random.choice(mozliwe_karty)
  karty_gracza.append(nowa_karta)

# Obliczanie sumy wszystkich kart
sumaLiczb = sum(karty_gracza)
print(f"Twoje liczby: {karty_gracza}")

# Wysyłanie wiadomości, o wygranej / przegranej
if sumaLiczb > 21:
   print(f"Przegrałeś! Suma twoich liczb to {sumaLiczb}")
elif sumaLiczb < 21:
   print(f"Przegrałeś! Suma twoich liczb to {sumaLiczb}")
else:
   print(f"Wygrałeś! Suma twoich liczb to {sumaLiczb}")
