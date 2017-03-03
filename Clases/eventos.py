## Funciones que haran interactuar a los personajes con el entorno


	## Metodos funcionales

def aumentarEstados(self):

	nivel = self.get_Nivel()
	puntosVida = self.get_PuntosVida()
	puntosMana = self.get_PuntosMana()
	estadoATK = self.get_EstadoATK()
	estadoDEF = self.get_EstadoDEF()
	estadoEVA = self.get_EstadoEVA()
	expParaSubirNivel = (self.get_Nivel() * 75) + self.get_ExpParaSubirNivel()
			
	self.set_PuntosVida(self.get_PuntosVida() + (nivel * (puntosVida / 100)))
	self.set_PuntosMana(self.get_PuntosMana() + (nivel * (puntosMana / 100)))
	self.set_EstadoATK(self.get_EstadoATK() + (nivel * (estadoATK / 10)))
	self.set_EstadoDEF(self.get_EstadoDEF() + (nivel * (estadoDEF / 10)))
	self.set_EstadoEVA(self.get_EstadoEVA() + (nivel * (estadoEVA / 10)))
	self.set_ExpParaSubirNivel(expParaSubirNivel)
