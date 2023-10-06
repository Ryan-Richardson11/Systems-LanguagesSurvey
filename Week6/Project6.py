import platform, os

def findOS():
    return platform.system()

def isValidPath(OS, path):
    if OS == "Windows":
        if '/' in path:
            path.replace("/", "\")
        else:
            continue
    elif OS == "Darwin":
        if "\" in path:
            path.replace("\", "/")
        else:
            continue
    


def main():
    OS = findOS()
