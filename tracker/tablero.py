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
        
        
            


        
        
