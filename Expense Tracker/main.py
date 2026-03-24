import json
import os
import matplotlib.pyplot as plt

FILE = "expenses.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense():
    name = input("Enter type (food, salary, etc): ")
    amount = float(input("Enter amount: "))
    
    data = load_data()
    data.append({"name": name, "amount": amount})
    
    save_data(data)
    print("✅ Saved!")

def show_summary():
    data = load_data()
    total = sum(item["amount"] for item in data)
    print(f"Total balance: {total}")

def show_chart():
    data = load_data()
    
    categories = {}
    for item in data:
        categories[item["name"]] = categories.get(item["name"], 0) + item["amount"]

    plt.bar(categories.keys(), categories.values())
    plt.title("Expenses Chart")
    plt.show()

def main():
    while True:
        print("\n1. Add\n2. Summary\n3. Chart\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            break

main()