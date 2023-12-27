import random
player1 = input('player1:choose rock,paper,scissors: ').lower()
player2 = input('player2:choose rock,paper,scissors: ').lower()

if player1 == "rock" and player2 == "paper":
    print("player2 won")
elif player1 == "scissors" and player2 == "rock":
    print("player2 won")
elif player1 == "paper" and player2 == "scissors":
    print("player2 won")
elif player1 == player2:
    print("TIE,play again")
else:
    print("player1 won")
