# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

