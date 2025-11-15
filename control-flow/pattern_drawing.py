# user_input = int(input("Enter the size of the pattern: "))

# i = 1

# while user_input <= 0:
#     print("*" * user_input)
#     i += 1




# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the input is positive
while size <= 0:
    size = int(input("Please enter a positive integer: "))

# Initialize row counter
row = 0

# Outer loop for each row
while row < size:
    # Inner loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing the row
    print()
    row += 1
