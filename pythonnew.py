import json
import os
from datetime import datetime

class TrackerApp:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = {"tasks": [], "expenses": []}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.data = json.load(f)
            except json.JSONDecodeError:
                print("Error reading data file. Starting fresh.")

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_task(self, title):
        task = {"id": len(self.data["tasks"]) + 1, "title": title, "done": False}
        self.data["tasks"].append(task)
        self.save_data()
        print(f"Task '{title}' added successfully!")

    def list_tasks(self):
        if not self.data["tasks"]:
            print("No tasks found.")
            return
        for t in self.data["tasks"]:
            status = "✅" if t["done"] else "❌"
            print(f"[{t['id']}] {t['title']} - Done: {status}")

    def complete_task(self, task_id):
        for t in self.data["tasks"]:
            if t["id"] == task_id:
                t["done"] = True
                self.save_data()
                print(f"Task {task_id} marked as complete.")
                return
        print("Task ID not found.")

    def add_expense(self, description, amount):
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "description": description,
            "amount": float(amount)
        }
        self.data["expenses"].append(expense)
        self.save_data()
        print(f"Added expense: {description} (${amount:.2f})")

    def view_expenses(self):
        if not self.data["expenses"]:
            print("No expenses recorded.")
            return
        total = sum(e["amount"] for e in self.data["expenses"])
        for e in self.data["expenses"]:
            print(f"{e['date']} | {e['description']}: ${e['amount']:.2f}")
        print(f"Total Expenditure: ${total:.2f}")

def main():
    app = TrackerApp()
    while True:
        print("\n=== SYSTEM MENU ===")
        print("1. Add Task        2. List Tasks       3. Complete Task")
        print("4. Add Expense     5. View Expenses    6. Exit")
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            if title: app.add_task(title)
        elif choice == "2":
            print("\n--- Current Tasks ---")
            app.list_tasks()
        elif choice == "3":
            try:
                tid = int(input("Enter Task ID to complete: "))
                app.complete_task(tid)
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "4":
            desc = input("Enter expense description: ").strip()
            try:
                amt = float(input("Enter amount ($): "))
                if desc and amt >= 0: app.add_expense(desc, amt)
            except ValueError:
                print("Invalid amount numeric format.")
        elif choice == "5":
            print("\n--- Expense Log ---")
            app.view_expenses()
        elif choice == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-6.")

if __name__ == "__main__":
    main()
