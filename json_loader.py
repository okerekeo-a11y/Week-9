"""
Ogechukwu Okereke
CSMCS 111
Week 9 assignment3
"""
import json

try:
    with open("data.json", "r") as file:
        data = json.load(file)
    print("JSON loaded successfully.")

except json.JSONDecodeError:
    print("Invalid JSON format!")

except FileNotFoundError:
    print("File not found!")