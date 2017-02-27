## Funciones que haran interactuar a los personajes con el entorno

	## Metodos funcionales

def aumentarEstados():
	nivel = Actor().get_Nivel()
	puntosVida = Actor().get_PuntosVida()
	puntosMana = Actor().get_PuntosMana()
	estadoATK = Actor().get_EstadoATK()
	estadoDEF = Actor().get_EstadoDEF()
	estadoEVA = Actor().get_EstadoEVA()
	expParaSubirNivel = (Actor().get_Nivel() * 100) + (Actor().get_PuntosVida() % Actor().get_Nivel())
			
	Actor().set_PuntosVida(Actor().get_PuntosVida() + (nivel * (puntosVida / 100)))
	Actor().set_PuntosMana(Actor().get_PuntosMana() + (nivel * (puntosMana / 100)))
	Actor().set_EstadoATK(Actor().get_EstadoATK() + (nivel * (estadoATK / 100)))
	Actor().set_EstadoDEF(Actor().get_EstadoDEF() + (nivel * (estadoDEF / 100)))
	Actor().set_EstadoEVA(Actor().get_EstadoEVA() + (nivel * (estadoEVA / 100)))
	Actor().set_ExpParaSubirNivel(expParaSubirNivel)
