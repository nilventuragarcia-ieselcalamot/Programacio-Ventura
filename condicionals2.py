def anti_texto(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido.")
num1 = anti_texto("Introduiex el primer nombre ")
num2 = anti_texto("Introduiex el segon nombre ")
print("presiona una tecla per seleccionar una operació")
print("1 = Sumar     2 = Restar      3 = Multiplicar    4 = Dividir")
print( "5 = Elevar   6 = Modular     7 = División entera")
operacion = anti_texto("Selecciona una operación: ")

if operacion == 1:
    print("La suma és: ", num1 + num2)

elif operacion == 2:
    print("Presiona", f"\033[1m{1}\033[0m", "para hacer (", num1, "-", num2, ") o Presiona", f"\033[1m{2}\033[0m", " para hacer (", num2, "-", num1, ")")
    resposta = anti_texto("Qué vols fer?")
    if resposta == 1:
        print("La resta és: ", num1 - num2)
    elif resposta == 2:
        print("La resta és: ", num2 - num1)
    else:
        print("Operació no vàlida")

elif operacion == 3:
    print("La multiplicació és: ", num1 * num2)

elif operacion == 4:
    print("Presiona", f"\033[1m{1}\033[0m", "para hacer (", num1, "entre", num2, ") o", "Presiona", f"\033[1m{2}\033[0m", "para hacer (", num2, "entre", num1, ")")
    resposta = anti_texto("Qué vols fer?")
    if resposta == 1:
        if num2 == 0:
            print("Error: No es pot dividir per zero.")
        else:
            print("La divisió és: ", num1 / num2)
    elif resposta == 2:
        if num1 == 0:
            print("Error: No es pot dividir per zero.")
        else:
            print("La divisió és: ", num2 / num1)
    else:
        print("Operació no vàlida")

elif operacion == 5:
    print("Presiona", f"\033[1m{1}\033[0m", "para hacer (", num1, "elevat a", num2, ") o", "Presiona", f"\033[1m{2}\033[0m", "para hacer (", num2, "elevat a", num1, ")")
    resposta = anti_texto("Qué vols fer?")
    if resposta == 1:
        if num1 == 0 and num2 < 0:
            print("Error: No es pot elevar zero a un exponent negatiu.")
        else:
            print("La potencia és: ", num1 ** num2)
    elif resposta == 2:
        if num2 == 0 and num1 < 0:
            print("Error: No es pot elevar zero a un exponent negatiu.")
        else:
            print("La potencia és: ", num2 ** num1)
    else:
        print("Operació no vàlida")

elif operacion == 6:
    print("Presiona", f"\033[1m{1}\033[0m", "para hacer (", num1, "modulat a", num2, ") o", "Presiona", f"\033[1m{2}\033[0m", "para hacer (", num2, "modulat a", num1, ")")
    resposta = anti_texto("Qué vols fer?")
    if resposta == 1:
        if num2 == 0:
            print("Error: No es pot calcular el mòdul amb divisor zero.")
        else:
            print("El mòdul és: ", num1 % num2)
    elif resposta == 2:
        if num1 == 0:
            print("Error: No es pot calcular el mòdul amb divisor zero.")
        else:
            print("El mòdul és: ", num2 % num1)
    else:
        print("Operació no vàlida")

elif operacion == 7:
    print("Presiona", f"\033[1m{1}\033[0m", "para hacer (", num1, "entre", num2, "de manera entera)  o  ", "Presiona", f"\033[1m{2}\033[0m", "para hacer (", num2, "entre", num1,"de manera entera)")
    resposta = anti_texto("Qué vols fer?")
    if resposta == 1:
        if num2 == 0:
            print("Error: No es pot calcular la divisió entera amb divisor zero.")
        else:
            print("La divisió entera és: ", num1 // num2)
    elif resposta == 2:
        if num1 == 0:
            print("Error: No es pot calcular la divisió entera amb divisor zero.")
        else:
            print("La divisió entera és: ", num2 // num1)
    else:
        print("Operació no vàlida")

else:
    print("Operació no vàlida")