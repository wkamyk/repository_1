while True:
    print('======== PROGRAM ODBLICZAJACY OBJETOSC BRYL ========')
    print()
    print('Spis numerow bryl: ')
    print('0 - zamkniecie programu')
    print('1 - szescian')
    print('2 - prostopadloscian')
    print('3 - graniastoslup prawidlowy trojkatny')
    print('4 - ostroslup prawidlowy czworokatny')
    print('5 - walec')
    print('6 - stozek')
    print('7 - kula')
    print()
    bryla = int(input('Podaj numer bruly: '))
    if bryla==0:
        print('Do zobaczenia!')
        break
    elif bryla==1:
        a = int(input('Podaj dlugosc krawedzi szescianu w centymetrach: '))
        if a < 0:
            print("Długość krawędzi nie może być ujemna. Spróbuj ponownie.")
            continue
        print('Objetosc tego szesciamu jest rowna: ',a**3,"cm3")
        print()
    elif bryla==2:
        a = int(input('Podaj dlugosc pierwszej krawedzi prostopadloscianu w centymetrach: '))
        b = int(input('Podaj dlugosc drugiej krawedzi prostopadloscianu w centymetrach: '))
        c = int(input('Podaj dlugosc trzeciej krawedzi prostopadloscianu w centymetrach: '))
        if a < 0 or b < 0 or c < 0:
            print("Długości krawędzi nie mogą być ujemne. Spróbuj ponownie.")
            continue
        print('Objetosc tego prostopadloscianu jest rowna: ',a*b*c,"cm3")
        print()
    elif bryla==3:
        a = int(input('Podaj wysokosc trojkata  w podstawie w centymetrach: '))
        h = int(input('Podaj dlugosc krawedi trojkata, prostopadlej do wysyokosc trojkata w centymetrach: '))
        H = int(input('Podaj dlugosc wysokosci tej bryly w centymetrach: '))
        pp = a*h/2
        if a < 0 or h < 0 or H < 0:
            print("Wysokość i długości krawędzi nie mogą być ujemne. Spróbuj ponownie.")
            continue
        print('Objetosc tego graniastoslupa prawidlowego trojkatnego jest rowna: ',pp*H,"cm3")
        print()
    elif bryla==4:
        a = int(input('Podaj dlugosc jednej krawedzi podstawy w centymetrach: '))
        H = int(input('Podaj wysokosc tej bryly w centymetrach: '))
        pp = a**2
        if a < 0 or H < 0:
            print("Długość krawędzi i wysokość nie mogą być ujemne. Spróbuj ponownie.")
            continue
        print('Objetosc tego ostroslupa prawidlowego czworokatnego jest rowna: ',1/3*pp*H,"cm3")
        print()
    elif bryla==5:
        import math
        r = int(input("Podaj promien podstawy: "))
        H = int(input("Podaj wysokosc tego walca: "))
        if r < 0 or H < 0:
            print("Promień i wysokość nie mogą być ujemne. Spróbuj ponownie.")
            continue
        print('Objetosc tego owalca wynosi: ',math.pi*r**2*H,"cm3")
        print()
    elif bryla==6:
        import math
        r = int(input("Podaj promien podstawy: "))
        H = int(input("Podaj wysokosc tego stozka: "))
        if r < 0 or H < 0:
            print("Promień i wysokość nie mogą być ujemne. Spróbuj ponownie.")
            continue
        print('Objetosc tego walca wynosi: ',(1/3)*math.pi*r**2*H,"cm3")
        print()
    elif bryla==7:
        import math
        r = int(input("Podaj promien kuli: "))
        if r < 0:
            print("Promień kuli nie może być ujemny. Spróbuj ponownie.")
            continue
        print('Objetosc tej kuli wynosi: ',(4/3)*math.pi*r**3,"cm3")
        print()
    else:
        print('Nie ma tekiego wyboru! Sprobuj ponownie.')
        print()