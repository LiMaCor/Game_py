## Clase que crea objetos Actor() con los parametros y metodos necesarios

import eventos
import habilidades

class Actor():

	## Constructor

	def __init__(self, nombre, nivel, objetos, puntosVida, puntosMana, puntosEXP, expParaSubirNivel, estadoATK, estadoDEF,
		estadoATM, estadoDEM, estadoEVA):
		self._nombre = nombre
		self._nivel = nivel
		self._objetos = objetos
		self._puntosVida = puntosVida
		self._puntosMana = puntosMana
		self._puntosEXP = puntosEXP
		self._expParaSubirNivel = expParaSubirNivel
		self._estadoATK = estadoATK
		self._estadoDEF = estadoDEF
		self._estadoATM = estadoATM
		self._estadoDEM = estadoDEM
		self._estadoEVA = estadoEVA

	## Metodos get y set

	def set_Nombre(self, nombre):
		self._nombre = nombre

	def get_Nombre(self):
		return self._nombre

	def set_Nivel(self, nivel):
		self._nivel = nivel

	def get_Nivel(self):
		return self._nivel

	def set_Objetos(self, objeto):
		self._objetos = objeto

	def get_Objetos(self):
		return self._objetos

	def set_PuntosVida(self, puntosVida):
		self._puntosVida = puntosVida

	def get_PuntosVida(self):
		return self._puntosVida

	def set_PuntosMana(self, puntosMana):
		self._puntosMana = puntosMana

	def get_PuntosMana(self):
		return self._puntosMana

	def set_PuntosEXP(self, puntosEXP):
		self._puntosEXP = puntosEXP

	def get_PuntosEXP(self):
		return self._puntosEXP

	def set_ExpParaSubirNivel(self, cantidadEXP):
		self._expParaSubirNivel = cantidadEXP

	def get_ExpParaSubirNivel(self):
		return self._expParaSubirNivel

	def set_EstadoATK(self, estadoATK):
		self._estadoATK = estadoATK

	def get_EstadoATK(self):
		return self._estadoATK

	def set_EstadoDEF(self, estadoDEF):
		self._estadoDEF = estadoDEF

	def get_EstadoDEF(self):
		return self._estadoDEF

	def set_EstadoATM(self, estadoATM):
		self._estadoATM = estadoATM

	def get_EstadoATM(self):
		return self._estadoATM

	def set_EstadoDEM(self, estadoDEM):
		self._estadoDEM = estadoDEM

	def get_EstadoDEM(self):
		return self._estadoDEM

	def set_EstadoEVA(self, estadoEVA):
		self._estadoEVA = estadoEVA

	def get_EstadoEVA(self):
		return self._estadoEVA


	## Metodos funcionales

	def coger(self, objeto):
		eventos.anyadir_objetos(self, objeto)

	def subir_Nivel(self):
		while (self._puntosEXP >= self._expParaSubirNivel):
			self.set_Nivel(self.get_Nivel() + 1)
			eventos.aumentarEstados(self)
		else:
			return "No sube de nivel"
	
	def hablar(self, texto):
		print texto

	def habilidad_Enfoque(self):
		eventos.incrementarATK_Nivel1(self)

	## Metodo de prueba. Se anyadira a otra clase posterior llamada "Pasivas"

	def habilidad_limite(self):
		if (self._puntosVida < (self._puntosVida * 20) / 100):
			self.set_EstadoATK(self.get_EstadoATK() + 50)
			self.set_EstadoDEF(self.get_EstadoDEF() + 70)
			self.set_EstadoEVA(self.get_EstadoEVA() + 40)
		else:
			print "Pero no ha funcionado...\n"


###############  Debugging  ###############

Aldia = Actor("Aldia", 1, ["Arco etereo", "Espadas fatuas"], 450, 220, 0, 100, 25, 45, 20, 32, 30)

Engel = Actor("Engel", 1, ["Espada eterea, Boken nulo"], 500, 220, 0, 100, 34, 58, 25, 30, 46)

Aldia.habilidad_Enfoque()

print("Ataque aumentado: {}\n").format(Aldia.get_EstadoATK())

Aldia.coger(["Pluma de fenix"])

print("""	--- Personajes ---

	Nombre: {}
	Nivel: {}
	Objetos: {}

	--- Estados ---

	Vida: {}
	Mana: {}
	Experiencia: {}
	Ataque: {}
	Defensa: {}
	Ataque magico: {}
	Defensa magica: {}
	Evasion: {}\n""").format(Aldia.get_Nombre(), Aldia.get_Nivel(), Aldia.get_Objetos(), Aldia.get_PuntosVida(),
	 Aldia.get_PuntosMana(), Aldia.get_PuntosEXP(), Aldia.get_EstadoATK(), Aldia.get_EstadoDEF(), Aldia.get_EstadoATM(),
	 Aldia.get_EstadoDEM(), Aldia.get_EstadoEVA())

Aldia.set_PuntosEXP(100)

Aldia.subir_Nivel()

print("""	--- Subes de nivel ---
	
	Nivel: {}
	Vida: {}
	Mana: {}
	Ataque: {}
	Defensa: {}
	Ataque magico: {}
	Defensa magica: {}
	Evasion: {}
	Experiencia: {}
	Experiencia necesaria para subir de nivel: {}\n""").format(Aldia.get_Nivel(), Aldia.get_PuntosVida(),
	 Aldia.get_PuntosMana(), Aldia.get_EstadoATK(), Aldia.get_EstadoDEF(), Aldia.get_EstadoATM(),
	 Aldia.get_EstadoDEM(), Aldia.get_EstadoEVA(), Aldia.get_PuntosEXP(), Aldia.get_ExpParaSubirNivel())

ataqueEnemigo = 370

Aldia.set_PuntosVida(Aldia.get_PuntosVida() - ataqueEnemigo)

print(Aldia.get_PuntosVida())

print(Aldia.habilidad_limite())

print("""	--- Estados limite ---

	Ataque: {}
	Defensa: {}
	Evasion: {}\n""").format(Aldia.get_EstadoATK(), Aldia.get_EstadoDEF(), Aldia.get_EstadoEVA())

Aldia.hablar("	Hola de nuevo.\n")