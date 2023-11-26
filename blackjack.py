import random

#define the deck with suits ranking etc.
def DefineDeck():
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        #j,q,k,a stand for jack, queen, king and ace
    suits = ['Hearts' , 'Diamonds', 'Clubs', 'Spades']
    return[{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

#shuffle the deck
def shuffle(CardDeck):
    random.shuffle(CardDeck)

#deal cards to player
def deal(CardDeck):
    return CardDeck.pop()

#function that calculates the score of your hand
def CalculateHandValue(hand):
    #assigns numerical values to card numbers
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    HandValue = sum(values[card['rank']] for card in hand) #adds the number of card's values
    NumberOfAces = sum(1 for card in hand if card['rank'] == 'A')
    
    #make a loop that happens for aces since they can either be a 11 or 1
    while NumberOfAces > 0 and HandValue > 21:
        HandValue -= 10
        NumberOfAces -= 1

    return HandValue

#function that prints the hand after calculating your score
def PrintHand(hand, HideFirstCard = False):
    if HideFirstCard:
        print(f"Hidden Card, {hand[1]['rank']} of {hand[1]['suit']}")
        for card in hand[2:]:
            print(f"{card['rank']} of {card['suit']}")
    else:
        for card in hand:
            print(f"{card['rank']} of {card['suit']}")

# make a player's turn simulation
def PlayerTurn(PlayerHand, CardDeck):
    while True:
        print("\nPlayer's turn:")
        PrintHand(PlayerHand)
        choice = input("Do you want to hit or stay? ").lower().strip() #takes away any unnecessary errors that could happen when type in an input
        print(f"Choice: {choice}") # verifies which choice was chosen after entering the text

        if choice == 'hit':
            PlayerHand.append(deal(CardDeck))
            if CalculateHandValue(PlayerHand) > 21:
                print("Bust! You lose.")
                return 'bust'
        elif choice == 'stay':
            print("Player chose to stay.")
            break #allows the code to flow into the next block (i had a problem before without having the break line)
        else:
            print("Please enter either 'hit' or 'stay'.")

    return 'stay'

# make a dealer's turn simulation
def DealerTurn(DealerHand, CardDeck):
    print("\nDealer's turn:")
    PrintHand(DealerHand)

    while CalculateHandValue(DealerHand) < 15:
        DealerHand.append(deal(CardDeck))
        print(f"Dealer hits: {DealerHand[-1]['rank']} of {DealerHand[-1]['suit']} ")

    if CalculateHandValue(DealerHand) > 21:
        print("Dealer busts! Player wins.")
        return 'bust'
    else: 
        print("Dealer stays.")
        return 'stay'

# put everything together and play the game
def PlayGame():
    while True:
        CardDeck = DefineDeck()
        shuffle(CardDeck)

        PlayerHand = [deal(CardDeck), deal(CardDeck)]
        DealerHand = [deal(CardDeck), deal(CardDeck)]

        print("\nIt's time to play Blackjack!")
        print("\nYou can either choose to hit or stay. the goal is to go as close to but under 21. If you go over 21 it is called a bust and you lose immediately.")
        print("\nYou will be playing against the dealer. If both of you stay under 21 after the round, the highest total wins!")
        print("\nBest of Luck!")

        # player's turn
        PlayerResult = PlayerTurn(PlayerHand, CardDeck)
        if PlayerResult  == 'bust':
            return

        # dealer's turn
        DealerResult = DealerTurn(DealerHand, CardDeck)
        if DealerResult == 'bust':
            return

        # compare dealer vs player hands
        PlayerValue = CalculateHandValue(PlayerHand)
        DealerValue = CalculateHandValue(DealerHand)

        print("\nGame Results")

        #print player's hand when both stay
        print("\nPlayer's Hand:")
        PrintHand(PlayerHand)
        print(f"Player's Hand: {PlayerValue}\n")

        #print dealer's hand when both stay
        print("\nDealer's Hand: ")
        PrintHand(DealerHand)
        print(f"Dealer's Hand Value: {DealerValue}\n")

        # if else statement saying who wins or if it is a tie
        if PlayerValue > DealerValue:
            print("Player wins!")
        elif PlayerValue < DealerValue:
            print("Dealer wins!")
        else:
            print("It's a tie!")

# code that ensures that the play_game() function only runs when it is being ran directly and not when it is imported into another script
if __name__ == "__main__":
    PlayGame()








