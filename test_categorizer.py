from categorizer import categorize, categorize_all


def make(kind, party):
    """Build a small fake transaction for testing."""
    return {"type": kind, "party": party, "amount": 100.0}


def test_supermarket_is_food():
    assert categorize(make("paid", "NAIVAS SUPERMARKET")) == "Food"


def test_uber_is_transport():
    assert categorize(make("paid", "UBER TRIP")) == "Transport"


def test_received_is_income():
    assert categorize(make("received", "JANE WANJIKU")) == "Income"


def test_airtime():
    assert categorize(make("airtime", "Safaricom Airtime")) == "Airtime & Data"


def test_sent_to_person_is_transfer():
    assert categorize(make("sent", "JOHN KAMAU")) == "Transfers"


def test_unknown_shop_is_other():
    assert categorize(make("paid", "RANDOM SHOP")) == "Other"


def test_categorize_all_adds_field():
    result = categorize_all([make("paid", "KPLC PREPAID")])
    assert result[0]["category"] == "Utilities"
