if __name__ == '__main__':
    # deklarujemy i inicjalizujemy zmienne
    year = 2023
    pythonYear = 1989
    # obliczamy wiek Pythona
    agePython = year - pythonYear

    # pobieramy dane
    name = input('Jak się nazywasz? ')
    age = int(input('Ile masz lat? '))

    # wyświetlamy komunikaty
    print("Witaj", name)
    print("Mów mi Python, mam", agePython, "lat.")

    # instrukcja warunkowa
    if age > agePython:
        print('Jesteś starszy ode mnie.')
    else:
        print('Jesteś młodszy ode mnie.')
