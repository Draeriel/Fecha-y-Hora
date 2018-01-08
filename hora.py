class Hora:

	def __init__(self, hora, minutos, segundos):
		self.hora = hora
		self.minutos = minutos
		self.segundos = segundos

	def __repr__(self):
		return "%s, %s, %s" % (self.hora, self.minutos, self.segundos)


class Interfaz():

	def getHora():
		pass


class Propiedades(Hora, Interfaz):

	def __init__(self, hora, minutos, segundos):
		Hora.__init__(self, hora, minutos, segundos)

	def setHora(self):
		try: 
			self.hora = int(self.hora)
			assert isinstance(self.hora, int)
			assert (0 <= self.hora <= 23)
		except (AssertionError, ValueError):
			self.hora = 0	

		try:
			self.minutos = int(self.minutos)
			assert isinstance(self.minutos, int)
			assert (0 <= self.minutos <= 59)
		except (AssertionError, ValueError):
			self.minutos = 0

		try:
			self.segundos = int(self.segundos)
			assert isinstance(self.segundos, int)
			assert (0 <= self.segundos <= 59)
		except (AssertionError, ValueError):
			self.segundos = 0	
	
	def imprimirHora(self):
		print(f"{self.hora}:{self.minutos}:{self.segundos}")
	
	def getHora(self):
		self.setHora()
		self.imprimirHora()

				


