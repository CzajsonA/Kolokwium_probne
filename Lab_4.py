import math

def pole_kola(r):
    pole = math.pi * r**2
    print(f"Pole koła o promieniu {r} wynosi {pole:.2f}")

def pole_trapezu(a, b, h):
    pole = ((a + b) * h) / 2
    print(f"Pole trapezu o podstawach {a}, {b} i wysokości {h} wynosi {pole:.2f}")
    return pole

def czy_dodatnia(x):
    if x > 0:
        print(f"Liczba {x} jest dodatnia.")
    elif x < 0:
        print(f"Liczba {x} jest ujemna.")
    else:
        print(f"Liczba {x} jest zerem.")

def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    print(f"Twoje BMI wynosi: {bmi:.2f}")
    if bmi < 18.5:
        print("Niedowaga")
    elif 18.5 <= bmi < 24.9:
        print("Prawidłowa waga")
    elif 25 <= bmi < 29.9:
        print("Nadwaga")
    else:
        print("Otyłość")
    return bmi

def srednia(lista_liczb):
    if not lista_liczb:
        print("Lista jest pusta, nie można obliczyć średniej.")
        return None
    srednia_wartosc = sum(lista_liczb) / len(lista_liczb)
    print(f"Średnia z liczb {lista_liczb} wynosi {srednia_wartosc:.2f}")
    return srednia_wartosc

def wypisz_imie_i_wiek(imie, wiek=20):
    print(f"Imię: {imie}, Wiek: {wiek}")
    print(wypisz_imie_i_wiek.__doc__)

def pole_trojkata(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Podane boki nie tworza trójkąta.")
        return None
    s = (a + b + c) / 2
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Pole trójkąta o bokach {a}, {b}, {c} wynosi {pole:.2f}")
    return pole

def potega_rekurencyjna(a, n):
    if n == 0:
        return 1
    return a * potega_rekurencyjna(a, n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Przenieś krążek z {source} na {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Przenieś krążek z {source} na {target}")
    hanoi(n - 1, auxiliary, target, source)

def odwracanie_stringa(s):
    return s[::-1]

if __name__ == "__main__":
    pole_kola(5)

    pole_trapezu(3, 5, 4)

    czy_dodatnia(-10)
    czy_dodatnia(0)
    czy_dodatnia(25)

    oblicz_bmi(70, 1.75)

    srednia([10, 20, 30, 40])

    wypisz_imie_i_wiek("Jan")
    wypisz_imie_i_wiek("Anna", 25)

    pole_trojkata(3, 4, 5)

    print(f"3^4 = {potega_rekurencyjna(3, 4)}")

    print(f"10-ty wyraz ciągu Fibonacciego: {fibonacci(10)}")

    print("Rozwiązanie problemu Wieży Hanoi dla 3 krążków:")
    hanoi(3, "A", "C", "B")

    print(f"Odwrócony string: {odwracanie_stringa('Python')}")
