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

import time # Importamos la librería time para usar time.sleep()
from datetime import datetime

# --- FUNCIONES DE UTILIDAD ---
def imprimir_lento(texto, retardo=0.01):
    """
    Imprime el texto carácter por carácter con un retardo.
    """
    #Función imprimir_lento(texto, retardo=0.01):
    for char in texto:
        print(char, end='', flush=True) # end='' evita el salto de línea automático, haciendo que los caracteres se impriman uno al lado del otro. flush=True asegura que el carácter se muestre inmediatamente en la consola, sin esperar a que el búfer se llene.
        time.sleep(retardo) # Pausa por un breve momento
    print() # Salto de línea al final del texto

def imprimir_seccion_lenta(titulo):
    """
    Imprime un título de sección de forma lenta.
    """
    imprimir_lento("\n" + "=" * 50, retardo=0.005)
    imprimir_lento(f"--- {titulo} ---", retardo=0.01)
    imprimir_lento("=" * 50 + "\n", retardo=0.005)


# --- PARTE A. OPERACIONES CON DNIs ---

# Lista de DNIs
DNI_LIST = [44828142, 34686890, 34553441, 41791139, 38566798]

# Función de digitos únicos.
def digitos_unicos(numero):
    """
    Recibe un número y devuelve una lista con sus dígitos únicos,
    sin repetir. Mantiene el orden en que aparecen.
    """
    unicos = []
    for i in str(numero):
        if i not in unicos:
            unicos.append(i)
    return unicos

# Función de operaciones lógicas.
def operaciones_logicas_dni(dni1, dni2):
    """
    Realiza operaciones lógicas con los dígitos únicos de dos DNIs:
    unión, intersección, diferencia y diferencia simétrica.
    """
    d1 = digitos_unicos(dni1)
    d2 = digitos_unicos(dni2)

    # Unión
    union = d1.copy()
    for i in d2:
        if i not in union:
            union.append(i)

    # Intersección
    interseccion = []
    for i in d1:
        if i in d2 and i not in interseccion:
            interseccion.append(i)

    # Diferencia (dni1 - dni2)
    diferencia = []
    for i in d1:
        if i not in d2:
            diferencia.append(i)

    # Diferencia simétrica
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

    # Mostrar resultados (usando imprimir_lento)
    imprimir_lento("=" * 50)
    imprimir_lento(f"DNI 1: {dni1} → Dígitos únicos: {' '.join(d1)}")
    imprimir_lento(f"DNI 2: {dni2} → Dígitos únicos: {' '.join(d2)}")
    imprimir_lento("-" * 50)
    imprimir_lento("Unión:                       " + " ".join(union))
    imprimir_lento("Intersección:                " + " ".join(interseccion))
    imprimir_lento("Diferencia (DNI1 - DNI2):    " + " ".join(diferencia))
    imprimir_lento("Diferencia simétrica:        " + " ".join(diferencia_simetrica))
    imprimir_lento("=" * 50)
    time.sleep(0.5) # Pausa al final de cada operación para que se aprecie la sección
    print()


# Devuelve un diccionario con la frecuencia de cada dígito.
def contar_frecuencia_digitos(numero):
    frecuencia = {}
    for i in str(numero):
        frecuencia[i] = frecuencia.get(i, 0) + 1
    return frecuencia

# Suma total de los dígitos de cada DNI.
def sumar_digitos(numero):
    return sum(int(i) for i in str(numero))

# Compara los pares posibles de la lista de DNIs
def ejecutar_operaciones_logicas_dnis():
    imprimir_seccion_lenta("OPERACIONES LÓGICAS ENTRE PARES DE DNI")
    total = len(DNI_LIST)
    for i in range(total):
        for j in range(i + 1, total):
            operaciones_logicas_dni(DNI_LIST[i], DNI_LIST[j])

def ejecutar_analisis_individual_dnis():
    imprimir_seccion_lenta("ANÁLISIS INDIVIDUAL DE DNIS")

    for dni in DNI_LIST:
        imprimir_lento(f"--- DNI: {dni} ---")
        imprimir_lento(f"  Dígitos únicos: {digitos_unicos(dni)}")
        imprimir_lento(f"  Frecuencia de dígitos: {contar_frecuencia_digitos(dni)}")
        imprimir_lento(f"  Suma de dígitos: {sumar_digitos(dni)}")
        imprimir_lento("-" * 30 + "\n", retardo=0.005) # Separador más rápido para cada DNI
        time.sleep(0.3) # Pequeña pausa entre DNI para mejor visualización

# --- EVALUACIÓN DE CONDICIONES EN CONJUNTOS PREDETERMINADOS ---
# Conjuntos
A = [1, 2, 4, 8]
B = [0, 3, 4, 6, 8, 9]
C = [1, 3, 4, 5]
D = [1, 3, 4, 7, 9]
E = [3, 5, 6, 7, 8, 9]

conjuntos = [A, B, C, D, E] 

def ejecutar_evaluacion_condicionales():
    imprimir_seccion_lenta("EVALUACIÓN DE CONDICIONES EN CONJUNTOS PREDETERMINADOS")

    # --- Condición: El número 3 es un dígito central ---
    imprimir_lento(">>> Verificando si el número 3 es un dígito central...\n", retardo=0.02)
    time.sleep(0.5)

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
        imprimir_lento(f"✅ ¡El número 3 es un dígito central!")
        imprimir_lento(f"   (Aparece en {cont} conjuntos y el promedio de D ({prom_D}) es divisible por 3).", retardo=0.008)
    else:
        imprimir_lento(f"❌ El número 3 no cumple las condiciones para ser un dígito central.")
        imprimir_lento(f"   (Aparece en {cont} conjuntos, se requieren 4. El promedio de D es {prom_D}, ¿es divisible por 3? {es_div_por_3}).", retardo=0.008)

    imprimir_lento("\n" + "-" * 50 + "\n", retardo=0.005)
    time.sleep(0.5)

    # --- Condición: Distribución Compensada ---
    imprimir_lento(">>> Verificando si hay distribución compensada...\n", retardo=0.02)
    time.sleep(0.5)

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
        imprimir_lento(f"✅ ¡Hay distribución compensada!")
        imprimir_lento(f"   (C tiene {len(C)} elementos, A tiene {len(A)}. E contiene {cont_pares_E} números pares).", retardo=0.008)
    else:
        imprimir_lento(f"❌ No hay distribución compensada.")
        imprimir_lento(f"   (C tiene {len(C)} elementos; A tiene {len(A)}. E contiene {cont_pares_E} números pares).", retardo=0.008)

    imprimir_lento("\n" + "=" * 50 + "\n", retardo=0.005)
    time.sleep(0.5)

# --- MENÚ PRINCIPAL ---
def mostrar_menu():
    imprimir_lento("\n" + "=" * 50, retardo=0.005)
    imprimir_lento("--- MENÚ PRINCIPAL ---", retardo=0.01)
    imprimir_lento("=" * 50, retardo=0.005)
    imprimir_lento("1. Realizar Operaciones Lógicas con DNIs", retardo=0.01)
    imprimir_lento("2. Realizar Análisis Individual de DNIs", retardo=0.01)
    imprimir_lento("3. Evaluar Condiciones Especiales en Conjuntos", retardo=0.01)
    imprimir_lento("4. Salir", retardo=0.01)
    imprimir_lento("=" * 50, retardo=0.005)

def main():
    while True:
        mostrar_menu()
        opcion = input("Por favor, elija una opción (1-4): ").strip()
        time.sleep(0.2) # Pequeña pausa después de que el usuario ingresa la opción

        if opcion == '1':
            ejecutar_operaciones_logicas_dnis()
        elif opcion == '2':
            ejecutar_analisis_individual_dnis()
        elif opcion == '3':
            ejecutar_evaluacion_condicionales()
        elif opcion == '4':
            imprimir_lento("Saliendo del programa. ¡Hasta pronto!", retardo=0.02)
            break
        else:
            imprimir_lento("Opción no válida. Por favor, intente de nuevo con un número entre 1 y 4.", retardo=0.02)
        time.sleep(1) # Pausa más larga antes de volver al menú


# Ejecutar el menú principal al iniciar el script
if __name__ == "__main__":
    main()

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