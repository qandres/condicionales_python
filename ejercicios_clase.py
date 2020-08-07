#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))


    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda


    if (numero_1 > numero_2):
        print ('numero_1 es mayor')
    else:
        print ('numero_2 es mayor')



    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

   

    if (numero_1 > 0):
        print ('el numero_1 es positivo')
    else:
        print ('el numero_1 es negativo')   
    if (numero_1 == 0):
        print ('el numero_1 es igual a  0') 


    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 > 0 and numero_1 < 100):
        print ('el numero_1 esta entre 0 - 100') 

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2

    if (numero_1 < 10 or numero_2 > -2):
        print ('cumple con la condicion')
    else:
        print ('no cumple la condicion')

    # Imprima en pantalla si se cumple o no la condición


def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if (texto_1 > texto_2):
        print ('texto_1 es mayor')
    else:
        print ('texto_2 es mayor')

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    texto_1_len = len(texto_1)
    texto_2_len = len (texto_2)
    if (texto_1_len > texto_2_len):
        print(' La primera palabra tiene mayor cantidad de letras')
    else:
        print('La segunda palabra tiene mayor cantidad de letras')
    

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
   
    sub_text1 = texto_1[0:1]
    sub_text2 = texto_2[0:1]
    if (sub_text1 > sub_text2):
        print ('La primera letra de la primera palabra es mayor')
    else:
        print ('La primera letra de la segunda palabra es mayor')

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    if texto_1 == copia_texto_1:
        print('texto_1 es igual a copia_texto_1')


    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
 
    if texto_2 != copia_texto_1:
        print('texto_2 es diferente a copia_texto1')

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = 9

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        if numero_2 > 0:
            print ('Resp=1')
        else:
            print ('Resp=2')

    if numero_1 < 5:
        print ('numero_1 no es mayor a 5')
        if numero_2 > 5:
            print ('Resp=3')
        else:
            print ('Resp=4')

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    if (puntaje > 90 or puntaje == 90) :
        print ('Calificacion A')
    else:
        if (puntaje > 80 or puntaje == 80) :
            print ('Calificacion B')
        elif (puntaje > 70 or puntaje == 70) :
             print ('Calificacion C')
        elif (puntaje > 60 or puntaje == 60) :
            print ('Calificacion D')
        elif (puntaje < 60):
            print ('Calificacion F')
             
    

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados


def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if (texto_1 > texto_2):
        print ('texto_1 es mayor')
    else:
        print ('texto_2 es mayor')
        

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)

    if (int(texto_1) > (int(texto_2))):
        print ('texto_1 es mayor int')
    else:
        print ('texto_2 es mayor int')

    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # texto_2 es mayor porque si lo toma como un string alfaticamente 7 es mayor a 5 al tener una s lo convierte en mayor.
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # porque en este caso los numeros los lee como texto no como enteros siete > cinco tiene una s.
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    ej4()
