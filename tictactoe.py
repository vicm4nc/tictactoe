# 04/30/2022
# Vícto Carrillo
# Tic-Tac-Toe


game = []
for some in range(9):
    game.append(some + 1)

def main():
    player = next_player("")
    #when play_number will be nine won't have next player
    play_number = 0
    while not (haswone() or play_number == 9):
        displaygame()
        make_move(player)
        play_number += 1
        player = next_player(player)
    displaygame()
    print("Good game. Thanks for playing!") 

#The player will use x or o
def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

#Here I compare if some one has wone, first horizontally from top to bottom,
#then vertically, from left to right
#finally, diagonally, the two combinations
def haswone():
    if game[0] == game[1] == game[2]:
        return True
    elif game[3] == game[4] == game[5]:
        return True
    elif game[6] == game[7] == game[8]:
        return True
    elif game[0] == game[3] == game[6]:
        return True
    elif game[1] == game[4] == game[7]:
        return True
    elif game[2] == game[5] == game[8]:
        return True
    elif game[0] == game[4] == game[8]:
        return True
    elif game[2] == game[4] == game[6]:
        return True
    else:
        return False

def displaygame():
    print()
    print(f"{game[0]}|{game[1]}|{game[2]}")
    print('-+-+-')
    print(f"{game[3]}|{game[4]}|{game[5]}")
    print('-+-+-')
    print(f"{game[6]}|{game[7]}|{game[8]}")
    print()
    

def make_move(player):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    game[square - 1] = player

if __name__ == "__main__":
    main()