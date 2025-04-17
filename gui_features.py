import os
import subprocess
import sys

import google.generativeai as genai


def write_code_to_file(file_name, response_text):
    if os.path.exists("generated_code.py"):
        os.remove("generated_code.py")
    # list of prohibited libraries that should not be used at all
    prohibited_libraries = ["os", "sys", "subprocess", "shutil", "socket", "requests", "http.client", "urllib", "ftplib",
                            "ctypes", "cffi", "pickle", "eval", "exec", "compile", "multiprocessing", "threading",
                            "pathlib", "glob"]

    # Write each line of the response text to a file
    with open(file_name, "w") as file:
        is_python_code = False
        for line in response_text.splitlines():
            split_line = line.split()
            if len(split_line) > 0 and split_line[0] == "import":
                # Check if the module is a third-party package
                module_name = split_line[1]
                if module_name in prohibited_libraries:
                    print("Error: Access to other files is prohibited. Exiting program")
                    quit(0)
                try:
                    # Attempt to import the module to check if it's installed
                    __import__(module_name)
                except ImportError:
                    # If the module is not installed, install it
                    subprocess.run([sys.executable, "-m", "pip", "install", module_name])
                is_python_code = True
            if line == "```":
                break
            if is_python_code:
                try:
                    file.write(line + '\n')
                except Exception as e:
                    print(f"Error writing line to file: {e}")

        file.close()


def add_features(file_name, model):
    while True:
        features_to_add = input("What features would you like to add or make to the program?\n"
                                "Or type 'none' to quit: ")

        if features_to_add.upper() == "NONE":
            break  # Exit the loop when the user types 'none'
        else:
            add_new_features_and_run(model, file_name, features_to_add)


def add_new_features_and_run(model: genai, file_name, features):
    with open("API_KEY", "r") as f:
        api_key = f.read()
    genai.configure(api_key=api_key)

    with open(file_name, "r") as python_file:
        full_code = python_file.read()

    prompt = f"{full_code}\n\n" \
             f"" \
             f"Add the following feature(s):" \
             f"\t{features}"

    response = model.generate_content(prompt)
    response_text = response.text

    write_code_to_file(file_name, response_text)

    # Now run the generated code
    subprocess.run([sys.executable, file_name])
