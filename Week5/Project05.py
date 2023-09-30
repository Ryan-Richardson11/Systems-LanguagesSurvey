import os
import random

def generateNumbers():
    randNums = []
    for i in range(0, 100):
        randNums.append(str(random.randint(0, 1000)))
    return "\n".join(randNums)

# def createFolder(folder):
#     if os.path.exists(folder):
#         os.rmdir(folder)
#     os.mkdir(folder)

def createFolder(folder):
    if os.listdir(folder):
        for file in os.listdir(folder):
            os.remove(file)
        os.rmdir(folder)
    os.mkdir(folder)

def createFile(numbers,folder, file):
    with open(os.path.join(folder, file), "w") as newFile:
        newFile.write(numbers)
    newFile.close()

# C:\Users\Ryan\Desktop\System+Languages\Week5\Test
# Test.txt
def main():
    folder = input("Enter the folder name: ")
    createFolder(folder)
    file = input("Enter the file name: ")
    numbers = generateNumbers()
    createFile(numbers, folder, file)

main()