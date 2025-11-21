def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def display_shopping_list (shopping_list):
    print(f"Here are the items in your shopping list: {shopping_list}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item not in shopping_list:
                print("Item not in the list, try again")
            else:
                shopping_list.remove(item)
            pass
        elif choice == '3':
            # Display the shopping list
            display_shopping_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()