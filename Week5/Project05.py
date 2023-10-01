import os
import random

# Generates 100 random numbers between 0 and 1000 then returns one per line.
def generateNumbers():
    randNums = []
    for i in range(0, 100):
        randNums.append(str(random.randint(0, 1000)))
    return "\n".join(randNums)

# Checks if the folder exists, if it does all files and folder are deleted then recreated.
# If the file does not exist, it is then created.
def createFolder(folder):
    if os.path.exists(folder):
        for file in os.listdir(folder):
            filePath = os.path.join(folder, file)
            os.remove(filePath)
        os.rmdir(folder)
    
    os.mkdir(folder)

# Creates new file with the inputed path and writes the numbers in generateNumbers()
def createFile(numbers, folder, file):
    with open(os.path.join(folder, file), "w") as newFile:
        newFile.write(numbers)

# Asks for user inputs to pass as parameters along with generated numbers then creates the folder and file.
def main():
    folder = input("Enter the folder name: ")
    createFolder(folder)
    file = input("Enter the file name: ")
    numbers = generateNumbers()
    createFile(numbers, folder, file)

main()

# C:\Users\Ryan\OneDrive\Desktop\SystemsLanguages\Week5\test
# test.txt