"""
TRABAJO PRÁCTICO INTEGRADOR MATEMÁTICA-PROGRAMACIÓN
Comision 24 - Grupo Verde
Integrantes:
- Facundo Arrieta
- Jose Matias Alvarez
- Azcuy Nicolas
- Luciano Andrelo
- Jeremias Apiani
"""

from datetime import datetime

# PARTE A. OPERACIONES CON DNIs

def digitos_unicos(numero):
    """
    Recibe un número y devuelve una lista con sus dígitos únicos,
    sin repetir, en el orden en que aparecen.
    """
    unicos = []                # Lista vacía para guardar dígitos únicos
    for i in str(numero):      # Convertimos el número a texto para iterar cada dígito
        if i not in unicos:    # Comprobamos que el número no este en la lista.
            unicos.append(i)   # Lo agregamos al final con append()
    return unicos              # Devolvemos la lista final


def pedir_dni():
    """
    Pide al usuario ingresar un DNI válido (solo números positivos).
    """
    while True:
        dni_input = input("Ingrese un DNI (solo números): ").strip()  # Pedimos DNI y quitamos espacios
        if dni_input.isdigit() and int(dni_input) > 0:
            # isdigit() verifica que sean solo números
            # int(dni_input) > 0 asegura que no sea 0 ni negativo
            return int(dni_input)  # Convertimos a entero y lo devolvemos
        else:
            print("Error: Debe ingresar solo números positivos. Intente de nuevo.")

def contar_frecuencia_digitos(numero):
    """
    Devuelve un diccionario con la frecuencia de cada dígito.
    """
    frecuencia = {}
    for i in str(numero):
        frecuencia[i] = frecuencia.get(i, 0) + 1
    return frecuencia


def sumar_digitos(numero):
    """
    Suma total de los dígitos de cada DNI.
    """
    return sum(int(i) for i in str(numero))


# Código principal

dni = pedir_dni()  # Llamamos a pedir_dni() → el usuario ingresa un DNI válido

digitos = digitos_unicos(dni)  # Llamamos a digitos_unicos() para obtener los dígitos sin repetir

# Mostramos los resultados en pantalla
print(f"DNI ingresado: {dni}")
print("Dígitos únicos:", " ".join(digitos))  # join une los dígitos con espacios para mostrar


######

def operaciones_logicas_dni(dni1, dni2):
    """
    Realiza operaciones lógicas con los dígitos únicos de dos DNIs:
    unión, intersección, diferencia y diferencia simétrica.
    """

    def digitos_unicos(numero):
        """
        Recibe un número y devuelve una lista con sus dígitos únicos,
        es decir, sin repetir. Mantiene el orden en que aparecen.
        """
        unicos = []  # Lista vacía donde guardaremos los dígitos únicos
        for i in str(numero):  # Convertimos el número a string para iterar cada dígito
            if i not in unicos:  # Si el dígito no está ya en la lista
                unicos.append(i)  # append agrega ese dígito al final de la lista
        return unicos  # Devolvemos la lista con dígitos sin repetir
    
    

    # Obtener dígitos únicos de cada DNI usando la función auxiliar
    d1 = digitos_unicos(dni1)
    d2 = digitos_unicos(dni2)

    """
    Unión:
    Conjunto de dígitos que aparecen en dni1 o en dni2 (sin repetir).
    Es decir, todos los dígitos presentes en al menos uno de los dos DNIs.
    """
    union = d1.copy()  # copy() crea una copia independiente de la lista d1
    for i in d2:
        if i not in union:
            union.append(i)  # Agregamos dígitos de d2 que no están en d1

    """
    Intersección:
    Conjunto de dígitos que aparecen tanto en dni1 como en dni2.
    Son los dígitos comunes a ambos DNIs.
    """
    interseccion = []
    for i in d1:
        if i in d2 and i not in interseccion:
            interseccion.append(i)

    """
    Diferencia (dni1 - dni2):
    Conjunto de dígitos que están en dni1 pero NO en dni2.
    Representa los dígitos exclusivos de dni1.
    """
    diferencia = []
    for i in d1:
        if i not in d2:
            diferencia.append(i)

    """
    Diferencia simétrica:
    Conjunto de dígitos que están en dni1 o en dni2 pero NO en ambos.
    Es decir, todos los dígitos que no comparten ambos DNIs.
    """
    diferencia_simetrica = []
    for i in d1:
        if i not in d2:
            diferencia_simetrica.append(i)
    for i in d2:
        if i not in d1 and i not in diferencia_simetrica:
            diferencia_simetrica.append(i)

    # Ordenar las listas para presentación ordenada
    union.sort()           
    interseccion.sort()
    diferencia.sort()
    diferencia_simetrica.sort()

    # Mostrar resultados
    print("="*40)
    print(f"DNI 1: {dni1} → Dígitos únicos: {' '.join(d1)}")
    print(f"DNI 2: {dni2} → Dígitos únicos: {' '.join(d2)}")
    print("-"*40)
    print("Unión:                 ", " ".join(union))
    print("Intersección:          ", " ".join(interseccion))
    print("Diferencia (DNI1 - DNI2):", " ".join(diferencia))
    print("Diferencia simétrica:  ", " ".join(diferencia_simetrica))
    print("="*40)
    f1, f2 = contar_frecuencia_digitos(dni1), contar_frecuencia_digitos(dni2)
    s1, s2 = sumar_digitos(dni1), sumar_digitos(dni2)
    print(f"Frecuencia DNI1: {f1} -->> Suma: {s1}")
    print(f"Frecuencia DNI2: {f2} -->> Suma: {s2}\n")
    print("="*40)

def pedir_dnis():
    """
    Pide al usuario que ingrese dos DNIs y valida que sean números positivos
    sin ceros y solo dígitos.
    Devuelve ambos DNIs como enteros.
    """
    while True:
        dni1_input = input("Ingrese el primer DNI (solo números): ").strip()
        dni2_input = input("Ingrese el segundo DNI (solo números): ").strip()

        # isdigit() verifica que toda la cadena sea solo dígitos numéricos
        if not dni1_input.isdigit():
            print("Error: El primer DNI debe contener solo números. Intente nuevamente.")
            continue
        if not dni2_input.isdigit():
            print("Error: El segundo DNI debe contener solo números. Intente nuevamente.")
            continue

        dni1 = int(dni1_input)  # Convertimos la cadena a entero
        dni2 = int(dni2_input)

        # Validamos que los DNIs sean positivos y diferentes de cero
        if dni1 == 0 or dni2 == 0:
            print("Error: Los DNIs deben ser números positivos distintos de cero.")
            continue

        return dni1, dni2  # Retornamos los DNIs válidos


def arrancar():
    """
    Función principal que pide los DNIs y muestra los resultados de las operaciones.
    """
    dni1, dni2 = pedir_dnis()
    operaciones_logicas_dni(dni1, dni2)

arrancar()

######################################################################################

ANIOS_NACIMIENTO = [1999, 2003, 1991, 1988, 1989]

# PARTE B. OPERACIONES CON AÑOS DE NACIMIENTOS

# Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
def anios_par_o_impar(anios_nacimiento):
  anios_pares = 0
  anios_impares = 0
  for anio in anios_nacimiento:
    if anio % 2 == 0:
      anios_pares += 1
    else:
      anios_impares += 1
  print(f"Hay {anios_pares} años pares y {anios_impares} años impares") 

# Si todos nacieron después del 2000, mostrar "Grupo Z".
def nacidos_desp_2000(anios_nacimiento):
  cont = 0
  for anio in anios_nacimiento:
    if anio >= 2000:
      cont += 1
  if cont == len(anios_nacimiento):
    print("Grupo Z")
  else:
    print("No es Grupo Z")

# Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
# Implementar funcion para ver si el año es bisiesto
def es_bisiesto(anio_nacimineto):
  if (anio_nacimineto % 4 == 0): 
    return True
  return False

def anios_especiales(anio_nacimineto):
  cont = 0
  for anio in anio_nacimineto:
    bisiesto = es_bisiesto(anio)
    if (bisiesto and cont == 0):
      cont += 1
      print(f'Tenemos un año especial {anio}')
    elif (bisiesto):
      print(f'Tenemos otro año especial {anio}')

# Cacula la edad en base a su año de nacimiento
def calcular_edad(anios_nacimiento):
  anio_actual = datetime.now().year
  edad_actual = []
  for anio in anios_nacimiento:
    edad_actual.append(anio_actual - anio)
  return edad_actual

# Cacula el producto carteciano entre años y edades actuales
def calc_producto_cartesiano(anios_nacimiento):
  producto_cartesiano = ''
  for i in range(len(anios_nacimiento)):
    if (i == 0):
      producto_cartesiano += '{'
    for j in range(len(calcular_edad(anios_nacimiento))):
      producto = f' ({anios_nacimiento[i]}, {calcular_edad(anios_nacimiento)[j]}) '
      producto_cartesiano += producto
    print(i, len(anios_nacimiento))
    if (i == len(anios_nacimiento) -1):
      producto_cartesiano += '}'
  print(f"El producto cartesiano es:\n {producto_cartesiano}")

def main():
  anios_par_o_impar(ANIOS_NACIMIENTO)
  nacidos_desp_2000(ANIOS_NACIMIENTO)
  anios_especiales(ANIOS_NACIMIENTO)
  calc_producto_cartesiano(ANIOS_NACIMIENTO)

main()