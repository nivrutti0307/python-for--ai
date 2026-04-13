def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python programming.")
greet("Nivrtti")

def check_weather(temperature):
    # temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather(35)

def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
# print(price)  # NameError: name 'price' is not defined

discount_rate = 0.15  # Global variable

def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return (price - discount)
result = apply_discount(100)
print(result)  # 85.0

counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2

# Bad - using global variable
total = 0

def add_to_total(amount):
    global total
    total += amount
add_to_total(10)
print(total)  # 10

# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

# Call with values
introduce("Alice", 25)
introduce("Bob", 30)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Use default
greet("Alice")           # Hello, Alice!

# Override default
greet("Bob", "Hi")       # Hi, Bob!
greet("Charlie", "Hey")  # Hey, Charlie!

# Wrong - don't use lists as defaults
def add_item(item, list=[]):
    list.append(item)
    return list
add_item(1)  # [1]
add_item(2)  # [1, 2] - unexpected! 
print(add_item(4))
#Right - use None and create new list
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
add_item(4)  # [4]
add_item(5)  # [5]  
add_item(6)  # [6]
print(add_item(7))  # [7]


def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)