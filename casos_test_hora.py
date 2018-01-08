from hora import *
if __name__ == "__main__":
	hora = input("Dime qué hora es: ")
	minutos = input("¿Cuántos minutos?: ")
	segundos = input("¿Y segundos?: ")
	reloj = Propiedades(hora, minutos, segundos)
	reloj.getHora()
