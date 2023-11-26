import os

def rename_files_with_sequence(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

        for index, filename in enumerate(files, start=1):
            new_filename = f"file{index}{os.path.splitext(filename)[1]}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = "C:/Users/vlais/OneDrive/Desktop/Facultate/Anul III Semestrul I/Python/fisiere"
    rename_files_with_sequence(directory_path)
