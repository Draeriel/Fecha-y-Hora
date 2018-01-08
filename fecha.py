class Fecha:

	def __init__(self, dia, mes, año):
		self.dia = dia
		self.mes = mes
		self.año = año

	def __repr__(self):
		return "%s, %s, %s" % (self.dia, self.mes, self.año)


class Interfaz():

	def getFecha():
		pass


class Propiedades(Fecha, Interfaz):

	def __init__(self, dia, mes, año):
		Fecha.__init__(self, dia, mes, año)	

	def setDia(self):
		try:
			treinta = ["4", "6", "9", "11"]
			treintaiuno = ["1", "3", "5", "7", "8", "10", "12"]
			self.dia = int(self.dia)
			if self.mes in treinta:
				assert isinstance(self.dia, int)
				assert (1 <= self.dia <= 30)
			elif self.mes in treintaiuno:	
				assert isinstance(self.dia, int)
				assert (1 <= self.dia <= 31)
			elif self.mes == 2:
				if self.año % 4 == 0:
					assert isinstance(self.dia, int)
					assert (1 <= self.dia <= 29)
				else:
					assert isinstance(self.dia, int)
					assert (1 <= self.dia <= 28)
			else:
				assert isinstance(self.dia, int)
				assert (1 <= self.dia <= 31)

		except (AssertionError, ValueError):
			self.dia = 1

	def setMes(self):
		try:
			self.mes = int(self.mes)
			assert isinstance(self.dia, int)
			assert (1 <= self.mes <= 12)
		except (AssertionError, ValueError):
			self.mes = 1			

	def setAño(self):
		try:
			self.año = int(self.año)
			assert isinstance(self.año, int)
			assert (1900 <= self.año <= 3000)
		except (AssertionError, ValueError):
			self.año = 1900

class Calendario(Propiedades):

	def __init__(self, dia, mes, año):
		Fecha.__init__(self, dia, mes, año)

	def incrementarFecha(self, valor):
		treinta = ["4", "6", "9", "11"]
		treintaiuno = ["1", "3", "5", "7", "8", "10", "12"]
		self.getFecha()
		self.dia += valor
		while (self.dia > 31 and self.mes in trentaiuno) or (self.dia > 30 and self.mes in trentaiuno) or (self.mes == 2 and ((self.año % 4 == 0) and self.dia > 29)) or (self.mes == 2 and ((self.año % 4 != 0) and self.dia > 28)):
			self.dia -= 31
			self.mes += 1
		while self.mes > 12:
			self.mes -= 12
			self.año += 1
		if self.año > 3000:
			print("¡Te has pasado!")
		self.imprimirFecha()
		
	def getFecha(self):
		self.setDia()
		self.setMes()
		self.setAño()
		return self

	def imprimirFecha(self):
		monat = self.mesLetra()
		print(f"{self.dia} de {monat} del {self.año}.")

	def mesLetra(self):
		meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}	
		self.getFecha()
		return meses[self.mes]



			




				
