import os

def extensii_fisiere_director(director):
    extensii = set()

    if os.path.exists(director) and os.path.isdir(director):
        fisiere = os.listdir(director)
        for nume_fisier in fisiere:
            if os.path.isfile(os.path.join(director, nume_fisier)):
                extensie = nume_fisier.split('.')[-1]
                if extensie:
                    extensii.add(extensie)

    return sorted(list(extensii))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Utilizare gresita!")
    else:
        director = sys.argv[1]
        extensii_unice = extensii_fisiere_director(director)
        print(extensii_unice)
