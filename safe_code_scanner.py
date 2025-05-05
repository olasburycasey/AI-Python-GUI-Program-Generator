import ast


class SafeCodeScanner:
    """
    Analyzes Python source code to detect potentially dangerous operations.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.forbidden_imports = {
            "os", "sys", "subprocess", "shutil", "socket", "requests", "pickle"
        }
        self.forbidden_calls = {
            "eval", "exec", "__import__", "open", "compile", "input"
        }

    def scan(self):
        """
        Scans the file for dangerous imports and function calls.
        Returns True if code is safe, False if unsafe code is detected.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

            for node in ast.walk(tree):
                # Scan for bad imports
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.split('.')[0] in self.forbidden_imports:
                            print(f"⚠️ Unsafe import detected: {alias.name}")
                            return False

                elif isinstance(node, ast.ImportFrom):
                    if node.module and node.module.split('.')[0] in self.forbidden_imports:
                        print(f"⚠️ Unsafe import detected: from {node.module}")
                        return False

                # Scan for bad function calls
                elif isinstance(node, ast.Call):
                    func = node.func
                    if isinstance(func, ast.Name) and func.id in self.forbidden_calls:
                        print(f"⚠️ Unsafe function call detected: {func.id}()")
                        return False

            return True  # No dangerous code found

        except Exception as e:
            print(f"Error during scan: {e}")
            return False

    def scan_source(self, source_code: str):
        """
        Scans raw Python source code (as a string) for dangerous imports and function calls.
        Returns True if code is safe, False otherwise.
        """
        try:
            tree = ast.parse(source_code)

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.split('.')[0] in self.forbidden_imports:
                            print(f"⚠️ Unsafe import detected: {alias.name}")
                            return False

                elif isinstance(node, ast.ImportFrom):
                    if node.module and node.module.split('.')[0] in self.forbidden_imports:
                        print(f"⚠️ Unsafe import detected: from {node.module}")
                        return False

                elif isinstance(node, ast.Call):
                    func = node.func
                    if isinstance(func, ast.Name) and func.id in self.forbidden_calls:
                        print(f"⚠️ Unsafe function call detected: {func.id}()")
                        return False

            return True
        except Exception as e:
            print(f"Error during source scan: {e}")
            return False
