class Nodo:
	def __init__(self,cadena, padre = None): #por defecto none, el primer nodo no tiene padre
		self.cadena = cadena
		self.padre = padre
		self.ruta_al_nodo = [] #el nodo guarda la ruta para llegar a si mismo.

	def conseguir_cadena(self):
		return self.cadena

	def conseguir_padre(self):
		return self.padre

	def conseguir_ruta_al_nodo(self):
		return self.ruta_al_nodo

	def establecer_ruta_al_nodo(self, ruta_al_nodo, nodo):
		self.ruta_al_nodo = ruta_al_nodo + [nodo]
		