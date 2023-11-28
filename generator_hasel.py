while True:
    import random
    import string
    dlugosc_hasla = int(input("Podaj długość hasła: "))
    
    if isinstance(dlugosc_hasla, int):
        pass
    else:
        print('Wpisz liczbe calkowita!')
        True
    
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