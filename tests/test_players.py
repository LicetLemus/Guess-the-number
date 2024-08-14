import unittest
from unittest.mock import patch, call # los patch se utilizan para simular la entrada de datos, sustituyendo la función original temporalmente mientras se ejecutan las pruebas
from src.players import get_input_value, set_number_user, get_number_computer, set_number_computer, print_number_user_computer

class TestPlayers(unittest.TestCase):
    """
    Test the functions of the players module.
    """

    @patch('builtins.input', return_value='5')
    def test_get_input_value(self, mock_input):
        """
        Tet the get_input_value function.
        """
        result = get_input_value()
        self.assertEqual(result, '5') 

    # def test_validate_number_user_valid(self):
    #     """
    #     Test the validate_number_user function.
    #     """
    #     result = validate_number_user('5')
    #     self.assertEqual(result, 5)
    
    # def test_validate_number_user_invalid(self):
    #     # Test para un número no válido (no es un número)
    #     result = validate_number_user('abc')
    #     self.assertIsNone(result)
        
    
    @patch('src.players.get_input_value', return_value='7')
    def test_set_number_user_valid(self, mock_imput):
        """
        Test the player_computer function when the random number is smaller than the user number.
        """
        user_computer_numbers = []
        number_user, update_user_computer_numbers = set_number_user(user_computer_numbers)
        self.assertEqual(number_user, 7)
        self.assertIn(7, update_user_computer_numbers) # assertIn()verifica si el elemento está en la lista

    
    @patch('src.players.get_input_value', return_value='gtheds')
    def test_set_number_user_invalid(self, mock_input):
        """
        Test the set_number_user function with an invalid number.
        """
        user_computer_numbers = []
        number_user, updated_user_computer_numbers = set_number_user(user_computer_numbers)
        self.assertEqual(number_user, None)
        self.assertEqual(updated_user_computer_numbers, [])

# -------------------------------------------------------------computer------------------------------------------------------

    def test_get_number_computer_empty_parameter(self):
        """
        Test the get_number_computer function when the computer has a empty list of numbers.
        """
        user_computer_numbers = []
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_number_computer(user_computer_numbers, "", ranges)
        self.assertEqual(result >= 1 and result <= 100, True)

    def test_get_number_computer_feedback_minor(self):
        """
        Test the get_number_computer function when the computer has a list of numbers and the last number is not in the list.
        """
        user_computer_numbers = [10, 70, 30, 40]
        ranges = {
            "min": 1,
            "max": 100
        }
    
        result = get_number_computer(user_computer_numbers, "El número es menor.", ranges)
        self.assertEqual(result >= 30 and result <= 40, True)


    def test_get_number_computer_feedback_empty(self):
        """
        Test the get_number_computer function when the feedback is empty.
        """
        user_computer_numbers = [10, 20, 30]
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_number_computer(user_computer_numbers, "", ranges)
        self.assertEqual(result >= 1 and result <= 100, True)
    
    def test_get_number_computer_feedback_different(self):
        """
        Test the get_number_computer function when the feedback is different from the other options.
        """
        user_computer_numbers = [10, 50,20, 40]
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_number_computer(user_computer_numbers, "excelente", ranges)
        self.assertEqual(result >= 1 and result <= 100, True)
        
            
    def test_get_number_computer_feedback_user_computer_number(self):
        """
        Test the get_number_computer function when has a feedback and the last number is in the list.
        """
        user_computer_numbers = [10, 50,20, 40]
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_number_computer(user_computer_numbers, "El número es mayor.", ranges)
        self.assertEqual(result >= 40 and result <= 50, True)


    def test_set_number_computer(self):
        """
        Test the set_number_computer function.
        """
        user_computer_numbers = [10, 30, 50, 20]
        ranges = {
            "min": 1,
            "max": 100
        }
        
        number_computer, update_user_computer_numbers = set_number_computer(user_computer_numbers, "El número es mayor.", ranges)
        self.assertEqual(number_computer >= 20 and number_computer <= 30, True)
        self.assertIn(20, update_user_computer_numbers)
        
    
    @patch('builtins.print')
    def test_print_number_user_computer(self, mocked_print):
        """
        Test the print_number_user_computer function.
        """
        print_number_user_computer(10, 20)

        self.assertEqual(mocked_print.call_count, 2)
        mocked_print.assert_has_calls([
            call("El usuario ha introducido el número: ", 10),
            call("El ordenador ha introducido el número: ", 20)
        ])