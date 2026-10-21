num1 = int(input("Introduiex el primer nombre "))
num2 = int(input("Introdueix el segon nombre        "))
print("Suma:", num1, "+", num2, "=", num1 + num2)
print("Resta:", num1, "-", num2, "=", num1 - num2)
print("Resta:", num2, "-", num1, "=", num2 - num1)
print("Producte:", num1, "*", num2, "=", num1 * num2)
print("Divisió:", num1, "/", num2, "=", num1 / num2)
print("Divisió:", num2, "/", num1, "=", num2 / num1)
print("Divisió entera:", num1, "//", num2, "=", num1 // num2)
print("Divisió entera:", num2, "//", num1, "=", num2 // num1)
print("Mòdul:", num1, "%", num2, "=", num1 % num2)
print("Mòdul:", num2, "%", num1, "=", num2 % num1)
print("Exponent:", num1, "**", num2, "=", num1 ** num2)
print("Exponent:", num2, "**", num1, "=", num2 ** num1, "\n")

t1 = input("Escriu un text curt: ")
t2 = input("Escriu un altre text curt: ")
print("Concatenar:", t1, "+", t2, "=", t1 + t2)
print("Multiplicació (3):" , t1, "*", 3, "=", t1 * 3, "\n")

print("El primer nombre és: ", num1)
print("El segon nombre és: ", num2, "\n")
print("CANVIII!!")
num3 = num1
num1 = num2
num2 = num3
print("El primer nombre ara és: ", num1)
print("El segon nombre ara és: ", num2)