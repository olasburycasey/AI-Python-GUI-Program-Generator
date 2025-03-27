import shutil
import re
import os


def save_file(generated_code_file):
    while True:
        destination_file_name = input("File name (without extension): ")

        # Replace spaces with underscores
        destination_file_name = destination_file_name.replace(" ", "_")

        # Check for invalid characters using regex
        if not re.match(r'^[\w\-.]+$', destination_file_name):
            print("Invalid file name. Please use only letters, numbers, underscores, hyphens, or periods.")
            continue

        file_path = f"saved_files/{destination_file_name}.py"

        # Check if file exists
        if os.path.exists(file_path):
            overwrite = input(f"'{destination_file_name}.py' already exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != 'y':
                print("Choose a different name.")
                continue

        try:
            shutil.copy(generated_code_file, file_path)
            print("File saved successfully as:", destination_file_name + ".py")
            break
        except Exception as e:
            print(f"Error saving file: {e}")
