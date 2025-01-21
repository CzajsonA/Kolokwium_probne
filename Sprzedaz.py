def dodaj_produkt(sprzedaz):
    nazwa = input("Podaj nazwę produktu: ")
    if nazwa in sprzedaz:
        print("Produkt już istnieje!")
        return
    wyniki = []
    for i in range(1, 4):
        wynik = int(input(f"Podaj wynik sprzedaży dla tygodnia {i}: "))
        wyniki.append(wynik)
    sprzedaz[nazwa] = wyniki
    print("Produkt dodany.")

def wyswietl_sumaryczna_sprzedaz(sprzedaz):
    for produkt, wyniki in sprzedaz.items():
        suma = sum(wyniki)
        print(f"Produkt: {produkt}, Sumaryczna sprzedaż: {suma}")

def usun_produkt(sprzedaz):
    nazwa = input("Podaj nazwę produktu do usunięcia: ")
    if nazwa in sprzedaz:
        del sprzedaz[nazwa]
        print("Produkt usunięty.")
    else:
        print("Produkt nie znaleziony.")

def znajdz_najwyzsza_sprzedaz(sprzedaz):
    maks_sprzedaz = max(sum(wyniki) for wyniki in sprzedaz.values())
    najlepsze_produkty = [produkt for produkt, wyniki in sprzedaz.items() if sum(wyniki) == maks_sprzedaz]
    print(f"Produkty o najwyższej sprzedaży ({maks_sprzedaz}): {', '.join(najlepsze_produkty)}")

def oblicz_srednia_sprzedaz(sprzedaz):
    for produkt, wyniki in sprzedaz.items():
        srednia = sum(wyniki) / len(wyniki)
        print(f"Produkt: {produkt}, Średnia sprzedaż: {srednia:.2f}")

def produkty_ponizej_progu(sprzedaz):
    prog = int(input("Podaj wartość progu sprzedaży: "))
    poniżej_progu = [produkt for produkt, wyniki in sprzedaz.items() if sum(wyniki) < prog]
    if poniżej_progu:
        print(f"Produkty z sumaryczną sprzedażą poniżej {prog}: {', '.join(poniżej_progu)}")
    else:
        print("Nie znaleziono żadnych produktów poniżej progu.")

def main():
    sprzedaz = {}
    while True:
        print("\nMenu:")
        print("1. Dodaj nowy produkt")
        print("2. Wyświetl sumaryczną sprzedaż")
        print("3. Usuń produkt")
        print("4. Znajdź produkt o najwyższej sprzedaży")
        print("5. Oblicz średnią sprzedaż dla każdego produktu")
        print("6. Wyświetl produkty poniżej progu sprzedaży")
        print("7. Zakończ program")

        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dodaj_produkt(sprzedaz)
        elif wybor == "2":
            wyswietl_sumaryczna_sprzedaz(sprzedaz)
        elif wybor == "3":
            usun_produkt(sprzedaz)
        elif wybor == "4":
            znajdz_najwyzsza_sprzedaz(sprzedaz)
        elif wybor == "5":
            oblicz_srednia_sprzedaz(sprzedaz)
        elif wybor == "6":
            produkty_ponizej_progu(sprzedaz)
        elif wybor == "7":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
