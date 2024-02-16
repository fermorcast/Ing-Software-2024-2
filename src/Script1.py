import random

class JuegoTenis:
    def __init__(self, jugador1, jugador2):
        self.jugadores = [jugador1, jugador2]

        self.set1 = 0
        self.set2 = 0
        self.juego1 = 0
        self.juego2 = 0
        self.puntos1 =  0
        self.puntos2 =  0
        self.servidor_actual = 0
        self.cambio_lados = False
        self.jugador_saca = random.choices([1,2])
        if self.jugador_saca == 1:
            print(f"Le toca sacar al {jugador1}")
        else:
            print(f"Le toca sacar al {jugador2}")


    def punto_ganado(self, jugador):
        if jugador == 1:
            if self.puntos1 == 3 and self.puntos2 == 3:
                self.puntos1 = 4
            elif self.puntos1 == 4 and self.puntos2 == 4:
                self.puntos2 = 3
            elif self.puntos1 == 3 and self.puntos2 == 4:
                self.puntos2 = 3 
            else: 
                self.puntos1 = self.puntos1+1 
            if self.puntos1 == 5:
                self.puntos1 = 0
                self.puntos2 = 0
                self.juego1 = self.juego1+1
                self.cambio_lados = True
                if self.jugador_saca == 1:
                    self.jugador_saca = 2
                    print(f"Le toca sacar al {self.jugadores[1]}")
                else:
                    self.jugador_saca = 1
                    print(f"Le toca sacar al {self.jugadores[0]}")
            if self.juego1 - self.juego2 >= 2 and self.juego1 >= 6:
                self.set1 = self.set1+1
                self.juego1 = 0
                self.juego2 = 0
            if self.set1 > 2:
                return True
                print("Juego terminado")
        else:     
            if self.puntos1 == 3 and self.puntos2 == 3:
                self.puntos2 = 4
            elif self.puntos1 == 4 and self.puntos2 == 4:
                self.puntos1 = 3
            elif self.puntos2 == 3 and self.puntos1 == 4:
                self.puntos1 = 3
            else: 
                self.puntos2 = self.puntos2+1
            if self.puntos2 == 5:
                self.puntos2 = 0
                self.puntos1 = 0
                self.juego2 = self.juego2+1
                self.cambio_lados = True
                if self.jugador_saca == 1:
                    self.jugador_saca = 2
                    print(f"Le toca sacar al {self.jugadores[1]}")
                else:
                    self.jugador_saca = 1
                    print(f"Le toca sacar al {self.jugadores[0]}")
            if self.juego2 - self.juego1 >= 2 and self.juego2 >= 6:
                self.set2 = self.set2+1
                self.juego2 = 0
                self.juego1 = 0
            if self.set2 > 2:
                return True
            
        if (self.juego1 + self.juego2) % 2 == 1 and self.cambio_lados:
            self.cambio_lados = False
            print("Hemos cambiado de cancha")
        return False

    
    def imprimir_marcador(self):
        print(f"Marcador actual: {self.jugadores[0]} {self.set1} sets, {self.juego1} juegos, "
              f"{self.puntos1} puntos - {self.jugadores[1]} {self.set2} sets, "
              f"{self.juego2} juegos, {self.puntos2} puntos")

try:

    nombre_jugador1 = input("Ingrese el nombre del primer jugador: ")

    nombre_jugador2 = input("Ingrese el nombre del segundo jugador: ")
    partida = JuegoTenis(nombre_jugador1, nombre_jugador2)

    print(f"Comienza el partido entre {nombre_jugador1} y {nombre_jugador2}.")
except EOFError: 
    print("Error")
while True:
    #jugador_ganador = random.choice([1,2])
    while True:
        try:
            jugador_ganador = int(input("El ganador del punto es: \n Opciones: \n  1 ó 2:  "))
            break
        except ValueError:
            print("Ingresa correctamente al ganador: ")

    if partida.punto_ganado(jugador_ganador):
        break
    partida.imprimir_marcador()

print(f"¡El partido ha terminado! El resultado final es: ")
partida.imprimir_marcador()
