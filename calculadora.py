# Calculadora
import tkinter as tk
import operacoes as op

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Simples")

        # Criação do campo de entrada
        self.entry = tk.Entry(root, width=30, font=('Helvetica', 20))
        self.entry.grid(row=0, column=0, columnspan=4)

        # Definição dos botões
        Botoes = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '.',
            'C', '0', '=', '%'
            '*', '÷', '^', '√'
        ]

        # Posicionamento dos botões
        Linhas, Colunas = 1, 0
        for Botao in Botoes:
            if Botao == "√":
                Acao = lambda x = Botao: self.calcular_raiz()
            else:
                Acao = lambda x = Botao: self.click(x)

            tk.Button(root, text=Botao, width=6, height=3, command=Acao).grid(row=Linhas, column=Colunas)
            Colunas += 1
            if Colunas > 3:
                Colunas = 0
                Linhas += 1

    def click(self, botao):
        valor_atual = self.entry.get()

        if botao == "=":
            try:
                resultado = eval(valor_atual)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(resultado))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif botao == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, botao)

    def calcular_raiz(self):
        try:
            valor = float(self.entry.get())
            resultado = op.RaizQuadrada(valor)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(resultado))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Erro")


# Inicializar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
