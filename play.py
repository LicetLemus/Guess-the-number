"""
randint return a random number selected element from the specified range
random.randint(start, end)
start Required. An integer specific at which position to start.
end Required. An integer specific at which position to end.

"""

import random

print("Bienvenido al juego de adivinar el número, ¡Buena suerte!")

number_random = random.randint(1, 100)
print("¡se ha generado un número aleatorio entre 1 y 100!")

MAX_TRY = 10
try_done = 0

# function1 validar el numero ( == > <)
# function 2 player user (input)
# function 3 player computer (random)
# function 4 main (while) validar el numero, player user maimo inten, player computer maimo inten, intentos, break

number_user = []
number_computer = []

while try_done < MAX_TRY:
    number_user.append(int(input("Introduce un número: ")))

    if number_user[-1] > number_random:
        number_computer.append(random.randint(1, number_user[-1] - 1))
    else:
        number_computer.append(random.randint(number_user[-1] + 1, 100))

    if number_user[-1] == number_random:
        print("¡Felicidades! Has adivinado el número")
        break

    if number_user[-1] > number_random:
        print("El número a adivinar es menor")
    else:
        print("El número a adivinar es mayor")

    print("El ordenador ha elegido el numero: ", number_computer[-1])

    if number_computer[-1] == number_random:
        print("\n¡El ordenador ha adivinado el número!")
        break

    try_done += 1

    if try_done == 10:
        print("¡Has agotado tus intentos!")
        break

    print("Intentos restantes: ", MAX_TRY - try_done)

print("\nEl número a adivinar era: ", number_random)

# .join () method returns a string in which the elements of sequence have been joined by str separator ' '.
# .map() function returns a list of the results converted to string
print("numeros introducidos por el usuario:", ' '.join(map(str, number_user)))
print("numeros introducido por el ordenador:",
      ' '.join(map(str, number_computer)))
