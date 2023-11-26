import os
import sys

def read_and_print_files(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        for filename in os.listdir(directory):
            if filename.endswith(extension):
                file_path = os.path.join(directory, filename)

                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"File: {filename}\n{content}\n{'=' * 30}")

                except Exception as file_error:
                    print(f"Error reading file '{filename}': {file_error}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)
