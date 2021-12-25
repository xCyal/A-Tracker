class PartidaChess:

    def __init__(self, nombres, jugador_inicial,ganador,movimientos):
        self._nombre_jugadores = nombres
        self._jugador_inicial = jugador_inicial
        self._ganador = ganador
        self._movimientos_partida = movimientos

    def get_nombre_jugadores(self):
        return self._nombre_jugadores

    def get_jugador_inicial(self):
        return self._jugador_inicial

    def get_ganador(self):
        return self._ganador

    def get_movimientos_partida(self):
        return self._movimientos_partida
