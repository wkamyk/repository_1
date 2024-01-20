while True:
    print('WITAJ W KONWENTERZE JEDNOSTEK')
    print('Spis zbiorow jednostek:')
    print('0 - zamkniecie programu')
    print('1 - tempereatura')
    print('2 - powierzchnia')

    wybor = int(input('Wpisz numer twojego wyboru: '))

    if wybor == 0:
        print('Zamykanie programu...')
        break

    elif wybor == 1:
        print('=====TEMPERATURA=====')
        print('Spis numerow zamian:')
        print('1 - stopnie Celsjusza --> stopnie Kelwina')
        print('2 - stopnie Celsjusza --> stopnie Fahrenheita')
        print('3 - stopnie Kelwina --> stopnie Fahrenheita')
        print('4 - stopnie Kelwina --> stopnie Celsjusza')
        print('5 - stopnie Fahrenheita --> stopnie Celsjusza')
        print('6 - stopnie Fahrenheita --> stopnie Kelwina')

        wybor_temperatura = int(input('Wpisz numer twojego wyboru: '))
        ilosc_temperatura = int(input('Podaj ilosc jednostek jaką chcesz przekonwertować: '))

        if wybor_temperatura == 1:
            wynik = ilosc_temperatura + 273.15
            print(ilosc_temperatura, '°C to', wynik, 'K')
        elif wybor_temperatura == 2:
            wynik = ilosc_temperatura * 1.8 + 32
            print(ilosc_temperatura, '°C to', wynik, '°F')
        elif wybor_temperatura == 3:
            wynik = (ilosc_temperatura - 273.15) * 1.8 + 32
            print(ilosc_temperatura, 'K to', wynik, '°F')
        elif wybor_temperatura == 4:
            wynik = ilosc_temperatura - 273.15
            print(ilosc_temperatura, 'K to', wynik, '°C')
        elif wybor_temperatura == 5:
            wynik = (ilosc_temperatura - 32) / 1.8
            print(ilosc_temperatura, '°F to', wynik, '°C')
        elif wybor_temperatura == 6:
            wynik = (ilosc_temperatura + 459.67) * (5 / 9)
            print(ilosc_temperatura, '°F to', wynik, 'K')
        else:
            print('Nie ma takiego wyboru!')

    elif wybor == 2:
        print('=====POWIERZCHNIA=====')
        print('Spis numerow zamian:')
        print('1 - mm² --> cm²')
        print('2 - cm² --> dm²')
        print('3 - dm² --> m²')
        print('4 - m² --> ary')
        print('5 - ary --> hektary')
        print('6 - hektary --> km²')
        print('7 - km² --> hektary')
        print('8 - hektary --> ary')
        print('9 - ary --> m²')
        print('10 - m² --> dm²')
        print('11 - dm² --> cm²')
        print('12 - cm² --> mm²')

        wybor_powierzchnia = int(input('Wpisz numer twojego wyboru: '))
        ilosc_powierzchnia = int(input('Podaj ilość jednostek jaką chcesz przekonwertować: '))

        if wybor_powierzchnia == 1:
            wynik = ilosc_powierzchnia * 0.01
            print(ilosc_powierzchnia, 'mm² to', wynik, 'cm²')
        elif wybor_powierzchnia == 2:
            wynik = ilosc_powierzchnia * 0.01
            print(ilosc_powierzchnia, 'cm² to', wynik, 'dm²')
        elif wybor_powierzchnia == 3:
            wynik = ilosc_powierzchnia * 0.01
            print(ilosc_powierzchnia, 'dm² to', wynik, 'm²')
        elif wybor_powierzchnia == 4:
            wynik = ilosc_powierzchnia * 0.01
            print(ilosc_powierzchnia, 'm² to', wynik, 'a')
        elif wybor_powierzchnia == 5:
            wynik = ilosc_powierzchnia * 0.01
            print(ilosc_powierzchnia, 'a to', wynik, 'ha')
        elif wybor_powierzchnia == 6:
            wynik = ilosc_powierzchnia * 0.01
            print(ilosc_powierzchnia, 'ha to', wynik, 'km²')
        elif wybor_powierzchnia == 7:
            wynik = ilosc_powierzchnia * 100
            print(ilosc_powierzchnia, 'km² to', wynik, 'ha')
        elif wybor_powierzchnia == 8:
            wynik = ilosc_powierzchnia * 100
            print(ilosc_powierzchnia, 'ha to', wynik, 'a')
        elif wybor_powierzchnia == 9:
            wynik = ilosc_powierzchnia * 100
            print(ilosc_powierzchnia, 'a to', wynik, 'm²')
        elif wybor_powierzchnia == 10:
            wynik = ilosc_powierzchnia * 100
            print(ilosc_powierzchnia, 'm² to', wynik, 'dm²')
        elif wybor_powierzchnia == 11:
            wynik = ilosc_powierzchnia * 100
            print(ilosc_powierzchnia, 'dm² to', wynik, 'cm²')
        elif wybor_powierzchnia == 12:
            wynik = ilosc_powierzchnia * 100
            print(ilosc_powierzchnia, 'cm² to', wynik, 'mm²')
        else:
            print('Nie ma takiego wyboru! ')
