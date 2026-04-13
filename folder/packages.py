# Pattern 1: Import the whole module
import math
print(math.sqrt(16))

# Pattern 2: Import specific items from a module
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])
print(f"Random number: {number}")
print(f"Random choice: {choice}")

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data,indent=4)  # Pretty print with indentation
print(json_string)

# # Web requests
# import requests

# response = requests.get("https://api.example.com/data")
# data = response.json()
# print(data)

