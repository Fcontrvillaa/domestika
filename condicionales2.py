print ("escribe tu nombre :")
nombre = input()
print("escribe tu edad :")
edad = int(input())


#elif
#operadores logicos

if nombre == "Fernando" and edad >= 20:
    print("Saludos Fernadno, eres un adulto")
elif nombre == "Fernando" and edad < 20:
    print("Saludos Fernadno, eres un joven")
else:
    print("saludos")
