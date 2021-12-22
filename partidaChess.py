class PartidaChess:

    def __init__(self, nombres, jugador_inicial,ganador,movimientos):
        self.nombre_jugadores = nombres
        self.jugador_inicial = jugador_inicial
        self.ganador = ganador
        self.movimientos_partida = movimientos

    def get_nombre_jugadores(self):
        return self.nombre_jugadores

    def get_jugador_inicial(self):
        return self.jugador_inicial

    def get_ganador(self):
        return self.ganador

    def get_movimientos_partida(self):
        return self.movimientos_partida
