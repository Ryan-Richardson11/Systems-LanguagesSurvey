import platform, os

# Function returns the current systems platform
def findOS():
    return platform.system()

#Checks the path using the findOS function and an inputed path.
# Switches the format to match the OS running. 
def checkPath(OS, path):
    if OS == "Windows":
        if '/' in path:
            path = path.replace("/", "\\")
        return path
    elif OS == "Darwin":
        if "\\" in path:
            path = path.replace("\\", "/")
        return path
    return path


def main():
    OS = findOS()
    mypath = input("Enter a the path to your file: ")
    path = checkPath(OS, mypath)

    # If the inputed path exists, prints out the base file name.
    if os.path.exists(path):
        print(os.path.basename(path))
    else:
        print("The path is not recognized.")

main()

# Test Windows:
# C:\\Users\\Ryan\\OneDrive\\Desktop\\AdvancedAlgorithms\\Week1\\Project1.py

# Test MacOS:
# C:/Users/Ryan/OneDrive/Desktop/AdvancedAlgorithms/Week1/Project1.py

