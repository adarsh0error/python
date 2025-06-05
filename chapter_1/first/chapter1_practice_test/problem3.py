#write a python program to print the contents of a dictionary using the os module 
import os

# Sample dictionary
my_dict = {
    "name": "Adarsh",
    "age": 21,
    "city": "Chennai",
    "profession": "Student"
}

# Clear screen (cross-platform)
os.system('cls' if os.name == 'nt' else 'clear')

# Print dictionary contents
print("Contents of the dictionary:\n")
for key, value in my_dict.items():
    print(f"{key}: {value}")
