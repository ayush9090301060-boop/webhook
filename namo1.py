import json
import os

DATA_FILE = "app_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": [], "expenses": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task(data):
    title = input("Enter task title: ").strip()
    if title:
        data["tasks"].append({"title": title, "status": "Pending"})
        print(f"✔️ Task '{title}' added.")

def list_tasks(data):
    if not data["tasks"]:
        print("📭 No tasks found.")
        return
    for idx, task in enumerate(data["tasks"], 1):
        print(f"{idx}. [{task['status']}] {task['title']}")

def complete_task(data):
    list_tasks(data)
    if data["tasks"]:
        try:
            choice = int(input("Enter task number to complete: ")) - 1
            if 0 <= choice < len(data["tasks"]):
                data["tasks"][choice]["status"] = "Completed"
                print("🎉 Task marked as completed!")
            else:
                print("❌ Invalid number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def add_expense(data):
    item = input("Enter expense item: ").strip()
    try:
        amount = float(input("Enter amount ($): "))
        data["expenses"].append({"item": item, "amount": amount})
        print(f"💰 Logged ${amount:.2f} for {item}.")
    except ValueError:
        print("❌ Invalid amount format.")

def show_summary(data):
    print("\n--- 📊 APPLICATION SUMMARY ---")
    total_tasks = len(data["tasks"])
    done_tasks = sum(1 for t in data["tasks"] if t["status"] == "Completed")
    print(f"📋 Tasks: {done_tasks}/{total_tasks} completed.")
    
    total_spend = sum(e["amount"] for e in data["expenses"])
    print(f"💵 Total Expenses: ${total_spend:.2f}")
    if data["expenses"]:
        print("Recent Expenses:")
        for e in data["expenses"][-3:]:
            print(f"  - {e['item']}: ${e['amount']:.2f}")

def main():
    data = load_data()
    while True:
        print("\n=== 🎯 MINI-DASHBOARD ===")
        print("1. Add Task\n2. View Tasks\n3. Complete Task")
        print("4. Add Expense\n5. View Summary\n6. Exit")
        choice = input("Choimport json
import os

DATA_FILE = "app_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": [], "expenses": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task(data):
    title = input("Enter task title: ").strip()
    if title:
        data["tasks"].append({"title": title, "status": "Pending"})
        print(f"✔️ Task '{title}' added.")

def list_tasks(data):
    if not data["tasks"]:
        print("📭 No tasks found.")
        return
    for idx, task in enumerate(data["tasks"], 1):
        print(f"{idx}. [{task['status']}] {task['title']}")

def complete_task(data):
    list_tasks(data)
    if data["tasks"]:
        try:
            choice = int(input("Enter task number to complete: ")) - 1
            if 0 <= choice < len(data["tasks"]):
                data["tasks"][choice]["status"] = "Completed"
                print("🎉 Task marked as completed!")
            else:
                print("❌ Invalid number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def add_expense(data):
    item = input("Enter expense item: ").strip()
    try:
        amount = float(input("Enter amount ($): "))
        data["expenses"].append({"item": item, "amount": amount})
        print(f"💰 Logged ${amount:.2f} for {item}.")
    except ValueError:
        print("❌ Invalid amount format.")

def show_summary(data):
    print("\n--- 📊 APPLICATION SUMMARY ---")
    total_tasks = len(data["tasks"])
    done_tasks = sum(1 for t in data["tasks"] if t["status"] == "Completed")
    print(f"📋 Tasks: {done_tasks}/{total_tasks} completed.")
    
    total_spend = sum(e["amount"] for e in data["expenses"])
    print(f"💵 Total Expenses: ${total_spend:.2f}")
    if data["expenses"]:
        print("Recent Expenses:")
        for e in data["expenses"][-3:]:
            print(f"  - {e['item']}: ${e['amount']:.2f}")

def main():
    data = load_data()
    while True:
        print("\n=== 🎯 MINI-DASHBOARD ===")
        print("1. Add Task\n2. View Tasks\n3. Complete Task")
        print("4. Add Expense\n5. View Summary\n6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task(data)
        elif choice == "2":
            list_tasks(data)
        elif choice == "3":
            complete_task(data)
        elif choice == "4":
            add_expense(data)
        elif choice == "5":
            show_summary(data)
        elif choice == "6":
            save_data(data)
            print("💾 Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please pick 1-6.")

if __name__ == "__main__":
    main()
ose an option (1-6): ").strip()

        if choice == "1":
            add_task(data)
        elif choice == "2":
            list_tasks(data)
        elif choice == "3":
            complete_task(data)
        elif choice == "4":
            add_expense(data)
        elif choice == "5":
            show_summary(data)
        elif choice == "6":
            save_data(data)
            print("💾 Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please pick 1-6.")

if __name__ == "__main__":
    main()
