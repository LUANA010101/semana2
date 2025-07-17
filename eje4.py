numero = int(input("introduce un númeroentero positivo:"))

if numero < 0:
    print("El número debe ser positivo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    print("El factorial de 5", numero,"es", factorial)

