def validate_number(number, number_random):
    """The function validates the number entered by the user
    and compares it with the random number"""

    if number == number_random:
        print("¡Felicidades! Has adivinado el número")
    if number < number_random:
        print("El número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")
    