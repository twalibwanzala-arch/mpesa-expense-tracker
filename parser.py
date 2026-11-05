"""Turns M-Pesa SMS messages into structured data.

All sample messages in this project are FAKE. Never commit real transactions.
"""

import re

# Pieces we reuse inside the patterns below.
AMOUNT = r"Ksh([\d,]+\.\d{2})"             # e.g. Ksh1,200.00
DATE_TIME = r"on (\d{1,2}/\d{1,2}/\d{2,4}) at (\d{1,2}:\d{2} [AP]M)"
PHONE = r"(?:\s+\d{10})?"                   # optional 10-digit phone number

# One pattern per kind of message. Each captures: amount, [party], date, time.
PATTERNS = {
    "received": re.compile(
        rf"You have received {AMOUNT} from (.+?){PHONE}\s+{DATE_TIME}"
    ),
    "paid": re.compile(rf"{AMOUNT} paid to (.+?)\.?\s+{DATE_TIME}"),
    "sent": re.compile(rf"{AMOUNT} sent to (.+?){PHONE}\s+{DATE_TIME}"),
    "airtime": re.compile(rf"You bought {AMOUNT} of airtime {DATE_TIME}"),
}


def to_number(text):
    """'1,200.00' -> 1200.0"""
    return float(text.replace(",", ""))


def parse_message(message):
    """Read one M-Pesa message and return a dictionary, or None if unrecognised."""
    code_match = re.match(r"^([A-Z0-9]{10})\s+Confirmed", message.strip())
    if not code_match:
        return None

    for kind, pattern in PATTERNS.items():
        match = pattern.search(message)
        if match:
            groups = match.groups()
            if kind == "airtime":
                amount, date, time = groups
                party = "Safaricom Airtime"
            else:
                amount, party, date, time = groups
            return {
                "code": code_match.group(1),
                "type": kind,
                "amount": to_number(amount),
                "party": party.strip(),
                "date": date,
                "time": time,
            }
    return None


def parse_file(path):
    """Parse every line of a text file, skipping lines we can't understand."""
    results = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                parsed = parse_message(line)
                if parsed:
                    results.append(parsed)
    return results


if __name__ == "__main__":
    for transaction in parse_file("sample_messages.txt"):
        print(transaction)
