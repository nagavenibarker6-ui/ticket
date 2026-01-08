from main import calculate_bill, booking_type
def test_calculate_bill_multiple_items():
    prices = [250, 300, 200]
    quantities = [2, 3, 1]
    assert calculate_bill(prices, quantities) == 1650
def test_calculate_bill_single_item():
    assert calculate_bill([500], [4]) == 2000
def test_calculate_bill_empty():
    assert calculate_bill([], []) == 0
def test_booking_type_platinum():
    assert booking_type(3000) == "Platinum Booking"
def test_booking_type_gold():
    assert booking_type(2000) == "Gold Booking"
def test_booking_type_silver():
    assert booking_type(1000) == "Silver Booking"
