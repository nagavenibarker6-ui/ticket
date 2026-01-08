import sys
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
def main():
    if len(sys.argv) > 4:
        customer_name = sys.argv[1]
        movie_name = sys.argv[2]
        prices = list(map(int, sys.argv[3].split(",")))
        quantities = list(map(int, sys.argv[4].split(",")))
        print("User provided booking details")
    else:
        customer_name = "Nagaveni"
        movie_name = "toxic"
        prices = [250, 300, 200]
        quantities = [2, 3, 1]
        print("Using default booking details")
    total_tickets = sum(quantities)
    total_amount = calculate_bill(prices, quantities)
    status = booking_type(total_amount)
    print("\n------ Movie Ticket Booking Summary ------")
    print("Customer Name:", customer_name)
    print("Movie Name:", movie_name)
    print("Ticket Prices:", prices)
    print("Ticket Quantities:", quantities)
    print("Total Tickets:", total_tickets)
    print("Total Amount:", total_amount)
    print("Booking Status:", status)
if __name__ == "__main__":
    main()
