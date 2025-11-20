# user_input = int(input("Enter the size of the pattern: "))

# i = 1

# while user_input <= 0:
#     print("*" * user_input)
#     i += 1





size = int(input("Enter the size of the pattern: "))


while size <= 0:
    size = int(input("Please enter a positive integer: "))

row = 0


while row < size:
    
    for col in range(size):
        print("*", end="")
   
    print()
    row += 1
 