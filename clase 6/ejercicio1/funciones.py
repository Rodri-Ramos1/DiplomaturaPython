import math

#Calculadora con funciones y valores ingresados por el usuario
def opciones():
    print("1- suma")
    print("2- resta")
    print("3- multiplicacion")
    print("4- division")
    print("5- potencia")
    print("6- raiz cuadrada")
    print("7- seno")
    opcion = int(input("Ingrese la opcion: "))
    return opcion

def suma():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = numero1 + numero2
    return resultado

def resta():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = numero1 - numero2
    return resultado

def multiplicar():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = numero1 * numero2
    return resultado

def division():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = numero1 / numero2
    return resultado

def potencia():
    numero = int(input("Ingrese un número: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = numero ** exponente
    return resultado

def raizCuadrada():
    numero = int(input("Ingrese un número: "))
    resultado = math.sqrt(numero)
    return resultado

def seno():
    numero = int(input("Ingrese un número: "))
    resultado = math.sin(numero)
    return resultado