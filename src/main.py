from game import game

game()

def play_again():
    """The function allows the user to play again the game"""

    play_again_user = input("¿Quieres jugar de nuevo? (s/n): ")
    if play_again_user == "s":
        game()
    else:
        print("¡Gracias por jugar!")

play_again()
    