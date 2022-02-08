from tipo_pieza import *

class Pieza:
    '''
    Clase Pieza, encargada de almacenar el las piezas del tablero.
    
    Atributos
    ---------
    _tipo : TipoPieza
        Variable del tipo enum TipoPieza que indica de que tipo de pieza se trata.
    _blanco : bool
    	Variable que determina el color de la pieza, blanco = True , negro = False
    '''
    
    def __init__(self,tipo,blanco):
        '''
        Constructor de la clase Pieza, inicializa las piezas a su tipo y color. Los parametros deben ser TipoPieza para tipo y bool para blanco
        
        Parámetros
        ---------
        tipo : TipoPieza
            Parametro del tipo TipoPieza que determina que tipo de pieza es
        blanco : bool
            Parametro del tipo bool que determina si una pieza es blanca o no
        '''
        if not isinstance(tipo,TipoPieza):
            raise ValueError("El tipo de la pieza debe ser enum TipoPieza")
        self._tipo = tipo
        
        if not isinstance(blanco,bool):
            raise ValueError("El tipo de blanco debe ser bool")
        self._blanco = blanco
        
    @property
    def tipo(self):
        '''
        Getter del atributo _tipo de la clase Pieza
        
        Devuelve _tipo
        '''
        print("Getter de _tipo en pieza.py")
        return self._tipo
        
    @property
    def blanco(self):
        '''
        Getter del atributo _blanco
        
        Devuelve _blanco
        '''
        print("Getter de _blanco en pieza.py")
        return self._blanco                 
