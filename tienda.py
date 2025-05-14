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


print("actualmente contamos con :")
print("perros:", num_perros, "gatos:", num_gatos, "pajaros:", num_Pajaros)
print("en total tenemos : ", sum_animales, "animales")