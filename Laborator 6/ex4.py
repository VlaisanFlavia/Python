import os
import sys

def count_files_by_extension(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directory not found")

        if not os.access(directory, os.R_OK):
            raise PermissionError("No read permissions for the directory")

        all_files = os.listdir(directory)

        if not all_files:
            print(f"The directory '{directory}' is empty.")
            return

        extension_counts = {}

        for filename in all_files:
            _, file_extension = os.path.splitext(filename)
            extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        print("Number of files by extension:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} file(s)")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)
