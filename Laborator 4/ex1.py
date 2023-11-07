import os
def lista_extensii(director):
    extensii = set()

    if os.path.exists(director) and os.path.isdir(director):
        for f in os.listdir(director):
            if os.path.isfile(os.path.join(director, f)):
                extensie = f.split('.')[-1]
                extensii.add(extensie)

    return sorted(list(extensii))


director  = "C:\\Users\\vlais\\OneDrive\\Desktop\\Facultate\\Anul III Semestrul I\\Python\\fisiere"

extensii_unice = lista_extensii(director)
print(extensii_unice)
