import unittest
from unittest.mock import patch # los patch se utilizan para simular la entrada de datos, sustituyendo la función original temporalmente mientras se ejecutan las pruebas
from src.players import player_user, player_computer

class TestPlayers(unittest.TestCase):
    """
    Test the functions of the players module.
    """

    @patch('src.players.number_user', new_callable=list)
    @patch('builtins.input', return_value=5)
    def test_player_user(self, mock_input, mock_number_user):
        """
        Test the player_user function.
        """
        player_user()  # Llama a la función player_user
        self.assertEqual(mock_number_user[-1], 5)  # Verifica que el valor de mock_number_user[-1] sea igual a 5


    @patch('src.players.number_user', new_callable=list)
    @patch('src.players.number_computer', new_callable=list)
    @patch('random.randint', return_value=3)
    def test_player_computer_with_number_random_smaller(self, mock_randint, mock_number_computer, mock_number_user):
        """
        Test the player_computer function when the random number is smaller than the user number.
        """
        mock_number_user.append(10)  # Simula que el usuario ya ha introducido el número 10
        player_computer(9)  # Llama a la función player_computer con un número aleatorio menor (9)
        self.assertEqual(mock_number_computer[-1], 3)  # Verifica que el número elegido por el ordenador sea 3


    @patch('src.players.number_user', new_callable=list) # simula la lista de números introducidos por el usuario
    @patch('src.players.number_computer', new_callable=list) # simula la lista de números introducidos por el ordenador
    @patch('random.randint', return_value=15)
    def test_player_computer_with_number_random_greater(self, mock_randint, mock_number_computer, mock_number_user):
        """
        Test the player_computer function when the random number is greater than the user number.
        """
        mock_number_user.append(10)  # Simula que el usuario ya ha introducido el número 10
        player_computer(11)  # Llama a la función player_computer con un número aleatorio mayor (11)
        self.assertEqual(mock_number_computer[-1], 15)  # Verifica que el número elegido por el ordenador sea 15