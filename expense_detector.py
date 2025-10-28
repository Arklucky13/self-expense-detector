import csv
from collections import defaultdict

# Define simple keyword categories
CATEGORIES = {
    "food": ["restaurant", "burger", "pizza", "coffee", "groceries"],
    "transport": ["uber", "taxi", "bus", "train", "flight", "fuel"],
    "entertainment": ["movie", "netflix", "game", "concert"],
    "bills": ["electricity", "water", "rent", "internet", "phone"],
    "shopping": ["clothes", "amazon", "mall", "store"]
}

def detect_category(description):
    description = description.lower()
    for category, keywords in CATEGORIES.items():
        if any(word in description for word in keywords):
            return category
    return "other"

def analyze_expenses(file_path):
    summary = defaultdict(float)

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row['amount'])
            description = row['description']
            category = detect_category(description)
            summary[category] += amount

    print("\nExpense Summary by Category:")
    for cat, total in summary.items():
        print(f"{cat.title()}: ${total:.2f}")

if __name__ == "__main__":
    print("💰 Expense Detector 💰")
    print("Make sure your CSV file has columns: description, amount")
    file_path = input("Enter path to your expense CSV file: ")
    analyze_expenses(file_path)
