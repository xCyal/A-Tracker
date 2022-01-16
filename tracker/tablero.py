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
        _posiciones: list[pieza]
             Argumento que proporciona una lista de 64 casillas para el tablero con la pieza que contiene.
        '''
        if len(posicion_tablero) == Tablero.MAX_PIEZAS:
            self._posicion = posicion_tablero
        else:
            self._posiciones = []
            
    @property
    def posicion(self):
        """
        Property de posicion (Getter)
        """
        print("Get de _posicion")
        return self._posicion


        
        
