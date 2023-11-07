import os

def cauta_in_fisiere(target, to_search):
    rezultat = []

    if not os.path.exists(target):
        raise ValueError("Calea specificată în 'target' nu există.")

    if os.path.isfile(target):
        if to_search_in_file(target, to_search):
            rezultat.append(target)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for nume_fisier in files:
                cale_fisier = os.path.join(root, nume_fisier)
                if to_search_in_file(cale_fisier, to_search):
                    rezultat.append(cale_fisier)
    else:
        raise ValueError("Argumentul 'target' nu este nici fișier, nici director.")

    return rezultat

def to_search_in_file(cale_fisier, to_search):
    try:
        with open(cale_fisier, 'r', encoding='utf-8') as fisier:
            continut = fisier.read()
            return to_search in continut
    except (IOError, UnicodeDecodeError):
        return False

target = "C:\\Users\\vlais\\OneDrive\\Desktop\\Facultate\\Anul III Semestrul I\\Python\\fisiere"
to_search = "text_de_cautat"
rezultat = cauta_in_fisiere(target, to_search)
print(rezultat)
