import os

def citeste_fisier_sau_extensii(my_path):
    if os.path.isfile(my_path):
        with open(my_path, 'r') as fisier:
            continut = fisier.read()
            return continut[-20:]
    elif os.path.isdir(my_path):
        extensii = {}
        for root, dirs, files in os.walk(my_path):
            for nume_fisier in files:
                extensie = nume_fisier.split('.')[-1]
                if extensie not in extensii:
                    extensii[extensie] = 1
                else:
                    extensii[extensie] += 1
        extensii_sorted = sorted(extensii.items(), key=lambda x: x[1], reverse=True)
        return extensii_sorted
    else:
        return "Calea specificata nu este nici un fișier, nici un director."


my_path = "C:\\Users\\vlais\\OneDrive\\Desktop\\Facultate\\Anul III Semestrul I\\Python\\fisiere"
rezultat = citeste_fisier_sau_extensii(my_path)
print(rezultat)
