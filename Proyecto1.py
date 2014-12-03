#coding: utf-8

import random
print "*"*70
print "*"*70
print "Bienveido al menu principal"
print """Intruccciones : El juego consiste en adivinar un numero generado aleatoriamente y solo tendras 3 intentos  pasaras por  3 niveles que son : 
    * Facil
    * Medio
en el nivel facíl el numero que se genera esta en el rango del 1 al 5 si aciertas pasaras al nivel medio el numero que se genera esta en el rango del 1 al 10 """
print "*"*70
print "*"*70

x = random.randint (1, 6)

#presentacion
def juego(x): 
	intentos = 0
	while intentos < 3:
		intentos = intentos + 1
		print ("Elige un numero del 1 al 5")
		while True:
			try:
				numero = int(raw_input())
				break
			except(SyntaxError, NameError, ValueError):
				print "Solo puede ingresar un numero: "
		if numero < x:
			print ("Tu numero es mas bajo")
		if numero > x:
			print ("Tu numero es mas alto")
		if numero == x:
			break

	if numero == x:
		print ("Excelete lo lograste")
		print (" Lo lograste con %d intentos" % (intentos))

	if numero != x:
		print ("Has perdido, sera en otra oportunidad")
		print "Tu Respuesta es: ", x
		print """
		              ***NIVEL II
		              Tienes 2 vidas"""
x = random.randint (1, 10)

def juego(x): 
	intentos = 0
	while intentos < 2:
		intentos = intentos + 1
		print ("Elige un numero del 1 al 10")
		while True:
			try:
				numero = int(raw_input())
				break
			except(SyntaxError, NameError, ValueError):
				print "Solo puede ingresar un numero: "
		if numero < x:
			print ("Tu numero es mas bajo")
		if numero > x:
			print ("Tu numero es mas alto")
		if numero == x:
			break

	if numero == x:
		print ("Excelete lo lograste")
		print ("Lo lograste con %d intentos" % (intentos))

	if numero != x:
		print ("Has perdido, sera en otra oportunidad")
		print "Tu Respuesta es: ", x

juego(x)
juego(x)
