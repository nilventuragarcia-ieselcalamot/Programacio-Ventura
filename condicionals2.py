num1 = int((input("Introduiex el primer nombre ")))
num2 = int((input("Introduiex el segon nombre ")))
print("1 = Sumar     2 = Restar      3 = Multiplicar    4 = Dividir")
print( "5 = Elevar   6 = Modular     7 = División entera")
operacion = int(input("Selecciona una operación: "))

if operacion == 1:
    print("La suma és: ", num1 + num2)

elif operacion == 2:
    print("1 =", num1, "-", num2, "o", "2 =", num2, "-", num1)
    resposta = int(input("Qué vols fer?"))
    if resposta == 1:
        print("La resta és: ", num1 - num2)
    elif resposta == 2:
        print("La resta és: ", num2 - num1)
    else:
        print("Operació no vàlida")

elif operacion == 3:
    print("La multiplicació és: ", num1 * num2)

elif operacion == 4:
    print("1 =", num1, "entre", num2, "o", "2 =", num2, "entre", num1)
    resposta = int(input("Qué vols fer?"))
    if resposta == 1:
        print("La divisió és: ", num1 / num2)
    elif resposta == 2:
        print("La divisió és: ", num2 / num1)
    else:
        print("Operació no vàlida")

elif operacion == 5:
    print("presiona 1 para", num1, "elevat a", num2, "o", " presiona 2 para", num2, "elevat a", num1)
    resposta = int(input("Qué vols fer?"))
    if resposta == 1:
        print("La potencia és: ", num1 ** num2)
    elif resposta == 2:
        print("La potencia és: ", num2 ** num1)
    else:
        print("Operació no vàlida")

elif operacion == 6:
    print("presiona 1 para", num1, "modulat a", num2, "o", " presiona 2 para", num2, "modulat a", num1)
    resposta = int(input("Qué vols fer?"))
    if resposta == 1:
        print("El mòdul és: ", num1 % num2)
    elif resposta == 2:
        print("El mòdul és: ", num2 % num1)
    else:
        print("Operació no vàlida")

elif operacion == 7:
    print("presiona 1 para", num1, "entre", num2, "de manera entera  o  ", "presiona 2 para", num2, "entre", num1,"de manera entera")
    resposta = int(input("Qué vols fer?"))
    if resposta == 1:
        print("La divisió entera és: ", num1 // num2)
    elif resposta == 2:
        print("La divisió entera és: ", num2 // num1)
    else:
        print("Operació no vàlida")

else:
    print("Operació no vàlida")