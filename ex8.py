while True:

    p1 = input("Rock, Papers, Scissors - Player 1: ")
    p2 = input("Rock, Papers, Scissors - Player 2: ")

    if p1 == "rock":
        if p2 == "scissors":
            winner = "Player 1"
        elif p2 == "rock":
            winner = "Nobody"
        else:
            winner = "Player 2"
    elif p1 == "scissors":
        if p2 == "paper":
            winner = "Player 1"
        elif p2 == "scissors":
            winner = "Nobody"
        else:
            winner = "Player 2"
    elif p1 == "paper":
        if p2 == "rock":
            winner = "Player 1"
        elif p2 == "paper"
            winner = "Nobody"
        else:
            winner = "Player 2"

    cont_playing = input("%s is the winner! Play again? " % winner)
    if cont_playing != "yes":
        break
