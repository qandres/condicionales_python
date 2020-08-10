#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''

    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    resultado = (numero_1 - numero_2)
    if numero_1 < numero_2:
      print (resultado, 'El resultado es Negativo')
    elif (numero_1 == numero_2):
          print ('El resultado es 0')
    elif (numero_1 > numero_2):
        print (resultado, 'El resultado es Positivo')
    
    
        

def ej2():
    print('Ejercicios de práctica con números')


  #Realice un programa que solicite el ingreso de tres números
   # enteros, y luego en cada caso informe si el número es par
    #o impar.
  #Para cada caso imprimir el resultado en pantalla.

  
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    numero_3 = int(input('Ingrese el tercer número:\n'))

    if (numero_1 % 2 == 0):
      print (numero_1 ,'El numero es par')
    else:
         print (numero_1 ,'El numero es impar')
    
    if (numero_2 % 2 == 0):
      print (numero_2 ,'El numero es par')
    else:
         print (numero_2 ,'El numero es impar')

    if (numero_3 % 2 == 0):
      print (numero_3 ,'El numero es par')
    else:
         print (numero_3 ,'El numero es impar')


def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
 
    numero_1 = float(input('Ingrese el primer número:\n'))

    numero_2 = float(input('Ingrese el segundo número:\n'))
    
    operacion = str(input('Ingrese Simbolo de Operacion:\n'))

    suma = (numero_1 + numero_2)

    resta = (numero_1 - numero_2)

    multiplicacion = (numero_1 * numero_2)

    division = (numero_1 / numero_2)

    exponente = (numero_1 ** numero_2)

    if (operacion == "+"):
      print ('El resultado es', suma)
    
    if (operacion == "-"):
      print ('El resultado es', resta)
    
    if (operacion == "*"):
      print ('El resultado es', multiplicacion)
    
    if (operacion == "/"):
      print ('El resultado es', division)
    
    if (operacion == "**"):
      print ('El resultado es', exponente)




def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
  '''
    print ('Ingrese 3 palabras que desee ordernar')

    palabra_1 = str(input('Ingrese primera palabra:\n'))

    palabra_2 = str(input('Ingrese segunda palabra:\n'))
    
    palabra_3 = str(input('Ingrese tercera palabra:\n'))

    palabra_1_len = len(palabra_1)

    palabra_2_len = len(palabra_2)

    palabra_3_len = len(palabra_3)

    orden = int (input ('Ingrese 1 para orden Alfabetico o Ingrese 2 para ordenar por Cantidad de Letras:\n'))
    
    if (orden == 1) and (palabra_1 > palabra_2) and (palabra_2 > palabra_3):
      print(palabra_1, palabra_2, palabra_3)
    elif (orden == 1) and (palabra_1 > palabra_3) and (palabra_3 > palabra_2):
      print (palabra_1, palabra_3, palabra_2)
    elif (orden == 1) and (palabra_2 > palabra_1) and (palabra_1 > palabra_3):
      print (palabra_2, palabra_1, palabra_3)
    elif (orden == 1) and (palabra_2 > palabra_3) and (palabra_3 > palabra_1): 
      print (palabra_2, palabra_3, palabra_1)
    elif (orden == 1) and (palabra_3 > palabra_2) and (palabra_2 > palabra_1):
      print (palabra_3, palabra_2, palabra_1)
    elif (orden == 1) and (palabra_3 > palabra_1) and (palabra_1 > palabra_2):
      print (palabra_3, palabra_1, palabra_2)

    if (orden ==2) and (palabra_1_len >  palabra_2_len) and (palabra_2_len > palabra_3_len):
      print (palabra_1, palabra_2, palabra_3)
    elif (orden ==2) and (palabra_1_len >  palabra_3_len) and (palabra_3_len > palabra_2_len):
      print (palabra_1, palabra_3, palabra_2)
    elif (orden ==2) and (palabra_2_len >  palabra_1_len) and (palabra_1_len > palabra_3_len):
      print (palabra_2, palabra_1, palabra_3)
    elif (orden ==2) and (palabra_2_len >  palabra_3_len) and (palabra_3_len > palabra_1_len):
      print (palabra_2, palabra_3, palabra_1)
    elif (orden ==2) and (palabra_3_len >  palabra_2_len) and (palabra_2_len > palabra_1_len):
      print (palabra_3, palabra_2, palabra_1)
    elif (orden ==2) and (palabra_3_len >  palabra_1_len) and (palabra_1_len > palabra_2_len):
      print (palabra_3, palabra_1, palabra_2)
    

     
def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

    temperatura_1 = float(input('Ingrese primera temperatura:\n'))

    temperatura_2 = float(input('Ingrese segunda temperatura:\n'))
    
    temperatura_3 = float(input('Ingrese tercera temperatura:\n'))

    suma = (temperatura_1 + temperatura_2 + temperatura_3)

    promedio = (suma / 3)

    if (temperatura_1 > temperatura_2) and (temperatura_2 > temperatura_3):
      print(temperatura_1, 'Es la temperatura maxima','y', temperatura_3, 'Es la temperatura minima', ', el promedio es =', promedio)
    elif (temperatura_1 > temperatura_3) and (temperatura_3 > temperatura_2):
      print (temperatura_1, 'Es la temperatura maxima','y', temperatura_2, 'Es la temperatura minima', ', el promedio es =', promedio)
    elif (temperatura_2 > temperatura_1) and (temperatura_1 > temperatura_3):
      print (temperatura_2, 'Es la temperatura maxima','y', temperatura_3, 'Es la temperatura minima', ', el promedio es =', promedio)
    elif (temperatura_2 > temperatura_3) and (temperatura_3 > temperatura_1): 
      print (temperatura_2, 'Es la temperatura maxima','y', temperatura_1, 'Es la temperatura minima', ', el promedio es =', promedio)
    elif (temperatura_3 > temperatura_2) and (temperatura_2 > temperatura_1):
      print (temperatura_3,'Es la temperatura maxima','y', temperatura_1, 'Es la temperatura minima', ', el promedio es =', promedio)
    elif (temperatura_3 > temperatura_1) and (temperatura_1 > temperatura_2):
      print (temperatura_3,'Es la temperatura maxima','y', temperatura_2, 'Es la temperatura minima', ', el promedio es =', promedio)
    elif (temperatura_1 == temperatura_2) and (temperatura_2 == temperatura_3):
      print( 'Las temperaturas son iguales', 'el promedio es =', promedio)  

    


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
