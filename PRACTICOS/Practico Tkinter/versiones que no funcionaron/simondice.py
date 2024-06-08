import tkinter as tk
import random

class SimonDice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('400x300')

        # Colores disponibles
        self.colores = ['teal', 'red', 'yellow', 'blue']

        # Botones
        self.botones = []
        for i in range(4):
            boton = tk.Button(self, bg=self.colores[i], command=lambda i=i: self.verificar_color(i))
            boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
            self.botones.append(boton)

        # Generar una secuencia aleatoria
        self.secuencia = [random.choice(self.colores) for _ in range(5)]
        self.indice_actual = 0

        # Mostrar la secuencia
        self.mostrar_secuencia()

    def mostrar_secuencia(self):
        if self.indice_actual < len(self.secuencia):
            color_actual = self.secuencia[self.indice_actual]
            self.botones[self.colores.index(color_actual)].config(state='active')
            self.after(1000, self.ocultar_color)
        else:
            print("Fin de la secuencia")

    def ocultar_color(self):
        color_actual = self.secuencia[self.indice_actual]
        self.botones[self.colores.index(color_actual)].config(state='normal')
        self.indice_actual += 1
        self.mostrar_secuencia()

    def verificar_color(self, boton_presionado):
        color_presionado = self.colores[boton_presionado]
        if color_presionado == self.secuencia[self.indice_actual]:
            # El color es correcto
            self.indice_actual += 1
            if self.indice_actual == len(self.secuencia):
                print("¡Correcto! Siguiente nivel.")
                # Generar el siguiente color en la secuencia
                self.secuencia.append(random.choice(self.colores))
                self.indice_actual = 0
                self.mostrar_secuencia()
        else:
            print("¡Incorrecto! Fin del juego.")
            # Reiniciar el juego
            self.secuencia = [random.choice(self.colores) for _ in range(5)]
            self.indice_actual = 0
            self.mostrar_secuencia()

if __name__ == '__main__':
    app = SimonDice()
    app.mainloop()
