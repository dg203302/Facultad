import tkinter as tk
class SimonDiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simon Dice")
        self.geometry("400x300")
        self.resizable(width=True, height=True)
        self.configure(bg="gray")
        #menu
        self.menu=tk.Menu()
        self.config(menu=self.menu)
        archimenu = tk.Menu(self.menu, tearoff=False)
        # Agregarlo a la barra.
        self.menu.add_cascade(menu=archimenu, label="Archivo")
        # menu
        # Create colored buttons
        self.create_colored_button("teal", 0, 0)
        self.create_colored_button("red", 0, 1)
        self.create_colored_button("yellow", 1, 0)
        self.create_colored_button("blue", 1, 1)

        # Create a label for the score
        self.score_label = tk.Label(self, text="Points: 0", bg="gray", fg="white")
        self.score_label.grid(row=2, column=0, columnspan=2)  # Utiliza grid() aquí

    def create_colored_button(self, color, row, column):
        button = tk.Button(self, bg=color)
        button.grid(row=row, column=column, sticky="nswe")

        # Configure expansion behavior
        self.columnconfigure(column, weight=1)
        self.rowconfigure(row, weight=1)

if __name__ == "__main__":
    app = SimonDiceApp()
    app.mainloop()
