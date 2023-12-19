while True:
    print('WITAJ W KONWENTERZE JEDNOSTEK')
    print('Spis zbiorow jednostek:')
    print('0 - zamkniecie programu')
    print('1 - tempereatura')
    print('2 - powierzchnia')

    wybor = int(input('Wpisz numer twojego wyboru: '))

    if wybor == 1:
        print('=====TEMPERATURA=====')
        print('Spis numerow zamian:')
        print('1 - stopnie Celsjusza --> stopnie Kelwina')
        print('2 - stopnie Celsjusza --> stopnie Fahrenheita')
        print('3 - stopnie Kelwina --> stopnie Fahrenheita')
        print('4 - stopnie Kelwina --> stopnie Celsjusza')
        print('5 - stopnie Fahrenheita --> stopnie Celsjusza')
        print('6 - stopnie Fahrenheita --> stopnie Kelwina')

        wybor = int(input('Wpisz numer twojego wyboru: '))
        ilosc = int(input('Podaj ilosc jesdostek jaka chcesz przekonwetwoac: '))

        if wybor == 1:
            wynik = ilosc+273.15
            print(ilosc, '°C to', wynik, 'K')
        elif wybor == 2:
            wynik = ilosc*2+32
            print(ilosc, '°C to', wynik, '°F')
        elif wybor == 3:
            wynik = (ilosc-273.15)*1.8+32
            print(ilosc, 'K to', wynik, '°F')
        elif wybor == 4:
            wynik = ilosc-273.15
            print(ilosc, 'K to', wynik, '°C')
        elif wybor == 5:
            wynik = (ilosc-32)/1.8
            print(ilosc, '°F to', wynik, '°C')
        elif wybor == 6:
            wynik = (ilosc+459.67)*(5/9)
            print(ilosc, '°F to', wynik, 'K')
        else:
            print('Nie ma takiego wyboru!')

    if wybor == 2:
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

        wybor = int(input('Wpisz numer twojego wyboru: '))
        ilosc = int(input('Podaj ilosc jesdostek jaka chcesz przekonwetwoac: '))

        if wybor == 1:
            wynik = ilosc*0.01
            print(ilosc, 'mm² to', wynik, 'cm²')
        elif wybor == 2:
            wynik = ilosc*0.01
            print(ilosc, 'cm² to', wynik, 'dm²')
        elif wybor == 3:
            wynik = ilosc*0.01
            print(ilosc, 'dm² to', wynik, 'm²')
        elif wybor == 4:
            wynik = ilosc*0.01
            print(ilosc, 'm² to', wynik, 'a')
        elif wybor == 5:
            wynik = ilosc*0.01
            print(ilosc, 'a to', wynik, 'ha')
        elif wybor == 6:
            wynik = ilosc*0.01
            print(ilosc, 'ha to', wynik, 'km²')
        elif wybor == 7:
            wynik = ilosc*100
            print(ilosc, 'km² to', wynik, 'ha')
        elif wybor == 8:
            wynik = ilosc*100
            print(ilosc, 'ha to', wynik, 'a')
        elif wybor == 9:
            wynik = ilosc*100
            print(ilosc, 'a to', wynik, 'm²')
        elif wybor == 10:
            wynik = ilosc*100
            print(ilosc, 'm² to', wynik, 'dm²')
        elif wybor == 11:
            wynik = ilosc*100
            print(ilosc, 'dm² to', wynik, 'cm²')
        elif wybor == 12:
            wynik = ilosc*100
            print(ilosc, 'cm² to', wynik, 'mm²')
        else:
            print('Nie ma takiego wyboru!')
    wybor=int(input('jesli chcesz kontynuowac wpisz 1, jesli nie wpisz 0: '))