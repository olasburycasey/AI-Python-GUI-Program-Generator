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


def main():
    print("Hello user. What would you like to do?\n"
          "\t1. Create a new LLM generated python GUI program\n"
          "\t2. Run existing LLM generated GUI program\n"
          "\t3. Give feedback on LLM generated python code\n"
          "\t4. quit")
    choice = input("\tEnter here: ")
    initiate_program(choice)


def initiate_program(choice: str):
    if choice == "1":
        generate_code_and_file()
        save_file_function()
    elif choice == "2":
        run_existing_path()


def generate_code_and_file():
    print("\nWhat type of GUI program would you like to run?"
          "\n\t1. An image display"
          "\n\t2. A video game"
          "\n\t3. Some other application"
          "\n\t4. quit")
    gui_type = input("Enter here: ")

    if gui_type == "1":
        image_description = input("\nProvide a description of the GUI image: ")
        prompt = f"Write a GUI program that opens a GUI window with the following image description:\n" \
                 f"{image_description}\n" \
                 f"Do not look for images on the web or locally. Just draw them."
    elif gui_type == "2":
        game = input("\nWhat game would you like to generate?: ")
        prompt = f"Write a Python GUI program of the game {game}." \
                 f"Do not make the program access other files or directories."
    elif gui_type == "3":
        application = input("\nDescribe the application you want to generate: ")
        prompt = f"Write a Python tkinter GUI application with the description: {application}." \
                 f"Do not make the program access other files or directories. Try to make it secure."
    else:
        print("Goodbye!")
        return

    # Generate content
    response = model.generate_content(prompt)
    response_text = response.text.strip()

    # READ CODE
    print("\nGenerated code preview:\n")
    print(response_text)

    # clean up response to only code
    code = gui_features.clean_up_response(response_text)
    print("\n\n---CODE---")
    print(code)

    # scan code to make sure it does not cause problems
    update_code = scan_code(code)
    print("---UPDATED CODE---")
    print(update_code)

    # Save code to a temporary file
    generated_filename = "generated_code.py"
    gui_features.write_code_to_file(generated_filename, update_code)

    confirmation = input("\nDo you want to run this generated code? (yes/no): ").lower()
    if confirmation == 'yes':
        print(f"Running {generated_filename} safely in a subprocess...")
        subprocess.run([sys.executable, generated_filename])
    else:
        print("Skipping execution.")

    gui_features.add_features(generated_filename, model)


def scan_code(response_code):
    prompt = f"can you scan this code to make sure it has no errors and does not access other files or directories?:" \
             f"\n\n{response_code}"
    new_response = model.generate_content(prompt)
    response_text = new_response.text.strip()
    new_code = gui_features.clean_up_response(response_text)
    if new_code == "":
        return response_code
    else:
        return new_code


def save_file_function():
    while True:
        save_file_option = input("\nWould you like to save the code permanently? (Y/N): ").strip().upper()
        if save_file_option == "Y":
            save_python_file.save_file("generated_code.py")
            break
        elif save_file_option == "N":
            if os.path.exists("generated_code.py"):
                os.remove("generated_code.py")
                print("Temporary file deleted.")
            break
        else:
            print("Error: Not a valid option. Please enter Y or N.")


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


if __name__ == "__main__":
    main()
