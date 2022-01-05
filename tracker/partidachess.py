from tablero import *

class PartidaChess:
   
   '''
   Clase encargada de almacenar los datos de una partida de ajedrez
        
   Atributos
   ---------
        
    _nombres_blancas : str
    	Nombre de usuario de jugador en blancas
    _nombre_negras : str
    	Nombre de usuario de jugador en negras
    _ganador : str
        Nombre del ganador de la partida
    _movimientos_partida : list[tablero]
    	Lista de tableros (movimientos) de los jugadores durante la partida
   '''

    def __init__(self, nombre_blancas,nombre_negras,ganador,movimientos):
        
        '''
    	Construye un objeto de tipo PartidaChess
    	
    	Atributos
    	---------
    	nombres_blancas : str
    		Nombre de usuario de jugador en blancas
    	nombre_negras : str
    		Nombre de usuario de jugador en negras
    	ganador : str
    		Nombre del ganador de la partida
    	movimientos : list[tablero]
    		Lista de tableros (movimientos) de los jugadores durante la partida
        '''
        
        self._nombre_blancas = nombre_blancas
        self._nombre_negras = nombre_negras
        self._ganador = ganador
        self._movimientos_partida = movimientos

    def get_nombre_blancas(self):
        return self._nombre_blancas
    
    def get_nombre_negras(self):
        return self._nombre_negras
    
    def get_jugador_inicial(self):
        return self._jugador_inicial

    def get_ganador(self):
        return self._ganador

    def get_movimientos_partida(self):
        return self._movimientos_partida
