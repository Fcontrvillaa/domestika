print("bienvenido al conversor de millas a km")

print("escribe un numero en millas :")
millas = input()  #string

print("tipo de datos:", type(millas))
millas = float(millas)
print("tipo de datos:", type(millas))

#1 milla = 1609 kms

kilometros = millas * 1.609

print("millas ingresadas :", millas)
print("equivale a :", kilometros)