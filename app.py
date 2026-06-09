users = []

def show_menu():
    print("\n=== User Management System ===")
    print("1. View Users")
    print("2. Exit")

def login(username):
    print(f"{username} logged in successfully.")

while True:
    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":
        if not users:
            print("No users found.")
        else:
            for user in users:
                print(user)

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

   