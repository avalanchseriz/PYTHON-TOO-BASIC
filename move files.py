import os

source = "folder"
destination = "C:\\Users\\abhin\\OneDrive\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("there is already a file there")

    else:
        os.replace(source, destination)
        print(source+" was moved")

except FileNotFoundError:
    print("file not found")