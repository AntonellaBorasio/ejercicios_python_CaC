''' Actividad Práctica - Python Unidad 2

1) Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según
la fecha sea correcta o no. Realizar también un programa para verificar el
comportamiento de la función.


# Versión basica

def validar_fecha(d, m, a):
    return d > 0 and d <= 31 and m >= 1 and m <=12 and a >= 1 and a <= 2022


# Versión para años no bisiestos

def validar_fecha(d,m,a):
"""Validación de fechas, sin tener en cuenta los bisiestos"""
    if (m == 1 or m == 3 or m == 5 or m==7 or m==8 or m==10 or m==12) and (d >= 1 and d <= 31) and (a>=1 and a <= 2022):
        return True
    elif (m == 4 or m == 6 or m==9 or m==11) and (d >= 1 and d <= 30) and (a>=1 and a <= 2022):
        return True
    elif m == 2 and d >= 1 and d <= 29 and a>=1 and a <= 2022:
        return True
    else:
        return False


# Versión con años bisiestos

def validar_fecha(d,m,a):
    """Validación de fechas teniendo en cuenta si el año es o no bisiesto"""
    if (m == 1 or m == 3 or m == 5 or m==7 or m==8 or m==10 or m==12) and (d >= 1 and d <= 31) and (a>=1 and a <= 2022):
        return True
    elif (m == 4 or m == 6 or m==9 or m==11) and (d >= 1 and d <= 30) and (a>=1 and a <= 2022):
        return True
    elif m == 2 and d >= 1 and d <= 29 and a>=1 and a <= 2022 and ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0):
        return True
    elif m == 2 and d >= 1 and d <= 28 and a>=1 and a <= 2022 and (a % 4 != 0 and a % 100 == 0):
        return True
    else:
        return False


# Variables y print de la función

dia=int(input('Escriba un dia: '))
mes=int(input('Escriba un mes: '))
anio=int(input('Escriba un anio: '))
print(validar_fecha(dia, mes, anio))

---

2) Desarrollar una función que reciba tres números positivos y devuelva el mayor
de los tres. Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
2.1)  Desarrollar  ej1, sólo si éste es único (mayor estricto). En caso de no existir el mayor
estricto devolver -1. 
2.2)  Resolver el ej 1  sin utilizar operadores lógicos (and, or, not).


# Parte 1: comparación de 3 números diferentes
def mayor_numero(n1, n2, n3):
    """ Determina y devuelve el número que sea mayor """
    max = 0
    if n1 > n2 and n1 > n2:
        max = n1
    elif n2 > n3:
        max = n2
    else:
        max = n3
    return max

# Parte 2 y 3: comparación de 3 números, con o sin mayor estricto, sin operadores lógicos
def mayor_estricto(n1, n2, n3):
    """ Determina y devuelve el número que sea mayor """
    max = 0
    lista = [n1, n2, n3]
    lista.sort(reverse=True)
    if(lista[0] == lista[1]):
        max = 'No hay mayor estricto'
    else:
        max = lista[0]
    return max

num1=int(input('Escriba un número: '))
num2=int(input('Escriba un número: '))
num3=int(input('Escriba un número: '))
print(mayor_numero(num1, num2, num3))
print(mayor_estricto(num1, num2, num3))

---

3) Un comercio de electrodomésticos necesita para su línea de cajas un programa
que le indique al cajero el cambio que debe entregarle al cliente. Para eso se
ingresan dos números enteros, correspondientes al total de la compra y al
dinero recibido. Informar cuántos billetes de cada denominación deben ser
entregados al cliente como vuelto, de tal forma que se minimice la cantidad de
billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la
compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de
$100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.

¿valor_producto = int(input('Valor del producto: '))
dinero_entregado = int(input('Dinero entregado por el cliente: '))
billetes = [500, 100, 50, 20, 10, 5, 1]
vuelto = dinero_entregado - valor_producto
cambio = []

if valor_producto > dinero_entregado:
    print('No es dinero suficiente')
else:
    for i in range(0, len(billetes), 1):
        cambio.append(vuelto // billetes[i])
        vuelto = vuelto % billetes[i]
        print(f'Se debe devolver {cambio[i]} billetes de {billetes[i]}')

---

4) Escribir dos funciones separadas para imprimir por pantalla los siguientes
patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
*****               *                  *   
*****               **                ***   
*****               ***              *****   
*****               ****            *******   
*****               *****          *********

def patron(n):
    for i in range(1, n+1, 1):
        print(("*"* 5).ljust(10, " "), ("*" * i).ljust(10, " "), ("*" * (i*2-1)).center(10, " "))

patron(5)

---

5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo
parámetro. Desarrollar además un programa para verificar el comportamiento
de la función.

cuadrado = lambda x: x**2
print(cuadrado(10))

---

6) Crear una función lambda para comprobar si un número es par o impar.
Desarrollar además un programa para verificar el comportamiento de la
función.

numero_par = lambda x: x % 2 == 0 
print(numero_par(4))

---

7) Crear una lista con los cuadrados de los números entre 1 y N (ambos
incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los
últimos 10 valores de la lista.

cuadrados = []

def lista_cuadrados(n):
    if n > 0:
        for i in range(1, n+1, 1):
            cuadrados.append(i**2)
        return f'Los cuadrados son: {cuadrados} y los últimos 10 cuadrados de la lista son: {cuadrados[-10:]}'
    else:
        return 'No es un número entero positivo'


n = int(input('Escribe un número entero positivo: '))
print(lista_cuadrados(n))

---

8) Eliminar de una lista de palabras que se encuentren en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

def lista_resultado(lista_original, lista_eliminada):
    resultante = lista_original[:]
    for i in range (0, len(lista_eliminada), 1):
        while lista_eliminada[i] in resultante:
           resultante.remove(lista_eliminada[i])
    return f'La diferencia entre {lista_original} y {lista_eliminada} es {resultante}'

print(lista_resultado([1, 2, 3, 4, 5], [2, 3]))

---

9) Escribir una función que reciba una lista como parámetro y devuelva True si la
lista está ordenada en forma ascendente o False en caso contrario. Por
ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
Desarrollar además un programa para verificar el comportamiento de la
función.

def lista_ordenada(lista):
    copia_lista = lista[:]
    copia_lista.sort()
    return lista == copia_lista

lista1 = list(input('Determine los elementos de la lista: '))
print(lista_ordenada(lista1))

---

10) Desarrollar una función que determine si una cadena de caracteres es capicúa,
sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que
permita verificar su funcionamiento.

def es_palindromo(cad):
    for i in range(0, int(len(cad)/2)):
        if cad[i] != cad[len(cad)-i-1]:
            return ('No es palíndromo.')
    return ('Es palíndromo.')

cadena = input('Escribe una palabra o frase: ')
print(es_palindromo(cadena))

---

11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que
la misma tiene 80 columnas.

cad = input('Escribir una cadena: ')
print(cad.center(80," "))

---

12) Escribir una función que reciba como parámetro una tupla conteniendo una
fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha
expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de
Octubre de 2017”. Escribir también un programa para verificar su
comportamiento.

def fecha_ext(fecha):
    return f'{fecha[0]} de {fecha[1]} de {fecha[2]}'

dia = int(input('Ingrese un dia: '))
mes = input('Ingrese un mes: ')
anio = int(input('Ingrese un anio: '))
fecha = (dia,mes,anio)
print(fecha_ext(fecha))

---

13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las
palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar
las palabras ordenadas según su longitud.

def comparar_frase(frase):
    conjunto1 = set(frase)
    conjunto2 = set(frase)
    dif = list(conjunto1 & conjunto2)    
    dif.sort(key=len)
    return dif
    
cad = (input('Ingrese una frase: ').split(' '))
print(comparar_frase(cad))
comparar_frase(cad)

---

14) Desarrollar una función eliminar_claves() que reciba como parámetros un
diccionario y una lista de claves. La función debe eliminar del diccionario todas
las claves contenidas en la lista, devolviendo el diccionario modificado y un
valor de verdad que indique si la operación fue exitosa. Desarrollar también un
programa para verificar su comportamiento.

def eliminar_claves(dicc, claves):
    for i in range(0, len(claves), 1):
        dicc.pop(claves[i], None)
    return dicc

dic = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
lista_claves = ['uno', 'dos']
print(eliminar_claves(dic, lista_claves))

---

15) Escribir una función para eliminar una subcadena de una cadena de
caracteres, a partir de una posición y cantidad de caracteres dados,
devolviendo la cadena resultante. Escribir también un programa para verificar
el comportamiento de la misma. Escribir una función utilizando rebanadas.

def eliminar_porcion(cad, pos, cant):
    lista = list(cad)
    for i in range(pos, pos+cant, 1):
        lista.pop(pos)
    return "".join(lista)



cadena = input('Introduzca una cadena: ')
posicion = int(input('Introduzca indice desde donde borrar: '))
cantidad = int(input('Introduzca cantidad de caracteres a borrar: '))
print(eliminar_porcion(cadena, posicion, cantidad))

'''