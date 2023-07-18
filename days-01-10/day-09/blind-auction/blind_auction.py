import os

print("Welcome to the secret auction program")

def find_highest_bidder(all_bids):
    highest_bid = 0
    winner = ""
    for bid_name in all_bids:
        bid_price = all_bids[bid_name]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bid_name
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
other_bidders = True

while other_bidders:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bids == 'yes':
        os.system("clear")
    else:
        other_bidders = False
        find_highest_bidder(bids)
