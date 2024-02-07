import os
folder_name = input("Enter the folder name you want to create: ")
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

file_name = input("Enter the name of the file you want to create: ")
file_path = os.path.join(folder_name, file_name)

with open(file_path, 'w') as file:
    file.write("This is the content of the file.")

print(f"File '{file_name}' created inside '{folder_name}'.")