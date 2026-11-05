from parser import parse_message


def test_paid():
    msg = ("QKL1ABC2XY Confirmed. Ksh500.00 paid to NAIVAS SUPERMARKET. "
           "on 5/11/26 at 2:15 PM. New M-PESA balance is Ksh3,250.00.")
    result = parse_message(msg)
    assert result["type"] == "paid"
    assert result["amount"] == 500.0
    assert result["party"] == "NAIVAS SUPERMARKET"


def test_sent_with_phone_number():
    msg = ("QKL1ABC3XZ Confirmed. Ksh1,200.00 sent to JOHN KAMAU 0712345678 "
           "on 5/11/26 at 6:40 PM. New M-PESA balance is Ksh2,050.00.")
    result = parse_message(msg)
    assert result["type"] == "sent"
    assert result["amount"] == 1200.0
    assert result["party"] == "JOHN KAMAU"


def test_received():
    msg = ("QKL1ABC4XA Confirmed. You have received Ksh5,000.00 from JANE WANJIKU "
           "0722345678 on 4/11/26 at 9:05 AM. New M-PESA balance is Ksh7,050.00.")
    result = parse_message(msg)
    assert result["type"] == "received"
    assert result["party"] == "JANE WANJIKU"


def test_airtime():
    msg = ("QKL1ABC5XB Confirmed. You bought Ksh50.00 of airtime "
           "on 5/11/26 at 8:00 AM. New M-PESA balance is Ksh2,000.00.")
    assert parse_message(msg)["type"] == "airtime"


def test_unknown_message_returns_none():
    assert parse_message("Hello, this is not an M-Pesa message") is None
