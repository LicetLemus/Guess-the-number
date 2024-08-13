import unittest
from unittest.mock import patch
from src.game import game
from src.players import number_user, number_computer


MAX_TRY = 10 

class TestGame(unittest.TestCase):

    @patch('src.game.validate_number')
    @patch('src.game.player_user')
    @patch('src.game.player_computer')
    @patch('builtins.print')  # Para capturar las salidas de print
    def test_game_user_wins(self, mock_print, mock_player_computer, mock_player_user, mock_validate_number):
        """Test cuando el usuario adivina el número correcto"""
        
        # Configuración del mock
        number_user.clear()
        number_computer.clear()
        number_user.append(50)
        mock_validate_number.side_effect = lambda number, random_number, entity: number == random_number # Si el número es igual al número aleatorio, devuelve True

        with patch('random.randint', return_value=50):  # Configura el número aleatorio
            game()

        # Verificaciones
        mock_player_user.assert_called_once()  # Verifica que player_user se haya llamado
        mock_validate_number.assert_called_with(50, 50, 'usuario')  # Verifica que validate_number se llame con los parámetros esperados
        mock_player_computer.assert_not_called()  # Verifica que player_computer no se haya llamado porque el juego terminó antes

        # Verifica que se imprimió el mensaje de juego terminado
        mock_print.assert_any_call("¡Juego terminado!")


    @patch('src.game.validate_number')
    @patch('src.game.player_user')
    @patch('src.game.player_computer')
    @patch('builtins.print')  # Para capturar las salidas de print
    def test_game_computer_wins(self, mock_print, mock_player_computer, mock_player_user, mock_validate_number):
        """Test cuando el ordenador adivina el número correcto"""
        
        # Configuración del mock
        number_user.clear()
        number_computer.clear()
        number_user.append(0)
        number_computer.append(50)
        mock_validate_number.side_effect = lambda number, random_number, entity: number == random_number # Si el número es igual al número aleatorio, devuelve True

        with patch('random.randint', return_value=50):  # Configura el número aleatorio
            game()

        # Verificaciones
        mock_player_user.assert_called_once()  # Verifica que player_user se haya llamado
        mock_validate_number.assert_called_with(50, 50, 'ordenador')  # Verifica que validate_number se llame con los parámetros esperados
        mock_player_computer.assert_called_once()  # Verifica que player_computer no se haya llamado porque el juego terminó antes

        # Verifica que se imprimió el mensaje de juego terminado
        mock_print.assert_any_call("¡Juego terminado!")