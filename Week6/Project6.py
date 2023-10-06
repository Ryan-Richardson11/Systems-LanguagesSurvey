import platform, os

def findOS():
    return platform.system()

def checkPath(OS, path):
    if OS == "Windows":
        if '/' in path:
            path.replace("/", "\\")
        return path
    elif OS == "Darwin":
        if "\\" in path:
            path.replace("\\", "/")
        return path
    return path

def main():
    OS = findOS()
    path = str(input("Enter a the path to your file: "))
    checkPath(OS, path)

    if os.path.exists(path):
        print(os.path.basename(path))
    else:
        print("The path is not recognized.")

main()

