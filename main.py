# Imports
import random


# Variables
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
player = random.sample(cards, 2)
computer = random.sample(cards, 2)


# Print out the first cards for player and computer
print(f"You got the cards {player} which is a total of {sum(player)}")
print(f"Computer got the cards {computer} which is a total of {sum(computer)} \n")


# Variable for While loop
game_is_on = True


# Function for continuing game and choosing a new card
def continue_game():
    global game_is_on
    go_on = input("Do you want another card? Type 'y' or 'n': ")
    if go_on == "y":
        add_card_player()
        add_card_computer()
        check_win()
    elif go_on == "n":
        check_out()


# Function to check if either players have won upon new cards as well as checking if nr 11 needs to be converted into 1
def check_win():
    global game_is_on

    for index, card_player in enumerate(player):
        if card_player == 11:
            player[index] = 1

    for index, card_computer in enumerate(computer):
        if card_computer == 11:
            computer[index] = 1


    if sum(player) == 21:
        print(f"Player wins! Points: {sum(player)}")
        game_is_on = False
    elif sum(computer) == 21:
        print(f"Computer Wins! Points: {sum(computer)}")
        game_is_on = False
        # TODO: Add if it is a draw
    elif sum(player) > 21:
        print(f"Win! \n Player Lose! Points: {sum(player)} \n Computer Wins! Points: {sum(computer)} \n")
        game_is_on = False
    elif sum(computer) > 21:
        print(f"Win! \n Player Wins! Points: {sum(player)} \n Computer Lose! Points: {sum(computer)} \n")
        game_is_on = False
    else:
        continue_game()


# Function for when player chooses "n" (no) and don't want another card.
def check_out():
    global game_is_on
    print(f"Player got cards {player} with a total of {sum(player)}")
    add_card_computer()

    if sum(player) == 21:
        print(f"Player wins! Points: {sum(player)}")
    elif sum(computer) == 21:
        print(f"Computer Wins! Points: {sum(computer)}")
    elif sum(player) > sum(computer):
        print(f"Win! \n Player Lose! Points: {sum(player)} \n Computer Wins! Points: {sum(computer)} \n")
    elif sum(computer) < sum(player):
        print(f"Win! \n Player Wins! Points: {sum(player)} \n Computer Lose! Points: {sum(computer)} \n")

    game_is_on = False


# Function to add new card to player
def add_card_player():
    player.append(random.choice(cards))
    print(f"Player got cards {player} with a total of {sum(player)}")


# Function to add new card to computer
def add_card_computer():
    computer.append(random.choice(cards))
    print(f"Computer got cards {computer} with a total of {sum(computer)}\n")


# IF statement to check if the two initial cards given equals 21 (Black Jack) and announces the winner
if sum(player) == 21:
    print("Player wins at draw!")
    game_is_on = False
elif sum(computer) == 21:
    print("Computer wins at draw!")
    game_is_on = False


# While loop to keep the game going until there is a winner.
# TODO: Add to while loop question if player wants to play another round
while game_is_on:
    continue_game()
