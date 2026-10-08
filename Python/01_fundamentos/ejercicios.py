# Ejercicio 1
# Crea una variable con tu nombre y una con tu edad. Imprime un mensaje que diga:
# "Me llamo X y tengo Y años"
nombre = "Santiago"
edad = 20
ciudad = "Bogota"
años = 18
precio = 1800.50
cantidad = 4

print("Me llamo", nombre, "y tengo", edad, "años")
print("Vivo en", ciudad, "hace" , años, "años")
print("El precios es" , precio, "y compre", cantidad, "unidades")
print("El total es", precio * cantidad)
print(type(nombre))
print(type(edad))
print(type(ciudad))
print(type(años))
print(type(precio))
print(type(cantidad))
# Ejercicio 2
# Crea dos variables numéricas y calcula su suma, resta, multiplicación y división.
# Imprime cada resultado.

a = 14
b = 11
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)  
print(type(a))
print(type(b))


# Ejercicio 3
# Crea una variable "precio" (float) y una variable "cantidad" (int).
# Calcula e imprime el total (precio * cantidad).
precio = 19.99
cantidad = 5
print("Total:", precio * cantidad)


# Ejercicio 4
# Usa type() para imprimir el tipo de cada variable que creaste arriba.
print(type(precio))
print(type(cantidad))


#Ejercios extras
precio_producto = 1500.75
descuento = 0.15
precio_final = precio_producto * (1 - descuento)
print(precio_final)

base = 5
altura = 10
area = base * altura
print("El area es", area)

