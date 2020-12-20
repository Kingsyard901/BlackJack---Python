#This is my first attempt on the game, I later replaced it for the functional version in main.

# Imports
import random


# Variables
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

player = random.sample(cards, 2)
computer = random.sample(cards, 2)

print(f"You got the cards {player} which is a total of {sum(player)}")
print(f"Computer got the cards {computer} which is a total of {sum(computer)} \n")

game_is_on = True

while game_is_on:
    if sum(player) < 21 and sum(computer) < 21:
        add_card = input("Do you want to take another card? Type 'yes' or 'no': ")
        if add_card == "yes":
            player.append(random.choice(cards))
            computer.append(random.choice(cards))
            print(f"You got the cards {player} which is a total of {sum(player)}")
            print(f"Computer got the cards {computer} which is a total of {sum(computer)}\n")
        elif sum(player) > sum(computer):
            print(f"Player Wins with {sum(player)} points!")
            game_is_on = False
        else:
            print(f"Computer wins with {sum(computer)} points!")
            game_is_on = False
    else:
        if sum(player) > 21:
            if sum(player) == 21:
                print(f"Player is Winner with a total of: {sum(player)}")
            else:
                print(f"Player is Bust with a  total of {sum(player)} and Computer is Winner!")
        elif sum(computer) > 21:
            if sum(player) == 21:
                print(f"Computer is Winner with a total of: {sum(computer)}")
            else:
                print(f"Computer is bust with a total of {sum(computer)} and Player is Winner!")
        game_is_on = False
