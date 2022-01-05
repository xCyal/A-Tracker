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
        self._posicion = posicion_tablero

    def get_posicion(self):
        return self._posicion
