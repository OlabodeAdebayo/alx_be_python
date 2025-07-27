def display_menu():
    print(f"Shopping List Manager")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")

def main():
    shopping_list = []
    while True: 
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            #Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            #Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"Item '{item}' not found in the shopping list.")
        elif choice == '3':
            #Display the shopping list
            item = ", ".join(shopping_list)
            if shopping_list:
                print(f"Shopping List:", item)
            else:
                print(f"Your shopping list is empty.")
        elif choice == '4':
            print(f"Goodbye!")
            break
        else:
            print(f"Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
