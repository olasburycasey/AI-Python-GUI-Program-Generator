import subprocess
import sys

import google.generativeai as genai
import os
import gui_features
import save_python_file

with open("API_KEY", "r") as f:
    api_key = f.read()

# Configure the API
genai.configure(api_key=api_key)

# Generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')


def initiate_program(choice: str):
    if choice == "1":
        generate_code_and_file()
        save_file()
    elif choice == "2":
        run_existing_path()


def main():
    print("Hello user. What would you like to do?\n"
          "\t1. Create a new python GUI program\n"
          "\t2. Run existing GUI program\n"
          "\t3. quit")
    choice = input("\tEnter here: ")
    initiate_program(choice)


def generate_code_and_file():
    print("\nWhat type of GUI program would you like to run?"
          "\n\t1. An image display"
          "\n\t2. A video game"
          "\n\t3. quit")
    gui_type = input("Enter here: ")

    prompt = ""
    if gui_type == "1":
        image_description = input("\nProvide a description of the GUI image: ")
        prompt = f"Write a GUI program that generates an image with the following description:\n" \
                 f"{image_description}\n" \
                 f"Do not look for images on the web or locally. Just draw them."
    elif gui_type == "2":
        game = input("\nWhat game would you like to generate?: ")
        prompt = f"Write a python GUI program of the game {game}"
    else:
        quit(0)

    # Generate content
    response = model.generate_content(prompt)
    response_text = response.text

    gui_features.write_code_to_file("generated_code.py", response_text)

    # Now run the generated code
    try:
        subprocess.run([sys.executable, "generated_code.py"], check=True)
        gui_features.add_features("generated_code.py", model)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running the generated script: {e}")
        return  # or handle appropriately


def run_existing_path():
    # Path to the saved_programs directory
    directory = 'saved_programs'

    # List only .py files in the saved_programs directory
    python_files = [file for file in os.listdir(directory) if file.endswith('.py')]

    if not python_files:
        print("No Python files found in the directory.")
        return

    # Display available Python files to the user
    print("Available Python files:")
    for idx, file in enumerate(python_files, 1):
        print(f"{idx}. {file}")

    # Prompt the user to select a file to run
    choice = input("Which file would you like to run? Enter the name or number: ").strip()

    try:
        # Try to interpret the choice as a number
        index = int(choice) - 1
        if 0 <= index < len(python_files):
            file_to_run = python_files[index]
        else:
            print("Invalid number choice. Please try again.")
            return
    except ValueError:
        # If not a number, treat it as a filename
        if choice in python_files:
            file_to_run = choice
        else:
            print("Invalid filename. Please try again.")
            return

    print(f"Running {file_to_run}...")

    # Full path to the selected file
    file_path = os.path.join(directory, file_to_run)

    # Using subprocess to run the file
    subprocess.run([sys.executable, file_path])

    # After running, add GUI features (assuming gui_features and model are available)
    gui_features.add_features(file_path, model)

    print(f"Features automatically saved to {file_path}")


def save_file():
    while True:
        save_file_option = input("Would you like to save the code? (Y or N): ")
        if save_file_option.upper() == "Y":
            save_python_file.save_file("generated_code.py")
            break
        elif save_file_option.upper() == "N":
            if os.path.exists("generated_code.py"):
                os.remove("generated_code.py")
            break
        else:
            "Error: Not a valid option"


if __name__ == "__main__":
    main()
