#
#   Write a program that given two numbers as input make the main operations.
#
#   Output:
#   Insert first number: 4
#   Insert second number: 2
#
#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2
#

def operazioni(num1:int, num2: int) -> None:
    print("Somma:", num1 + num2)
    print("Differenza:", num1 - num2)
    print("Prodotto:", num1 * num2)
    if num2 == 0:
        print("Divisione non possibile. Il divisore è 0.")
    else:
        print("Divisione:", num1 / num2)

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
operazioni(a, b)
