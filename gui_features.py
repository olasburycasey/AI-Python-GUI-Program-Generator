import subprocess
import sys
from safe_code_scanner import SafeCodeScanner

import google.generativeai as genai


def write_code_to_file(file_name, code):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(code)


def clean_up_response(response_text: str) -> str:
    prohibited_libraries = {"os", "sys", "subprocess", "shutil", "socket", "requests", "http.client", "urllib",
                            "ftplib", "ctypes", "cffi", "pickle", "eval", "exec", "compile",
                            "multiprocessing", "threading", "pathlib", "glob"}

    python_code_lines = []
    is_python_code = False

    for line in response_text.splitlines():

        # Start extracting code after triple backticks
        if line.startswith("```python") or line.startswith("```py"):
            is_python_code = True
            continue
        elif line.startswith("```") and is_python_code:
            break  # End of code block

        if is_python_code:
            # Check for prohibited libraries
            split_line = line.split()
            '''if len(split_line) >= 2 and split_line[0] == "import":
                module_name = split_line[1]
                if module_name.split('.')[0] in prohibited_libraries:
                    raise ValueError(f"Error: Use of prohibited module '{module_name}' detected.")

            if len(split_line) >= 4 and split_line[0] == "from" and split_line[2] == "import":
                module_name = split_line[1]
                if module_name.split('.')[0] in prohibited_libraries:
                    raise ValueError(f"Error: Use of prohibited module '{module_name}' detected.")'''

            python_code_lines.append(line)

    # Return the cleaned-up Python code as a single string
    return "\n".join(python_code_lines)


def add_features(file_name, model):
    while True:
        features_to_add = input("What features would you like to add or make to the program?\n"
                                "Or type 'none' to quit: ")
        if features_to_add.upper() == "NONE":
            break  # Exit the loop when the user types 'none'
        else:
            add_new_features_and_run(model, file_name, features_to_add)


def add_new_features_and_run(model, file_name, features):
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

    print(response_text)
    clean_response = clean_up_response(response_text)
    print("---CLEAN CODE---")
    print(clean_response)

    if clean_response != "":
        confirmation = input("\nDo you want to run this newly generated code? (yes/no): ").lower()
        if confirmation == 'yes':
            write_code_to_file(file_name, clean_response)
            print(f"Running {file_name} safely in a subprocess...")
            run_if_safe(file_name)
        else:
            print("Skipping execution.")
    else:
        print("Error updating code.")


def run_if_safe(file_path):
    scanner = SafeCodeScanner(file_path)
    if scanner.scan():
        print("✅ Code appears safe. Running...")
        subprocess.run([sys.executable, file_path])
    else:
        print("🚫 Execution blocked: Unsafe code detected.")
