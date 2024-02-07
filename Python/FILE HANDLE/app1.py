import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            print(f"Data has been written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def append_to_file(file_path, data):
    try:
        with open(file_path, 'a') as file:
            file.write(data)
            print(f"Data has been appended to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Define file path
file_path = input("Enter the file name: ")

# Check if the file exists before reading or writing
if os.path.exists(file_path):
    # Read the file
    file_contents = read_file(file_path)
    if file_contents:
        print("File contents:")
        print(file_contents)
else:
    print(f"The file '{file_path}' does not exist. Creating it...")

    # Get the data to write to the file from user input
    initial_data = input("Enter the initial data: ")
    write_file(file_path, initial_data)

    # Read the newly created file
    file_contents = read_file(file_path)
    if file_contents:
        print("File contents:")
        print(file_contents)

# Get the new data to append to the file from user input
new_data = input("Enter the data to append: ")
append_to_file(file_path, new_data)

# Read the file again to see the appended data
file_contents = read_file(file_path)
if file_contents:
    print("Updated file contents:")
    print(file_contents)
