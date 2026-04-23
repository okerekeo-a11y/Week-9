"""
Ogechukwu Okereke
CSMCS 111
Week 9 assignment1
"""
try:
    file = open("missing_file.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found!")

