import unittest

from unittest.mock import patch, call
from src.utils import print_information, get_random_number, get_validate_number

class TestUtils(unittest.TestCase):
    
    @patch('builtins.print')
    def test_print_information(self, mocked_print):
        """
        Test the print_information function.
        """
        print_information()
        self.assertEqual(print.call_count, 2)
        mocked_print.assert_has_calls([
            call("Bienvenido al juego de adivinar el número, ¡Buena suerte!"),
            call("¡se ha generado un número aleatorio entre 1 y 100!")
        ])
        
    @patch('random.randint', return_value=50)
    def test_get_random_number(self, mocked_random):
        """
        Test function get_random_number
        """
        
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_random_number(ranges)
        self.assertEqual(result, 50)
        
    
    def test_get_validate_number_outside_ranges(self):
        """
        Test the get_validate_number function when the number is outside the ranges.
        """
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_validate_number(101, 50, ranges, "usuario")
        self.assertEqual(result, (False, "usuario: El número no es válido. Debe estar entre 1 y 100."))
        
    @patch('random.randint', return_value=50)
    def test_get_validate_number_equal_random(self, mocked_random):
        """
        Test the get_validate_number function when the number is correct.
        """
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_validate_number(50, 50, ranges, "usuario")
        self.assertEqual(result, (True, "¡Felicidades, usuario! Has adivinado el número correctamente."))
        
    @patch('random.randint', return_value=50)
    def test_get_validate_number_greater_random(self, mocked_random):
        """
        Test the get_validate_number function when the number is lower than the random number.
        """
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_validate_number(10, 50, ranges, "usuario")
        self.assertEqual(result, (False, "El número es mayor."))
        
    @patch('random.randint', return_value=50)
    def test_get_validate_number_minor_random(self, mocked_random):
        """
        Test the get_validate_number function when the number is greater than the random number.
        """
        ranges = {
            "min": 1,
            "max": 100
        }
        
        result = get_validate_number(60, 50, ranges, "usuario")
        self.assertEqual(result, (False, "El número es menor."))