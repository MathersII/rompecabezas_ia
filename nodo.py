class Nodo:
	def __init__(self,cadena, padre = None): #por defecto none, el primer nodo no tiene padre
		self.cadena = cadena
		self.padre = padre

	def conseguir_cadena(self):
		return self.cadena

	def conseguir_padre(self):
		return self.padre
		