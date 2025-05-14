print("**************************")
print("****Bienvenidos a*********")
print("****tienda de mascotas****")
print("**************************")
print("**************************")

num_perros = 10
num_Pajaros = 25
num_gatos = 8
sum_animales = num_perros + num_Pajaros + num_gatos

print("Cual es su nombre?")
nombre = input()
print("Cual es su apellido?")
apellido = input()

#concatenar
nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos ", nombre_completo)

print("selecciona la opcion que deseas ")
print("1: conocer cuantos animales tiene la tienda")
print("2: comprar un animal")

respuesta = int(input())

if respuesta == 1:
    print("actualmente contamos con :")
    print("perros:", num_perros, "gatos:", num_gatos, "pajaros:", num_Pajaros)
    print("en total tenemos : ", sum_animales, "animales")

elif respuesta == 2:
    print("que animal deseas comprar ?")
    animal = input()
    print("Haz comprado un ", animal)
