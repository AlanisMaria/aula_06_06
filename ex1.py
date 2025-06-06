class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        print("Este animal emite som")

class Cachorro (Animal):
    def emitir_som(self):
       print(f"{self.nome} diz: Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")

#Teste

rex = Cachorro("Rex")
rex.emitir_som()
mike = Gato("Mike")
mike.emitir_som()
