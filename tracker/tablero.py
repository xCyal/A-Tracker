from pieza import *

class Tablero:
    '''
    Clase tablero, encargada de almacenar una posicion unica de las piezas en un tablero de ajedrez
    
    Atributos
    ---------
    _posiciones : list[pieza]
        Variable que almacena hasta MAX_PIEZAS piezas que representan el tablero en una situación concreta
    MAX_PIEZAS : int
    	Variable de clase que indica el maximo de piezas que puede almacenar un tablero.
    '''
    MAX_PIEZAS = 64;
    
    def __init__(self, posicion_tablero):
        
        '''
        Constructor de la clase tablero, inicializa el tablero solo si hay 64 casillas, en caso contrario lo 
        deja vacío.
        
        Atributos
        ---------
        posicion_tablero: list[pieza]
             Argumento que proporciona una lista de 64 casillas para el tablero con la pieza que contiene.
        '''
        if  len(posicion_tablero) != Tablero.MAX_PIEZAS:
            raise ValueError("El tamaño del tablero debe ser exactamente 64 casillas")
        
        for i in posicion_tablero:
            if not isinstance(i,pieza):
                raise ValueError("Los valores introducidos deben ser del tipo pieza")
        
        self._posiciones = posicion_tablero
        
    @property
    def posiciones(self):
        '''
        Getter del atributo _posiciones de la clase tablero
        
        Devuelve _posiciones
        '''
        print("Getter de _posiciones en tablero.py")
        return self._posiciones       
            


    def puntuacion_tablero(self):
        '''
        Metodo que devuelve la puntuacion, a nivel de material, del tablero.
        
        En caso de empate material puntuacion = 0, en caso de mayoria blanca puntuacion positiva, en caso de victoria negra puntuacion
        negativa.
        
        La puntuacion de las piezas:
        Peon = +-1
        Alfil / Caballo = +-3
        Torre = +-5
        Reina = +-9 
        '''
        puntuacion = 0
        
        for i in self_posiciones:
            if i.value == Pieza.PEON_BLANCO.value:
                puntuacion +=1
            elif i.value == Pieza.PEON_NEGRO.value:
                puntuacion -=1
            elif i.value == Pieza.ALFIL_BLANCO.value:
                puntuacion +=3
            elif i.value == Pieza.ALFIL_NEGRO.value:
                puntuacion -=3
            elif i.value == Pieza.CABALLO_BLANCO.value:
                puntuacion +=3
            elif i.value == Pieza.CABALLO_NEGRO.value:
                puntuacion -=3
            elif i.value == Pieza.TORRE_BLANCO.value:
                puntuacion +=5
            elif i.value == Pieza.TORRE_NEGRO.value:
                puntuacion -=5
            elif i.value == Pieza.REINA_BLANCO.value:
                puntuacion +=9
            elif i.value == Pieza.REINA_NEGRO.value:
                puntuacion -=9
        
        return puntuacion    
        
