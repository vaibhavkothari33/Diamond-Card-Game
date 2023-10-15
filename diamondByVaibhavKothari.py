import random

diamonds = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
lowest_cards = ['2', '3']
low_cards = ['4', '5', '6', '7', '8', '9', '10', 'Jack']
high_cards = ['Queen', 'King', 'Ace']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
bot_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
player_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def show_diamond(diamonds):
    diamond = random.choice(diamonds)
    diamonds.remove(diamond)
    return card_values[diamond]

def bot_bidding(diamond, bot_cards):
    if diamond > 12:
        bot_bid = random.choice(lowest_cards)
        lowest_cards.remove(bot_bid)
    elif diamond > 9:
        bot_bid = random.choice(high_cards)
        high_cards.remove(bot_bid)
    else:
        bot_bid = random.choice(low_cards)
        low_cards.remove(bot_bid)
    bot_cards.remove(bot_bid)
    return bot_bid

def valid_card(player_cards, player_bid):
    return player_bid in player_cards

# When playing the for time I am placing alot of Invalid bid so 
# adding a function to dispaly the remaining cards 

def display_player_cards(player_cards):
    print("Your remaining cards:")
    for card in player_cards:
        print(card, end=" ")
    print("\n")

computer_diamonds, player_diamonds = 0, 0

def score(bot, user, diamond, player_diamonds, computer_diamonds):
    bot_bid = card_values[bot]
    user_bid = card_values[user]
    if bot_bid == user_bid:
        player_diamonds += diamond / 2
        computer_diamonds += diamond / 2
    elif bot_bid > user_bid:
        computer_diamonds += diamond
    else:
        player_diamonds += diamond
    return player_diamonds, computer_diamonds

def play_game():
    ps, cs = 0, 0
    print()
    print("Welcome to the Diamond Bidding Game!")
    print("In this game, you and the bot will take turns bidding on diamond cards.")
    print("Your goal is to win as many rounds as possible and outscore the bot.")
    print("You can only bid on the cards you currently hold.")
    print("Let's get started!")
    print()
    for i in range(1, 14):
        print("Round", i)
        diamond = show_diamond(diamonds)
        print('Diamond card:', ''.join([i for i in card_values if card_values[i] == diamond]))

        bot_bid = bot_bidding(diamond, bot_cards)
        player_bid = input("Place a bid: ")

        while not valid_card(player_cards, player_bid):
            player_bid = input("Place a valid bid: ")

        player_cards.remove(player_bid)
        print("Bot bid:", bot_bid)

        # display the remaining cards 
        display_player_cards(player_cards)

        ps, cs = score(bot_bid, player_bid, diamond, ps, cs)
        print("Player Score:", ps, "Bot Score:", cs, '\n')

    # return ("Bot wins!" if cs > ps else "Player wins!")
    # the above return is not printing when the game ends so adding a conditonal statement will work
    if cs>ps:
        print("Bot Wins!")
    else:
        print("Player Wins!") 

play_game()
