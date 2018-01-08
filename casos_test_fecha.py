from fecha import *
if __name__ == "__main__":
	dia = input("Dime qué día es: ")
	mes = input("¿De qué mes?: ")
	año = input("¿Y de qué año?: ")
	calendario = Calendario(dia, mes, año)
	incremento = int(input("¿Cuántos días quieres aumentar?: "))
	calendario.incrementarFecha(incremento)
	calendario.imprimirFecha()
	print(calendario.mesLetra())
	calendario.getFecha()