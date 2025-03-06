import os
import subprocess


def validate_exe(file_path):
    """
    This function checks if the .exe file exists and executes correctly.

    Args:
        file_path (str): The path to the .exe file to be validated.

    Returns:
        bool: True if the .exe file exists and executes correctly, False otherwise.
    """
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return False

    try:
        # Execute the .exe file and capture the output
        result = subprocess.run([file_path], capture_output=True, text=True)

        if result.returncode == 0:
            print("Execution successful!")
            print("Output:")
            print(result.stdout)
            return True
        else:
            print("Execution failed!")
            print("Error Output:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"An error occurred while executing the file: {e}")
        return False


# Example usage
exe_file_path = "dist\\main.exe"
if validate_exe(exe_file_path):
    print("Validation successful: The .exe file was created and executed correctly.")
else:
    print("Validation failed: There was an issue with the .exe file.")
