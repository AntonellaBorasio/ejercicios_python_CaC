""" Actividad Práctica - Python Unidad 1

1) Escribe un programa muestre por pantalla “Hello World”. 

print("Hello World")

---

2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.

print(f"La suma de {3} + {5} es {3 + 5}")

---

3) Escribe un programa que pida el nombre del usuario y escriba un texto que
diga “Hola nombreUsuario”.

userNombre = input('Ingrese su nombre: ')
print(f'Hola {userNombre}')

---

4) Escribe un programa que pida un número, pida otro número y escriba el
resultado de sumar estos dos números.

num1 = int(input('Escriba el primer numero: '))
num2 = int(input('Escriba el segundo numero>: '))
print(f'La suma de {num1} y {num2} es {num1 + num2}')

---

5) Escribe un programa que pida dos números y escriba en la pantalla cual es el
mayor.

num1 = int(input('Escriba el primer numero: '))
num2 = int(input('Escriba el segundo numero>: '))
if num1 > num2:
    print(f'{num1} es mayor que {num2}')
else:
    print(f'{num2} es mayor que {num1}')

---

6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
los tres.

num1 = int(input('Escriba el primer numero: '))
num2 = int(input('Escriba el segundo numero: '))
num3 = int(input('Escriba el tercer numero: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} es mayor que {num2} y {num3}')
elif num2 > num1 and num2 > num3:
    print(f'{num2} es mayor que {num1} y {num3}')
else:
    print(f'{num3} es mayor que {num1} y {num2}')

---

7) Escribe un programa que pida un número y diga si es divisible por 2.

num1 = int(input('Escriba el número: '))

if num1 % 2 == 0:
    print(f'{num1} es divisible por 2')
else:
    print(f'{num1} no es divisible por 2')

---

8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o
7 (sólo hay que comprobar si lo es por uno de los cuatro)

num1 = int(input('Escriba el número: '))

if num1 % 2 == 0:
    print(f'{num1} es divisible por 2')
elif num1 % 3 == 0:
    print(f'{num1} es divisible por 3')
elif num1 % 5 == 0:
    print(f'{num1} es divisible por 5')
elif num1 % 7 == 0:
    print(f'{num1} es divisible por 7')

---

9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay
que decir todos por los que es divisible)

num1 = int(input('Escriba el número: '))
if num1 % 2 == 0 or num1 % 3 == 0 or num1 % 5 == 0 or num1 % 7 == 0:
    if num1 % 2 == 0:
        print(f'{num1} es divisible por 2')
    if num1 % 3 == 0:
        print(f'{num1} es divisible por 3')
    if num1 % 5 == 0:
        print(f'{num1} es divisible por 5')
    if num1 % 7 == 0:
        print(f'{num1} es divisible por 7')
else: 
    print(f'{num1} no es divisible por 2, 3, 5 ni 7')

---

10) Escribir un programa que escriba en pantalla los divisores de un número dado.

num1 = int(input('Escriba el número: '))
for i in range(1, num1+1, 1): # No usar num1 / 2, eso provoca un float. No se puede usar float en range.
    if num1 % i == 0:
        print(f'{num1} es divisible por {i}')

---

11) Escribir un programa que nos diga si un número dado es primo (no es divisible
por ninguno otro número que no sea él mismo o la unidad).

num1 = int(input('Escriba el número: '))

for i in range(2, num1+1, 1):
    if num1 % i == 0 and i != num1:
        print(f'{num1} no es primo')
        break
    elif num1 == i:
        print(f'{num1} es primo')

---

12) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente

num1 = float(input('Escriba el número: '))

if num1 > 0 and num1 <= 3:
    print('Muy deficiente')
elif num1 > 3 and num1 <= 5:
    print('Insuficiente')
elif num1 > 5 and num1 <= 6:
    print('Suficiente')
elif num1 > 6 and num1 <= 7:
    print('Bien')
elif num1 > 7 and num1 <= 9:
    print('Notable')
elif num1 > 9 and num1 <= 10:
    print('Sobresaliente')

---

13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente
forma:
1
22
333
4444
55555
666666
..........

for i in range(1, 31, 1):
    print(f'{i}' * i)

---

14) Haz un programa que escriba una pirámide inversa de los números del 1 al
número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666
55555

4444
333
22
1

num1 = int(input('Escriba el número: '))

for i in range (num1, 0, -1):
    print(f'{i}' * i)

---

15) Crear un programa que escriba los números del 1 al 500, y que indique cuales
son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por
ejemplo:
1
2
3
4 (Múltiplo de 4)
5
------------------------------------------------------------
6
7
8 (Múltiplo de 4)
9 (Múltiplo de 9)


for i in range(1, 501, 1):
    if i % 4 == 0:
        print(f'{i} es divisible por 4')
    elif i % 9 == 0:
        print(f'{i} es divisible por 9')
    elif i % 5 == 0:
        print(f'{i} \n -----------------')
    else:
        print(i) 

        
10 """








