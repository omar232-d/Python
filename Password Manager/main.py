import json
import os

FILE_NAME = "passwords.json"

# Load existing data
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add new password
def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data = load_data()

    data[website] = {
        "username": username,
        "password": password
    }

    save_data(data)
    print("✅ Password saved!")

# View passwords
def view_passwords():
    data = load_data()

    if not data:
        print("No passwords saved.")
        return

    for website, info in data.items():
        print(f"\nWebsite: {website}")
        print(f"Username: {info['username']}")
        print(f"Password: {info['password']}")

# Main menu
def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()