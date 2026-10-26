num1 = int(input("Introduiex el primer nombre "))
num2 = int(input("Introdueix el segon nombre "))
if (num1 + num2) > 10:
    print("La suma és major que 10")
else:
    print("La suma és menor o igual que 10")

#Nou programa

if ((num1 + num2) > 8) or ((num1 + num2) < 4):
    print("La suma és major que 8 o menor que 4")
    if ((num1 + num2) > 14) and ((num1 + num2) < 18):
        print("La suma està entre 14 i 18")
        if ((num1 + num2) == 15):
            print("La suma és 15")
        else:
            print("La suma no és 15")
    else:
        print("La suma no està entre 14 i 18")
else:
    print("La suma és entre 4 i 8")
