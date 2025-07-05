from . interface import heading
def fileExist(name):
    try:
        with open(name, 'r'):
            return print("File found successfully")
    except FileNotFoundError:
        return print("File does not exist.")

def fileCreate(name):
    try:
        with open(name, 'w'):
            return print(f"File {name} created successfully.")
    except FileExistsError:
        print(f"File {name} already exists.")

def readFile(name):
    try:
        with open(name, 'r') as record:
            heading("PEOPLE RECORDED")
            print(record.read())
    except (FileNotFoundError, OSError):
        print(f"There was an error trying to read the file.")

def record(file, name, age):
    try:
        with open(file, 'a') as record:
            record.write(f"Name: {name:<25} Age: {age:<10}\n")
    except (FileExistsError, OSError):
        print("Unable to log data to non-existent files.")
