while True:
    import random
    import string
    dlugosc_hasla = int(input("Podaj długość hasła (max 40 znakow): "))

    if dlugosc_hasla in range(1, 41):
        pass
    else:
        print('Max 40 znakow!')
        dlugosc_hasla = int(input("Podaj długość hasła jeszcze raz (max 40 znakow): "))
        continue
    
    def generuj_haslo(dlugosc):
        znaki = string.ascii_letters + string.digits + string.punctuation
        haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
        return haslo

    nowe_haslo = generuj_haslo(dlugosc_hasla)
    print("Wygenerowane hasło:", nowe_haslo)

    print('Czy chcesz wygenerowac jeszcze jedno haslo?')
    powtorka=input("Jesli chcesz wygenerowac nowe haslo wpisz tak: ")

    if powtorka.lower() != 'tak':
        break