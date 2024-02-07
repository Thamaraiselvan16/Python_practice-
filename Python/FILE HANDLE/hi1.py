import os
folder_name = input("Enter the folder name:")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
file_names = [input("Enter the file name to create:")]
for file_name in file_names:
    with open(os.path.join(folder_name, file_name), 'w') as file:
        file.write(f"This is {file_name}.")

print(f"Folder '{folder_name}' and text files created successfully.")

f=open(file_name,"w")
f.write(input("enter the content:"))
f.close()

f=open(file_name,"r")
print(f.read())