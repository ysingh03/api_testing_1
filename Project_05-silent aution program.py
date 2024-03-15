import os
def find_bid_winner(bidder_data):
    higest_bid = 0
    winner = ''
    for bidder in bidder_data:
        bidding_price = bidder_data[bidder]
        if bidding_price > higest_bid:
            higest_bid = bidding_price
            winner = bidder
    print(f"the winner of the bidding is {winner} with the price of {higest_bid} ")

bidders_data = {}
end_of_bidding = False
while not end_of_bidding:
    names = input("What is your name? :\n")
    bid = int(input("What is your bid? :\n"))
    bidders_data[names] = bid
    bidders = input("Is there any other bidders? Type 'yes' or 'no'\n").lower()

    if bidders == 'no':
        end_of_bidding = True
        find_bid_winner(bidders_data)
    elif bidders == 'yes':
        os.system("cls")

