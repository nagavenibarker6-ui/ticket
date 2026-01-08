from main import calculate_bill, booking_type
def test_calculate_bill():
    assert calculate_bill([250, 300, 200], [2, 3, 1]) == 1650
def test_booking_type():
    assert booking_type(1600) == "Gold Booking"
