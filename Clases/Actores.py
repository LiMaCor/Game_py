# Clase que crea objetos Actor() con los parametros y metodos necesarios

class Actor():

	# Variables

	nombre = ""
	nivel = 1
	objetos = []
	puntosVida = 0
	puntosMana = 0
	estadoATK = 0
	estadoDEF = 0
	estadoEVA = 0


	# Metodos get y set

	def set_Nombre(self, nombre):
		self.nombre = nombre

	def get_Nombre(self):
		return self.nombre

	def set_Nivel(self, nivel):
		self.nivel = nivel

	def get_Nivel(self):
		return self.nivel

	def set_Objetos(self, objeto):
		self.objetos = objeto

	def get_Objetos(self):
		return self.objetos

	def set_PuntosVida(self, puntosVida):
		self.puntosVida = puntosVida

	def get_PuntosVida(self):
		return self.puntosVida

	def set_PuntosMana(self, puntosMana):
		self.puntosMana = puntosMana

	def get_PuntosMana(self):
		return self.puntosMana

	def set_EstadoATK(self, estadoATK):
		self.estadoATK = estadoATK

	def get_EstadoATK(self):
		return self.estadoATK

	def set_EstadoDEF(self, estadoDEF):
		self.estadoDEF = estadoDEF

	def get_EstadoDEF(self):
		return self.estadoDEF

	def set_EstadoEVA(self, estadoEVA):
		self.estadoEVA = estadoEVA

	def get_EstadoEVA(self):
		return self.estadoEVA

	# Metodos funcionales

# Este metodo se anyadira a otra clase posterior llamada "Habilidades"

	def habilidad_incrementarATK(self):
		self.estadoATK = self.estadoATK + ((self.estadoATK * 50) / 100)

# Metodo de prueba. Se anyadira a otra clase posterior llamada "Pasivas"

	def habilidad_limite(self):
		if (self.puntosVida < ((self.puntosVida * 20) / 100)):
			self.estadoATK = self.estadoATK + 50
			self.estadoDEF = self.estadoDEF + 70
			self.estadoEVA = self.estadoEVA + 40
		else:
			return "\nPero no ha funcionado...\n"

# Debugging

Aldia = Actor()

Aldia.set_Nombre("Aldia")
Aldia.set_Nivel(1)
Aldia.set_Objetos(["Arco etereo", "Espadas fatuas"])
Aldia.set_PuntosVida(450)
Aldia.set_PuntosMana(220)
Aldia.set_EstadoATK(20)
Aldia.set_EstadoDEF(45)
Aldia.set_EstadoEVA(30)

print("""	--- Personajes ---

	Nombre: {}
	Nivel: {}
	Objetos: {}

	--- Estados ---

	Vida: {}
	Mana: {}
	Ataque: {}
	Defensa: {}
	Evasion: {}\n""").format(Aldia.get_Nombre(), Aldia.get_Nivel(), Aldia.get_Objetos(), Aldia.get_PuntosVida(),
	 Aldia.get_PuntosMana(), Aldia.get_EstadoATK(), Aldia.get_EstadoDEF(), Aldia.get_EstadoEVA())

Aldia.habilidad_incrementarATK()

print("Ataque aumentado: {}").format(Aldia.get_EstadoATK())

print(Aldia.habilidad_limite())