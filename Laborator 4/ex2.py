import os

def scrie_cai_fisiere_cu_A(director, fisier):
    with open(fisier, 'w') as fisier_output:
        if os.path.exists(director) and os.path.isdir(director):
            for radacina, subdirectoare, fisiere in os.walk(director):
                for nume_fisier in fisiere:
                    cale_fisier = os.path.join(radacina, nume_fisier)
                    if nume_fisier.startswith('A'):
                        fisier_output.write(cale_fisier + '\n')


director = "C:\\Users\\vlais\\OneDrive\\Desktop\\Facultate\\Anul III Semestrul I\\Python\\fisiere"
fisier = "C:\\Users\\vlais\\OneDrive\\Desktop\\Facultate\\Anul III Semestrul I\\Python\\fisiere\\fisier.txt"
scrie_cai_fisiere_cu_A(director, fisier)
