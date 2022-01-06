from pieza import *

class Tablero:
    '''
    Clase tablero, encargada de almacenar una posicion unica de las piezas en un tablero de ajedrez
    
    Atributos
    ---------
    _posicion : list[pieza]
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
        posicion_tablero : list[pieza]
             Argumento que proporciona una lista de 64 casillas para el tablero con la pieza que contiene.

        '''
        if len(posicion_tablero) == Tablero.MAX_PIEZAS:
            self._posicion = posicion_tablero
        else:
            self._posicion = []
        

    def get_posicion(self):
        return self._posicion
        
    def puntuar_tablero(self):
        
        '''
        Metodo que devuelve la puntuación del tablero, siendo negativa en favor de negras y positiva en favor de blancas
        '''
        puntuacion = 0
        
        for i in self._posicion:
            if i.value == Pieza.PEON_BLANCO.value:
                print("Peon blanco")
                puntuacion += 1
            elif i.value == Pieza.PEON_NEGRO.value:
                print("Peon negro")
                puntuacion -= 1
            elif i.value == Pieza.ALFIL_BLANCO.value:
                print("Alfil")
                puntuacion += 3
            elif i.value == Pieza.ALFIL_NEGRO.value:
                print("Alfil")
                puntuacion -= 3
            elif i.value == Pieza.CABALLO_BLANCO.value:
                print("Caballo blanco")
                puntuacion += 3
            elif i.value == Pieza.CABALLO_NEGRO.value:
                print("Caballo negro")
                puntuacion -= 3
            elif i.value == Pieza.TORRE_BLANCO.value:
                print("Torre blanca")
                puntuacion += 5
            elif i.value == Pieza.TORRE_NEGRO.value:
                print("Torre negra")
                puntuacion -= 5
            elif i.value == Pieza.REINA_BLANCO.value:
                print("Reina blanca")
                puntuacion += 9
            elif i.value == Pieza.REINA_NEGRO.value:
                print("Reina negra")
                puntuacion -= 9
        return puntuacion
