## Clase que crea objetos Actor() con los parametros y metodos necesarios

class Actor():

	## Variables

	nombre = ""
	nivel = 1
	objetos = []
	puntosVida = 0
	puntosMana = 0
	puntosEXP = 0
	expParaSubirNivel = 100
	estadoATK = 0
	estadoDEF = 0
	estadoEVA = 0


	## Metodos get y set

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

	def set_PuntosEXP(self, puntosEXP):
		self.puntosEXP = puntosEXP

	def get_PuntosEXP(self):
		return self.puntosEXP

	def set_ExpParaSubirNivel(self):
		self.expParaSubirNivel = (self.get_Nivel() * 100) + (self.get_PuntosVida() % self.get_Nivel())

	def get_ExpParaSubirNivel(self):
		return self.expParaSubirNivel

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


	## Metodos funcionales

	def anyadir_objetos(self, objeto = []):
		self.objetos = self.objetos + objeto

	def subir_Nivel(self):
		if (self.puntosEXP >= self.expParaSubirNivel):
			self.set_Nivel(self.get_Nivel() + 1);
			self.set_ExpParaSubirNivel() ## Falta por anyadir un evento externo "aumentarEstados"


## Este metodo se anyadira a otra clase posterior llamada "Habilidades"

	def habilidad_incrementarATK(self):
		self.estadoATK = self.estadoATK + ((self.estadoATK * 50) / 100)


## Metodo de prueba. Se anyadira a otra clase posterior llamada "Pasivas"

	def habilidad_limite(self):
		if (self.puntosVida < (self.puntosVida * 20) / 100):
			self.set_EstadoATK(self.get_EstadoATK() + 50)
			self.set_EstadoDEF(self.get_estadoDEF() + 70)
			self.set_EstadoEVA(self.get_EstadoEVA() + 40)
		else:
			return "\nPero no ha funcionado...\n"


###############  Debugging  ###############

Aldia = Actor()

Aldia.set_Nombre("Aldia")
Aldia.set_Nivel(1)
Aldia.set_Objetos(["Arco etereo", "Espadas fatuas"])
Aldia.set_PuntosVida(450)
Aldia.set_PuntosMana(220)
Aldia.set_EstadoATK(20)
Aldia.set_EstadoDEF(45)
Aldia.set_EstadoEVA(30)

Aldia.habilidad_incrementarATK()

print("Ataque aumentado: {}\n").format(Aldia.get_EstadoATK())

Aldia.anyadir_objetos(["Lagrima de cristal"])

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
	Evasion: {}\n""").format(Aldia.get_Nombre(), Aldia.get_Nivel(), Aldia.get_Objetos(), Aldia.get_PuntosVida(),
	 Aldia.get_PuntosMana(), Aldia.get_PuntosEXP(), Aldia.get_EstadoATK(), Aldia.get_EstadoDEF(), Aldia.get_EstadoEVA())

Aldia.set_PuntosEXP(100)

Aldia.subir_Nivel()
print("""	--- Subes de nivel ---
	
	Nivel: {}
	Experiencia: {}
	Experiencia necesaria para subir de nivel: {}\n""").format(Aldia.get_Nivel(), Aldia.get_PuntosEXP(), Aldia.expParaSubirNivel)