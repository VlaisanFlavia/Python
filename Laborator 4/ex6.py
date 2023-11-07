import os

def cauta_in_fisiere_cu_callback(target, to_search, callback=None):
    rezultat = []

    if not os.path.exists(target):
        raise ValueError("Calea specificată în 'target' nu există.")

    if os.path.isfile(target):
        try:
            if to_search_in_file(target, to_search):
                rezultat.append(target)
        except Exception as e:
            if callback:
                callback(e)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for nume_fisier in files:
                cale_fisier = os.path.join(root, nume_fisier)
                try:
                    if to_search_in_file(cale_fisier, to_search):
                        rezultat.append(cale_fisier)
                except Exception as e:
                    if callback:
                        callback(e)
    else:
        raise ValueError("Argumentul 'target' nu este nici fișier, nici director.")

    return rezultat

def to_search_in_file(cale_fisier, to_search):
    with open(cale_fisier, 'r', encoding='utf-8') as fisier:
        continut = fisier.read()
        return to_search in continut

def callback_eroare(exceptie):
    print(f"EROARE: {exceptie}")

target = "C:\\Users\\vlais\\OneDrive\\Desktop\\Facultate\\Anul III Semestrul I\\Python\\fisiere"
to_search = "text_de_cautat"
rezultat = cauta_in_fisiere_cu_callback(target, to_search, callback_eroare)
print(rezultat)
