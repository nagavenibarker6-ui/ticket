def calculate_bill(prices, quantities):
    total = 0
    for p, q in zip(prices, quantities):
        total += p * q
    return total
def booking_type(total_amount):
    if total_amount >= 3000:
        return "Platinum Booking"
    elif 1500 <= total_amount < 3000:
        return "Gold Booking"
    else:
        return "Silver Booking"
if __name__ == "__main__":
    print("Using default booking details")
    prices = [250, 300, 200]
    quantities = [2, 3, 1]
    total = calculate_bill(prices, quantities)
    status = booking_type(total)
    print("\n------ Movie Ticket Booking Summary ------")
    print("Total Amount:", total)
    print("Booking Status:", status) 
