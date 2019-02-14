import nodo
import sys

class Main:
	def __init__(self, estado_inicial, estado_final):
		self.estado_final = estado_final
		self.estado_inicial = cadenaNodo(estado_inicial)
		self.conseguirRuta()

	def conseguir_ruta(self):
		estado_actual = self.estado_inicial
		visitados = []

		while ( es_solucion(estado_actual.conseguir_cadena()) == False):
			visitados.append(estado_actual.conseguir_cadena())
			hijos = crearHijos(estado_actual)
			for x in hijos:
				if x.conseguir_cadena() not in visitados:
					cola.push(x)

			estado_actual = cola.pop()

		print(visitados)

	def es_solucion(self, estado):
		if (estado == estado_final):
			return True
		else:
			return False


	def crear_hijos(self):

if __name__ == '__main__':
	
	main = Main()

