# -	Si el numero 3 aparece en al menos cuatro conjuntos y el promedio del conjunto D es divisible por 3, 
# entonces se considera un digito central. 

# Conjuntos 
A = [1, 2, 4, 8]
B = [0, 3, 4, 6, 8, 9]
C = [1, 3, 4, 5]
D = [1, 3, 4, 7, 9]
E = [3, 5, 6, 7, 8, 9]

conjuntos = [A, B, C, D, E]

# Contamos en cuántos conjuntos aparece el numero 3
cont = 0
for i in conjuntos:
    if 3 in i:
        cont += 1

# promedio entero del conjunto D
prom_D = sum(D) // len(D)

# Verificar si el promedio entero es divisible por 3
es_div_por_3 = prom_D % 3 == 0

# Evaluar ambas condiciones
if cont >= 4 and es_div_por_3:
    print("El numero 3 es un dígito central")
else:
    print("El numero 3 no cumple las condiciones para ser un dígito central")


# -	Si el conjunto C tiene más elementos que el conjunto A, y el conjunto E tiene al menos dos números pares, 
# entonces se considera que hay una distribución compensada.

# Conjuntos 
A = [1, 2, 4, 8]
B = [0, 3, 4, 6, 8, 9]
C = [1, 3, 4, 5]
D = [1, 3, 4, 7, 9]
E = [3, 5, 6, 7, 8, 9]

# chequear si C tiene más elementos que A
condicion1 = len(C) > len(A)

# ver cuántos números pares hay en E
cont_pares_E = 0
for numero in E:
    if numero % 2 == 0:
        cont_pares_E += 1

# vemos si hay al menos dos pares en E
condicion2 = cont_pares_E >= 2

# evaluamos la expresión compuesta
if condicion1 and condicion2:
    print("Hay distribución compensada") 
else:
    print("No hay distribución compensada")  

# imprimimos los valores intermedios
print(f"C tiene {len(C)} elementos; A tiene {len(A)} elementos.")
print(f"E contiene {cont_pares_E} números pares.")
