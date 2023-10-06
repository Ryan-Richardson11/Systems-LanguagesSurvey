import platform, os

def findOS():
    return platform.system()

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
    mypath = str(input("Enter a the path to your file: "))
    path = checkPath(OS, mypath)

    if os.path.exists():
        print(os.path.basename(path))
    else:
        print("The path is not recognized.")

main()

