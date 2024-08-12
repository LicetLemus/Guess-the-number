import unittest
from unittest.mock import patch, call
from src.game import game
from src.players import number_user, number_computer


MAX_TRY = 10 

class TestGame(unittest.TestCase):
    """
    Test the game function.
    """
    
    @patch('random.randint', return_value=50)  # Simula el número aleatorio generado
    @patch('src.game.player_user')
    @patch('src.game.validate_number')
    @patch('src.game.player_computer')
    @patch('builtins.print')  # Mocks print to capture its output
    def test_game(self, mock_print, mock_player_computer, mock_validate_number, mock_player_user, mock_randint):
        number_user.clear()
        number_computer.clear()
        number_user.append(10)

        game()
        # Verifica que player_user se llame
        mock_player_user.assert_called()

        mock_validate_number.assert_called()  # Puedes usar assert_called() y luego imprimir los argumentos si es necesario
            
        # Verifica que player_computer se llame con el número aleatorio
        mock_player_computer.assert_called_with(50)
            
        # Verifica la llamada a random.randint
        mock_randint.assert_called_with(1, 100)
