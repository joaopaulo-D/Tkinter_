from tkinter import *

class App:
    def __init__(self, master = None):  
        self.fontPadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.title = Label(self.primeiroContainer, text="Dados do Cliente")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.nameLabel = Label(self.segundoContainer, text="Nome", font=self.fontPadrao)
        self.nameLabel.pack(side=LEFT)

        self.name = Entry(self.segundoContainer)
        self.name["width"] = 30
        self.name["font"] = self.fontPadrao
        self.name.pack(side=LEFT)

        self.passwordLabel = Label(self.terceiroContainer, text="Senha", font=self.fontPadrao)
        self.passwordLabel.pack(side=LEFT)

        self.password = Entry(self.terceiroContainer)
        self.password["width"] = 30
        self.password["font"] = self.fontPadrao
        self.password["show"] = "*"
        self.password.pack(side=LEFT)

        self.auth = Button(self.quartoContainer)
        self.auth["text"] = "Autenticar"
        self.auth["font"] = ("Calibri", "8")
        self.auth["width"] = 12
        self.auth["command"] = self.verificarPassword
        self.auth.pack()

        self.msg = Label(self.quartoContainer, text="", font=self.fontPadrao)
        self.msg.pack()

    def verificarPassword(self):
        user_auth = self.name.get()
        password_auth = self.password.get()

        user = "devjoao"
        password = "dev"

        if user_auth == user and password_auth == password:
            self.msg["text"] = "Bem-vido ao sistema do Joao Paulo " + user_auth
        else:
            self.msg["text"] = "Por favor preecha todos os campos ;)"

root = Tk()
App(root)
root.mainloop()      