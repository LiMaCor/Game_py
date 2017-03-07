## Funciones que haran interactuar a los personajes con el entorno


	## Metodos funcionales

def aumentarEstados(self):

	nivel = self.get_Nivel()
	puntosVida = self.get_PuntosVida()
	puntosMana = self.get_PuntosMana()
	estadoATK = self.get_EstadoATK()
	estadoDEF = self.get_EstadoDEF()
	estadoATM = self.get_EstadoATM()
	estadoDEM = self.get_EstadoDEM()
	estadoEVA = self.get_EstadoEVA()
	expParaSubirNivel = (self.get_Nivel() * 67) + self.get_ExpParaSubirNivel()
			
	self.set_PuntosVida(self.get_PuntosVida() + (nivel * (puntosVida / 100)))
	self.set_PuntosMana(self.get_PuntosMana() + (nivel * (puntosMana / 100)))
	self.set_EstadoATK(self.get_EstadoATK() + (nivel * (estadoATK / 10)))
	self.set_EstadoDEF(self.get_EstadoDEF() + (nivel * (estadoDEF / 10)))
	self.set_EstadoATM(self.get_EstadoATM() + (nivel * (estadoATM / 10)))
	self.set_EstadoDEM(self.get_EstadoDEM() + (nivel * (estadoDEM / 10)))
	self.set_EstadoEVA(self.get_EstadoEVA() + (nivel * (estadoEVA / 10)))
	self.set_ExpParaSubirNivel(expParaSubirNivel)


def anyadir_objetos(self, objeto):
	self._objetos = self._objetos + objeto

def incrementarATK_Nivel1(self):
	self._estadoATK = self._estadoATK + ((self._estadoATK * 50) / 100)