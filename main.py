from src.game import game

def main():
    """
    The main function allows the user to play the game and ask if they want to play again
    """
    while True:
        game()
        play_again_user = input("¿Quieres jugar de nuevo? (s/n): ")
        if play_again_user == "n":
            print("¡Gracias por jugar!")
            break


if __name__ == "__main__": # si el archivo es el principal, se llama a la función main
    main() 
