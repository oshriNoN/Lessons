#This is a test file to test the file handling in python
import os

# open the file in write mode
with open("/home/oshkosh/Documents/test.txt", "w") as file:
    file.write("Hello World")
    file.close()

# open the file in append mode 
try:
    with open("/home/oshkosh/Documents/test.txt", "a") as file:
        file.write("\nHello World!!!!!")
        file.close()
except FileNotFoundError as e:
    print("File not found to append", e)
    ## do something

# open the file in read mode and read the content 
try:
    with open("/home/oshkosh/Documents/test.txt", "r") as file:
        f = (file.read())
        file.close()
        print(f)
except FileNotFoundError as e:
    print("File not found to read", e)
    ## do something

# Just open the file without reading or writing
try:
    with open("/home/oshkosh/Documents/test.txt", "x") as file:
        file.close()
except FileExistsError as e:
    print("File already exists", e)

# delete the file - using os module:
try:
    os.remove("/home/oshkosh/Documents/test.txt")
    print("File deleted")
except FileNotFoundError as e:
    print("File not found to delete", e)