import unittest # importar la librería unittest para realizar las pruebas
from unittest.mock import patch # esta funcion permite simular o mockear objetos dentro de las pruebas
from src.players import player_user, number_user

# unittest trabaja con una clase que hereda de TestCase, por lo tanto, se crea una clase TestPlayers que hereda de 
class TestPlayers(unittest.TestCase):
    """
    Test the functions of the players module
    """
    @patch('builtins.input', return_value='5') # se simula la entrada de un valor por teclado con el valor 5
    def test_player_user(self, mock_input): # self es el objeto que se pasa a la función
        """
        Test the player_user function
        """
        player_user() # se llama a la función player_user
        self.assertEqual(number_user[-1], 5) # se comprueba que el último valor de la lista number_user sea 5