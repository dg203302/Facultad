import random
import time

# Colores disponibles
COLORES = ["rojo", "verde", "azul", "amarillo"]

def generar_secuencia(longitud):
    """Genera una secuencia aleatoria de colores."""
    return [random.choice(COLORES) for _ in range(longitud)]

def mostrar_secuencia(secuencia):
    """Muestra la secuencia al jugador."""
    for color in secuencia:
        print(f"Simon dice: {color}")
        time.sleep(1)  # Espera 1 segundo entre cada color

def obtener_respuesta():
    """Obtiene la respuesta del jugador."""
    return input("Tu turno (ingresa los colores separados por comas): ").lower().split(", ")

def verificar_respuesta(secuencia, respuesta):
    """Verifica si la respuesta del jugador coincide con la secuencia."""
    return secuencia == respuesta

def jugar():
    print("¡Bienvenido a Simon Dice!")
    nivel = 1

    while True:
        print(f"\nNivel {nivel}")
        secuencia = generar_secuencia(nivel)
        mostrar_secuencia(secuencia)
        respuesta = obtener_respuesta()

        if verificar_respuesta(secuencia, respuesta):
            print("¡Correcto! Siguiente nivel.")
            nivel += 1
        else:
            print(f"¡Incorrecto! Tu puntaje final es {nivel}.")
            break

if __name__ == "__main__":
    jugar()

#codigos del principal
#en orden
#__actb1:bool
#__actb2:bool
#__actb3:bool
#__actb4:bool
    #inicializacion rancia
    '''
    self.__actb1=False
    self.__actb2=False
    self.__actb3=False
    self.__actb4=False
    '''
    #regiistro rancio
    '''
    def registrarb1(self):
        self.__actb1=True
    def registrarb2(self):
        self.__actb2=True
    def registrarb3(self):
        self.__actb3=True
    def registrarb4(self):
        self.actb4=True
    '''

    #codigo del juego mal hecho
    '''
    def generarsecuencia(self,nivel):
        botones=[1,2,3,4]
        return [random.choice(botones) for _ in range(nivel)]
    def cambiarcolorb1(self):
        self.__boton1.config(bg='gray')
    def cambiarcolorb2(self):
        self.__boton2.config(bg='gray')
    def cambiarcolorb3(self):
        self.__boton3.config(bg='gray')
    def cambiarcolorb4(self):
        self.__boton4.config(bg='gray')
    def reiniciarcolores(self):
        self.__boton1.config(bg='teal')
        self.__boton2.config(bg='red')
        self.__boton3.config(bg='yellow')
        self.__boton4.config(bg='blue')
    def iluminarbotones(self,secuencia):
        for boton in secuencia:
            if boton==1:
                self.cambiarcolorb1()
            elif boton==2:
                self.cambiarcolorb2()
            elif boton==3:
                self.cambiarcolorb3()
            elif boton==4:
                self.cambiarcolorb4()
    def verificar(self,toque,secuencia):
        for boton in secuencia:
            if toque==boton:
                return True
    def reiniciarvalores(self):
        self.__actb1=False
        self.__actb2=False
        self.__actb3=False
        self.__actb4=False
    def reiniciarcontador(self):
        self.__contador=0
    def registrartoque(self):
        if self.__actb1==True:
            return 1
        elif self.__actb2==True:
            return 2
        elif self.__actb3==True:
            return 3
        elif self.__actb4==True:
            return 4
        else:
            return False
        '''
    #funcion del juego mal hecha
    '''
    def iniciar(self):
        nivel=1
        while True:
            secuencia=self.generarsecuencia(nivel)
            self.iluminarbotones(secuencia)
            time.sleep(1)
            self.reiniciarcolores()
            toque=self.registrartoque()
            if self.verificar(toque,secuencia):
                self.aumentar()
                self.reiniciarvalores()
                nivel+=1
            else:
                messagebox.showinfo(title='GAME OVER', message=f'el puntaje final es: {self.__contador}')
                self.reiniciarvalores()
                self.reiniciarcontador()
                nivel=1
                break
    '''