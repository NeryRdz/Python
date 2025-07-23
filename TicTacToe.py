from random import randint
import time

class TicTacToe():
    def __init__(self):
        self.tablero = ["", "", "", 
                        "", "", "", 
                        "", "", ""]

    def Pedir(self):
        #Pedir posicion al usuario
        posicion = int(input("Escoge una posicion (0-8): "))
        while -1 < posicion < 9:
            if  -1 < posicion < 9 and self.tablero[posicion] == "":
                self.tablero[posicion] = "X"
                break
            else:
                print("Posicion fuera de rango o ya ocupada")
                posicion = int(input("Escoge otra posicion (0-8): "))


    def turnocpu(self):
        time.sleep(1)
        print("\nCPU escogiendo...")
        while True:
            cpuposition = randint(0,8)
            if self.tablero[cpuposition] == "":
                self.tablero[cpuposition] = "O"
                break
            if "" not in self.tablero:
                break

    def mostrartablero(self):
        #Imprimir tablero
        for i in range(0,9,3):
                print(f"| {self.tablero[i]} | {self.tablero[i+1]} | {self.tablero[i+2]} |")
                if i < 6:
                    print("-------------")
    
    def verificarganador(self):
        #Verificar filas
        for i in range(0,9,3):
            if self.tablero[i] == "X" and self.tablero[i+1] == "X" and self.tablero[i+2] == "X":
                print("El jugador gana")
                return True
            elif self.tablero[i] == "O" and self.tablero[i+1] == "O" and self.tablero[i+2] == "O":
                print("La computadora gana")
                return True
            
        #Verificar columnas
        for i in range(0,3):
            if self.tablero[i] == "X" and self.tablero[i+3] == "X" and self.tablero[i+6] == "X":
                print("El jugador gana")
                return True
            elif self.tablero[i] == "O" and self.tablero[i+3] == "O" and self.tablero[i+6] == "O":
                print("La computadora gana")
                return True
            
        #Verificar diagonales
        if self.tablero[0] == "X" and self.tablero[4] == "X" and self.tablero[8] == "X":
            print("El jugador gana")
            return True
        elif self.tablero[0] == "O" and self.tablero[4] == "O" and self.tablero[8] == "O":
            print("La computadora gana")
            return True

        if self.tablero[2] == "X" and self.tablero[4] == "X" and self.tablero[6] == "X":
            print("El jugador gana")
            return True
        elif self.tablero[2] == "O" and self.tablero[4] == "O" and self.tablero[6] == "O":
            print("La computadora gana")
            return True

        #Empate
        if "" not in self.tablero:
            print("Empate")
            return True

        return False
    
Tic = TicTacToe()

while True:
    Tic.Pedir()
    Tic.mostrartablero()
    if Tic.verificarganador():
       break

    Tic.turnocpu()
    Tic.mostrartablero()
    if Tic.verificarganador():
        break
