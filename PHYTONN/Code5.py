import os
import sys

# File processing function
def process_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a file.")
        return

    output_file = os.path.splitext(file_path)[0] + "_output.txt"
    with open(file_path, 'r') as f:
        lines = f.readlines()

    processed_lines = 0
    with open(output_file, 'w') as f:
        for line in lines:
            # Take the number in the line as it is and append "-10"
            f.write(line.strip() + "-10\n")  # Append "-10" and write
            processed_lines += 1
    
    print(f"{file_path} has been processed. A total of {processed_lines} lines were processed.")

# Directory processing function
def process_directory(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory.")
        return

    files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".txt")]

    for file_name in files:
        output_file = os.path.splitext(file_name)[0] + "_output.txt"
        with open(file_name, 'r') as f:
            lines = f.readlines()

        processed_lines = 0
        with open(output_file, 'w') as f:
            for line in lines:
                # Take the number in the line as it is and append "-10"
                f.write(line.strip() + "-10\n")  # Append "-10" and write
                processed_lines += 1

        print(f"{file_name} has been processed. A total of {processed_lines} lines were processed.")

# User notification
def user_notification():
    print("Usage: py sourcecode.py <Input_files(D or F)> <Last_suffix>")

# File check function
def file_check(file_path):
    if os.path.exists(file_path):
        print(f"{file_path} file exists.")
    else:
        print(f"{file_path} file not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        user_notification()
    else:
        option = sys.argv[1]
        path = sys.argv[2]
        if option == "F":
            file_check(path)
            process_file(path)
        elif option == "D":
            file_check(path)
            process_directory(path)
        else:
            print("Invalid option. It must be 'F' or 'D'")

