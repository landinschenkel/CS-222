#   Name: Landin Schenkel
#   Assignment: 1
#   Program Name: Loop
#   Date: 08/25/25

target_price = int(input("Enter the target price of your company: "))

while True:
    current_price = float(input("Enter your current stock price: "))

    if current_price >= target_price:
        print("Shares can be sold now")
        break