import os
def informatii_fisier(cale_fisier):
    rezultat = {}

    if os.path.exists(cale_fisier):
        rezultat["full_path"] = os.path.abspath(cale_fisier)
        rezultat["file_size"] = os.path.getsize(cale_fisier)

        extensie = os.path.splitext(cale_fisier)[-1]
        rezultat["file_extension"] = extensie if extensie else ""

        rezultat["can_read"] = os.access(cale_fisier, os.R_OK)

        rezultat["can_write"] = os.access(cale_fisier, os.W_OK)

    else:
        print(f"Fișierul '{cale_fisier}' nu există.")

    return rezultat


cale_fisier = "C:\\Users\\vlais\\OneDrive\\Desktop\\Facultate\\Anul III Semestrul I\\Python\\fisiere"
rezultat = informatii_fisier(cale_fisier)
print(rezultat)
