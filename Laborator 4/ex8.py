import os

def lista_fisiere_in_director(dir_path):
    cai_fisiere = []

    for root, dirs, files in os.walk(dir_path):
        for nume_fisier in files:
            cale_fisier = os.path.join(root, nume_fisier)
            cai_fisiere.append(cale_fisier)

    return cai_fisiere


dir_path = "C:\\director"
cai_fisiere = lista_fisiere_in_director(dir_path)
print(cai_fisiere)
