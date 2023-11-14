print('======== PROGRAM ODBLICZAJACY OBJETOSC BRYL ========')
print()
print('Spis numerow bryl: ')
print('1 - szescian')
print('2 - prostopadloscian')
print('3 - graniastoslup prawidlowy trojkatny')
print('4 - ostroslup prawidlowy czworokatny')
print('5 - walec')
print('6 - stozek')
print('7 - kula')
print()
bryla = int(input('Podaj numer bruly: '))

if bryla==1:
    a = int(input('Podaj dlugosc krawedzi szescianu w centymetrach: '))
    print('Objetosc tego szesciamu jest rowna: ',a**3,"cm3")
elif bryla==2:
    a = int(input('Podaj dlugosc pierwszej krawedzi prostopadloscianu w centymetrach: '))
    b = int(input('Podaj dlugosc drugiej krawedzi prostopadloscianu w centymetrach: '))
    c = int(input('Podaj dlugosc trzeciej krawedzi prostopadloscianu w centymetrach: '))
    print('Objetosc tego prostopadloscianu jest rowna: ',a*b*c,"cm3")
elif bryla==3:
    a = int(input('Podaj wysokosc trojkata  w podstawie w centymetrach: '))
    h = int(input('Podaj dlugosc krawedi trojkata, prostopadlej do wysyokosc trojkata w centymetrach: '))
    H = int(input('Podaj dlugosc wysokosci tej bryly w centymetrach: '))
    pp = a*h/2
    print('Objetosc tego graniastoslupa prawidlowego trojkatnego jest rowna: ',pp*H,"cm3")
elif bryla==4:
    a = int(input('Podaj dlugosc jednej krawedzi podstawy w centymetrach: '))
    H = int(input('Podaj wysokosc tej bryly w centymetrach: '))
    pp = a**2
    print('Objetosc tego ostroslupa prawidlowego czworokatnego jest rowna: ',1/3*pp*H,"cm3")
elif bryla==5:
    a = int(input('Podaj dlugosc jednej krawedzi podstawy w centymetrach: '))
    H = int(input('Podaj wysokosc tej bryly w centymetrach: '))
    pp = a**2
    print('Objetosc tego ostroslupa prawidlowego czworokatnego jest rowna: ',1/3*pp*H,"cm3")