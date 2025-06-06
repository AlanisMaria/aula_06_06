class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")


aluno1 = Aluno("João Silva", 20, "2023001", "Engenharia de Software")


aluno1.exibir_dados()