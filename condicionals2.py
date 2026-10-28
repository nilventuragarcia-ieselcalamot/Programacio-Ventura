num1 = int((input("Introduiex el primer nombre ")))
num2 = int((input("Introduiex el segon nombre ")))
print("1 = Sumar 2 = Restar 3 = Multiplicar 4 = Dividir")
print( "5 = Elevar 6 = Modular 7 = División entera")
operacion = int(input("Selecciona una operación: "))
if operacion == 1:
    print("La suma és: ", num1 + num2)
elif operacion == 2:
    print("La resta és: ", num1 - num2, "i" , num2 - num1)
elif operacion == 3:
    print("La multiplicació és: ", num1 * num2)
elif operacion == 4:
    print("La divisió és: ", num1 / num2, "i", num2 / num1)
elif operacion == 5:
    print("Elevar és: ", num1 ** num2)
elif operacion == 6:
    print("El mòdul és: ", num1 % num2)
elif operacion == 7:
    print("La divisió entera és: ", num1 // num2)
else:
    print("Operació no vàlida")