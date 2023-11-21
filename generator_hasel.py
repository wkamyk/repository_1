print('PROGRAM DO GENEROWANIA HASEL')

import secrets
import string

dlugosc=int(input('Podaj dlugosc hasla: '))
cyfry=int(input('Podaj ilos cyfr: '))
def generowanie_hasla(dlugosc, cyfry):
    # Sprawdź, czy suma długości liter i cyfr jest równa oczekiwanej długości
    if dlugosc < cyfry:
        print("Błąd: Łączna długość liter i cyfr nie może być mniejsza niż oczekiwana długość hasła.")
        return None

    # Zdefiniuj zestaw znaków, z których ma być generowane hasło
    characters = string.ascii_letters + string.digits

    # Wybierz cyfry do hasła
    digits = ''.join(secrets.choice(string.digits) for _ in range(cyfry))

    # Reszta hasła (bez cyfr)
    length_without_digits = dlugosc - cyfry
    password_without_digits = ''.join(secrets.choice(characters) for _ in range(length_without_digits))

    # Połącz obie części hasła
    password = password_without_digits + digits

    # Wymieszaj hasło, aby zachować losowość
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password


strong_password = generowanie_hasla(dlugosc, cyfry)
if strong_password:
    print(f"Silne hasło: {strong_password}")
