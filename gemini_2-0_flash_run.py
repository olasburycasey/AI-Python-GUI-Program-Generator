import subprocess
import sys
import google.generativeai as genai
import os
import gui_features
import save_python_file
from safe_code_scanner import SafeCodeScanner
import os
from datetime import datetime

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
    while True:
        print("Welcome to the Python GUI program generator application.\n\n"
              "What would you like to do?\n"
              "\t1. Create a new LLM generated python GUI program\n"
              "\t2. Run existing LLM generated GUI program\n"
              "\t3. Give feedback on LLM generated python GUI program\n"
              "\t4. quit")
        choice = input("\tEnter here: ")
        if choice == "4":
            print("Thanks for using this program.")
            break
        else:
            initiate_program(choice)


def initiate_program(choice: str):
    if choice == "1":
        generate_code_and_file()
    elif choice == "2":
        run_existing_path()
    elif choice == "3":
        give_feedback()
    else:
        print(f"Error: Not a valid option {choice}")


def generate_code_and_file():
    print("\nWhat type of GUI program would you like me to generate?"
          "\n\t1. An image display"
          "\n\t2. A video game"
          "\n\t3. Some other application"
          "\n\t4. Go to the homescreen"
          "\n\t5. quit")
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
    elif gui_type == "4":
        return
    else:
        print("Error: Not a valid option. Returning to home-screen.")
        return

    # Generate content
    response = model.generate_content(prompt)
    response_text = response.text.strip()

    print("\nGenerated code preview:\n")
    print(response_text)

    # Clean up response to extract only the code
    code = gui_features.clean_up_response(response_text)
    print("\n\n---RAW CODE---")
    print(code)

    # Fix common errors and make it more robust
    code = attempt_to_fix_code(code)

    print("\n\n---FIXED CODE---")
    print(code)

    if code:
        update_code = scan_code(code)
        if not update_code:
            print("Code rejected due to safety concerns.")
            return

        print("---UPDATED CODE---")
        print(update_code)

        generated_filename = "generated_code.py"
        gui_features.write_code_to_file(generated_filename, update_code)

        confirmation = input("\nDo you want to run this generated code? (yes/no): ").lower()
        if confirmation == 'yes':
            print(f"Running {generated_filename} safely in a subprocess...")
            subprocess.run([sys.executable, generated_filename])
        else:
            print("Skipping execution.")

        gui_features.add_features(generated_filename, model)
        save_file_function()


def attempt_to_fix_code(raw_code: str) -> str:
    """
    Use the model to review and correct the code for syntax or runtime issues.
    """
    fix_prompt = f"The following Python GUI code may contain errors or unsafe behavior. Please fix any syntax errors," \
                 f"runtime issues, and add appropriate exception handling. Ensure the program won't crash." \
                 f"\n\n{raw_code}"
    response = model.generate_content(fix_prompt)
    clean_code = gui_features.clean_up_response(response.text)
    return clean_code


def scan_code(code: str) -> str:
    """
    Scans code for safety. Returns the same code if safe.
    If unsafe, returns an empty string and prints why.
    """
    scanner = SafeCodeScanner("dummy_path")  # we only use scan_source here
    is_safe = scanner.scan_source(code)
    if is_safe:
        return code
    else:
        print("🚫 Unsafe code detected. Aborting write and run.")
        return ""


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
    gui_features.run_if_safe(file_path)

    # After running, add GUI features (assuming gui_features and model are available)
    gui_features.add_features(file_path, model)

    print(f"Features automatically saved to {file_path}")


def give_feedback():
    # Path to the saved_programs directory
    directory = 'saved_programs'

    print("Let's give a file some feedback.")
    python_files = [file for file in os.listdir(directory) if file.endswith('.py')]

    if not python_files:
        print("No Python files found in the directory.")
        return

    # Display available Python files to the user
    print("Available Python files:")
    for idx, file in enumerate(python_files, 1):
        print(f"{idx}. {file}")

    # Prompt the user to select a file
    choice = input("Which file would you like me to provide feedback on? Enter the name or number: ").strip()

    try:
        index = int(choice) - 1
        if 0 <= index < len(python_files):
            file_to_run = python_files[index]
        else:
            print("Invalid number choice.")
            return
    except ValueError:
        if choice in python_files:
            file_to_run = choice
        else:
            print("Invalid filename.")
            return

    print(f"Rating {file_to_run}...")

    file_path = os.path.join(directory, file_to_run)

    with open(file_path, "r") as file:
        full_code = file.read()

    prompt = f"{full_code}\n\n" \
             f"Can you provide some feedback on this code?\n" \
             f"Rate it on a scale from 1 to 10, with 10 being excellent.\n" \
             f"Then, improve the code and make it a 10/10 version."

    response = model.generate_content(prompt)
    response_text = response.text

    print("\n--- MODEL RESPONSE ---\n")
    print(response_text)

    # Extract new code from response (if any)
    new_code = gui_features.clean_up_response(response_text)

    if new_code:
        print("\n--- UPDATED CODE SUGGESTION ---\n")
        print(new_code)

        save_choice = input("\nWould you like to save the improved version? (y/n): ").strip().lower()
        if save_choice == 'y':
            base_name = os.path.splitext(file_to_run)[0]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{base_name}_improved_{timestamp}.py"
            new_file_path = os.path.join(directory, new_filename)

            with open(new_file_path, "w") as f:
                f.write(new_code)

            print(f"Improved code saved to {new_file_path}")
        else:
            print("Improved code not saved.")
    else:
        print("No updated code found in the model's response.")


if __name__ == "__main__":
    main()
