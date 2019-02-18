from nodo import Nodo
from estructuras import Cola
import sys

class Main:
	def __init__(self, estado_inicial, estado_final):
		self.estado_final = estado_final
		self.estado_inicial = Nodo(estado_inicial)
		r = self.conseguir_ruta()
		self.imprimir_ruta(r)


	def conseguir_ruta(self):
		cola = Cola()
		estado_actual = self.estado_inicial
		visitados = []
		hijos = self.crear_hijos(estado_actual)
		while (self.es_solucion(estado_actual.conseguir_cadena()) == False):
			#self.imprimir_como_matriz(estado_actual.conseguir_cadena())
			visitados.append(estado_actual.conseguir_cadena())
			hijos = self.crear_hijos(estado_actual)
			for x in hijos: 
				if x.conseguir_cadena() not in visitados:
					cola.push(x)
			estado_actual = cola.pop()
		visitados.append(estado_actual.conseguir_cadena()) #añado el último nodo al salir del while
		return estado_actual

	def es_solucion(self, estado):
		if (estado == self.estado_final):
			return True
		else:
			return False


	def crear_hijos(self, nodo):
		cadena = nodo.conseguir_cadena()
		pos_vacia = cadena.find("0")
		positions = self.crear_posiciones(pos_vacia)
		return list(#convierto mapa a lista
			filter( #filtro aquellos que sean -1 --> ver funcion nueva_cadena, retorna -1
				lambda x: type(x) == Nodo,list(
					map(lambda x: self.nueva_cadena(nodo,pos_vacia,x),positions) #creo las nuevas cadenas
					)
				)
			)


	def crear_posiciones(self,pos_vacia):
		mod = (pos_vacia + 1) % 3 #me dice  si es una posicion en el extremo derecho o izquierdo
		if(mod == 0):
			return [pos_vacia - 3,
					pos_vacia - 1,
					pos_vacia + 3]
		elif (mod == 1):
			return [pos_vacia - 3,
					pos_vacia + 1,
					pos_vacia + 3]
		else:
			return [pos_vacia - 3,
					pos_vacia - 1,
					pos_vacia + 1,
					pos_vacia + 3]

	def nueva_cadena(self,nodo,posicion_cero,nueva_posicion):
		cadena = nodo.conseguir_cadena()
		if nueva_posicion >= 0 and nueva_posicion < 9: #evito tener error por un fuera de rango en el array
			nueva_cadena = cadena[:posicion_cero] + cadena[nueva_posicion] + cadena[posicion_cero + 1:]
			nueva_cadena = nueva_cadena[:nueva_posicion] + "0" + nueva_cadena[nueva_posicion + 1:]
			return Nodo(nueva_cadena.strip(),nodo)
		else:
			return -1 #los fuera de rango retornan esta bandera

	def imprimir_ruta(self,nodo_final): #imprime ruta de final a inicio, corregir esto
		nodo_actual = nodo_final
		while(nodo_actual != None):
			self.imprimir_como_matriz(nodo_actual.conseguir_cadena())
			nodo_actual = nodo_actual.conseguir_padre()

	def imprimir_como_matriz(self,cadena):
		print(cadena[:3] + "\n" + cadena[3:6] + "\n" + cadena[6:] + "\n\n")


if __name__ == '__main__':	
	main = Main(sys.argv[1],sys.argv[2])

