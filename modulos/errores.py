frase = "Buenas Noches"
print(frase[20])
try:
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    res = num1 // num2
    print(res)
except (ZeroDivisionError, ValueError, TypeError):
    print("Error de datos")
