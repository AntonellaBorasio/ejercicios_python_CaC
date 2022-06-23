""" Actividad Práctica - Python Unidad 2

1) Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según
la fecha sea correcta o no. Realizar también un programa para verificar el
comportamiento de la función.
"""

# Version basica
""" def validar_fecha(d, m, a):
    return d > 0 and d <= 31 and m >= 1 and m <=12 and a >= 1 and a <= 2022 """

# Version no bisiesto
""" def validar_fecha(d,m,a):
    if (m == 1 or m == 3 or m == 5 or m==7 or m==8 or m==10 or m==12) and (d >= 1 and d <= 31) and (a>=1 and a <= 2022):
        return True
    elif (m == 4 or m == 6 or m==9 or m==11) and (d >= 1 and d <= 30) and (a>=1 and a <= 2022):
        return True
    elif m == 2 and d >= 1 and d <= 29 and a>=1 and a <= 2022:
        return True
    else:
        return False """

# Version bisiesto
def validar_fecha(d,m,a):
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

dia=int(input('Escriba un dia: '))
mes=int(input('Escriba un mes: '))
anio=int(input('Escriba un anio: '))
print(validar_fecha(dia, mes, anio))

"""
2) Desarrollar una función que reciba tres números positivos y devuelva el mayor
de los tres.Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
2.1)  Desarrollar  ej1, sólo si éste es único (mayor estricto). En caso de no existir el mayor
estricto devolver -1. 
2.2)  Resolver el ej 1  sin utilizar operadores lógicos (and, or, not). 
 

3) Un comercio de electrodomésticos necesita para su línea de cajas un programa
que le indique al cajero el cambio que debe entregarle al cliente. Para eso se
ingresan dos números enteros, correspondientes al total de la compra y al
dinero recibido. Informar cuántos billetes de cada denominación deben ser
entregados al cliente como vuelto, de tal forma que se minimice la cantidad de
billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la
compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de
$100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.

4) Escribir dos funciones separadas para imprimir por pantalla los siguientes
patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
*****               *                  *   
*****               **                ***   
*****               ***              *****   
*****               ****            *******   
*****               *****          *********


5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo
parámetro. Desarrollar además un programa para verificar el comportamiento
de la función.

6) Crear una función lambda para comprobar si un número es par o impar.
Desarrollar además un programa para verificar el comportamiento de la
función.

7) Crear una lista con los cuadrados de los números entre 1 y N (ambos
incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los
últimos 10 valores de la lista.

8) Eliminar de una lista de palabras que se encuentren en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

9) Escribir una función que reciba una lista como parámetro y devuelva True si la
lista está ordenada en forma ascendente o False en caso contrario. Por
ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
Desarrollar además un programa para verificar el comportamiento de la
función.

10) Desarrollar una función que determine si una cadena de caracteres es capicúa,
sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que
permita verificar su funcionamiento.

11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que
la misma tiene 80 columnas.

12) Escribir una función que reciba como parámetro una tupla conteniendo una
fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha
expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de
Octubre de 2017”. Escribir también un programa para verificar su
comportamiento.

13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las
palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar
las palabras ordenadas según su longitud.

14) Desarrollar una función eliminar_claves() que reciba como parámetros un
diccionario y una lista de claves. La función debe eliminar del diccionario todas
las claves contenidas en la lista, devolviendo el diccionario modificado y un
valor de verdad que indique si la operación fue exitosa. Desarrollar también un
programa para verificar su comportamiento.

15) Escribir una función para eliminar una subcadena de una cadena de
caracteres, a partir de una posición y cantidad de caracteres dados,
devolviendo la cadena resultante. Escribir también un programa para verificar
el comportamiento de la misma. Escribir una función utilizando rebanadas.

"""