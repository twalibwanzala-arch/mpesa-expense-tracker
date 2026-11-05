"""Sorts parsed M-Pesa transactions into spending categories."""

from parser import parse_file

# Keywords to look for in the name of who you paid.
# The first category with a matching keyword wins, so order matters.
KEYWORDS = {
    "Food": ["NAIVAS", "QUICKMART", "CARREFOUR", "CHANDARANA", "SUPERMARKET",
             "RESTAURANT", "CAFE", "JAVA", "KFC", "PIZZA", "BUTCHERY"],
    "Transport": ["UBER", "BOLT", "LITTLE", "MATATU", "SHELL", "RUBIS",
                  "TOTAL", "PARKING", "FUEL"],
    "Utilities": ["KPLC", "KENYA POWER", "WATER", "ZUKU", "WIFI", "DSTV", "GOTV"],
    "Health": ["PHARMACY", "HOSPITAL", "CLINIC", "CHEMIST"],
    "Airtime & Data": ["AIRTIME", "DATA", "BUNDLES"],
}


def categorize(transaction):
    """Return a category name for one parsed transaction."""
    # Money coming in is income, not spending.
    if transaction["type"] == "received":
        return "Income"

    # Airtime messages have no shop name, so the type tells us the category.
    if transaction["type"] == "airtime":
        return "Airtime & Data"

    name = transaction["party"].upper()
    for category, words in KEYWORDS.items():
        if any(word in name for word in words):
            return category

    # Money sent to a person we can't classify further.
    if transaction["type"] == "sent":
        return "Transfers"

    return "Other"


def categorize_all(transactions):
    """Return copies of the transactions with a 'category' field added."""
    return [{**t, "category": categorize(t)} for t in transactions]


if __name__ == "__main__":
    for t in categorize_all(parse_file("sample_messages.txt")):
        print(f"{t['category']:<16} Ksh{t['amount']:>9,.2f}  {t['party']}")
