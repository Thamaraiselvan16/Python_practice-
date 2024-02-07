import os

# Specify the folder name
folder_name = "my_folder"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create text files inside the folder
for i in range(1, 6):  # Creating 5 text files
    file_name = f"{folder_name}/text_file_{i}.txt"
    with open(file_name, 'w') as file:
        file.write(f"This is text file {i}.")

print(f"Folder '{folder_name}' and text files created successfully.")
