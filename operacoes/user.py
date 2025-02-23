class Ender:
    def __init__(self,rua,numero,cidade,estado,cep):
        self.rua = rua 
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}, CEP: {self.cep}"

class Pessoa:
    def __init__(self,nome,cpf,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}\nEmail: {self.email}"

class User:
    def __init__(self, Pessoa, Ender):
        self.Pessoa = Pessoa
        self.Ender = Ender

    def __str__(self):
        return f"{self.pessoa}\nEndereço: {self.endereco}"