import unittest
from unittest.mock import patch, call
from src.game import game


MAX_TRY = 10 

class TestGame(unittest.TestCase):

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.print_information')
    @patch('src.game.set_number_user', return_value=(50, [50]))
    @patch('src.game.set_number_computer', return_value=(40, [50, 40]))
    @patch('src.game.get_validate_number', side_effect=[(True, "¡Felicidades, usuario! Has adivinado el número correctamente.")])
    @patch('builtins.print')
    def test_user_wins(self, mock_print, mock_get_validate_number, mock_set_number_computer, mock_set_number_user, mock_print_information, mock_get_random_number):
        """
        Test when the user guesses the correct number.
        """
        game()
        
        mock_get_random_number.assert_called_once_with({'min': 1, 'max': 100})
        mock_print_information.assert_called_once()
        mock_set_number_user.assert_called_once_with([])
        mock_set_number_computer.assert_called_once_with([50], '', {'min': 1, 'max': 100})
        mock_get_validate_number.assert_called_once_with(50, 50, {'min': 1, 'max': 100}, 'usuario')
        mock_print.assert_any_call("¡Juego terminado!")



    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.print_information')
    @patch('src.game.set_number_user', return_value=(30, [30]))
    @patch('src.game.set_number_computer', return_value=(50, [30, 50]))
    @patch('src.game.get_validate_number', side_effect=[
        (False, "El número ingresado no es correcto."),  # Primera llamada para el usuario
        (True, "¡Felicidades, computadora! Has adivinado el número correctamente.")  # Segunda llamada para la computadora
    ])
    @patch('builtins.print')
    def test_computer_wins(self, mock_print, mock_get_validate_number, mock_set_number_computer, mock_set_number_user, mock_print_information, mock_get_random_number):
        """
        Test when the user guesses the correct number.
        """
        game()
        
        mock_get_random_number.assert_called_once_with({'min': 1, 'max': 100})
        mock_print_information.assert_called_once()
        mock_set_number_user.assert_called_once_with([])
        mock_set_number_computer.assert_called_once_with([30], '', {'min': 1, 'max': 100})
        mock_get_validate_number.assert_has_calls([
            call(30, 50, {'min': 1, 'max': 100}, 'usuario'),
            call(50, 50, {'min': 1, 'max': 100}, 'computadora')
            ])
        mock_print.assert_any_call("¡Juego terminado!")
        
    
    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.print_information')
    @patch('src.game.set_number_user', side_effect=[(30, [30])] * 10)  # Simula 10 intentos del usuario
    @patch('src.game.set_number_computer', side_effect=[(40, [30, 40])] * 10)  # Simula 10 intentos de la computadora
    @patch('src.game.get_validate_number', side_effect=[
        (False, "El número ingresado no es correcto."),
        (False, "El número es mayor.")
    ] * 10)  # Simula respuestas incorrectas
    @patch('builtins.print')
    def test_try_done_round_max_try(self, mock_print, mock_get_validate_number, mock_set_number_computer, mock_set_number_user, mock_print_information, mock_get_random_number):
        """
        Test when the maximum number of tries is reached.
        """
        game()
        
        mock_get_random_number.assert_called_once_with({'min': 1, 'max': 100})
        mock_print_information.assert_called_once()
        
        self.assertEqual(mock_set_number_user.call_count, 10)
        self.assertEqual(mock_set_number_computer.call_count, 10)
        
        mock_get_validate_number.assert_has_calls([
            call(30, 50, {'min': 1, 'max': 100}, 'usuario'),
            call(40, 50, {'min': 1, 'max': 100}, 'computadora')
        ] * 10, any_order=False)
        
        mock_print.assert_any_call("¡Has agotado tus intentos!")
        mock_print.assert_any_call("\nEl número a adivinar era: ", 50)
        