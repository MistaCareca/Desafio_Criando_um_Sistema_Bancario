from .user import User

class ContaCorrente:
    contas = []
    numero_conta = 1

    def __init__(self, user):  
        for conta in ContaCorrente.contas:
            if conta.user == user:  
                raise Exception("Usuário já possui uma conta.")
            
        self.agencia = "0001"
        self.numero = str(ContaCorrente.numero_conta).zfill(4)
        self.user = user  
        self.saldo = 0
        self.operacoes = []

        ContaCorrente.contas.append(self)
        ContaCorrente.numero_conta += 1
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f"Depósito: +R$ {valor:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.operacoes.append(f"Saque: -R$ {valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato(self):
        print("\n=== Extrato ===")
        if not self.operacoes:
            print("Nenhuma operação realizada.")
        else:
            for operacao in self.operacoes:
                print(operacao)
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
    
    def __str__(self):
        return f"Agência: {self.agencia}\nConta: {self.numero}\nTitular: {self.user.Pessoa.nome}"
    
    @staticmethod
    def listar_contas():
        if not ContaCorrente.contas:
            print("Nenhuma conta cadastrada.")
            return
        else:
            print("\nContas Cadastradas:")
            for conta in ContaCorrente.contas:
                print(conta)
                print("-" * 30)
