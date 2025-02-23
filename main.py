from operacoes.saque import saque
from operacoes.deposito import deposito
from operacoes.extrato import extrato
from operacoes.user import Pessoa, Ender, User
from operacoes.contaCorrente import ContaCorrente
import time


def criar_usuario():
    print("Bem-vindo ao Banco Python!")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    print("=====================================")
    print(f"Olá, {nome}!")
    print("vamos adicionar seu endereço:")
    rua = input("Rua: ")
    numero = input("Número: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    print(f"Perfeito, {nome}!")
    print("Conta criada com sucesso!")
    pessoa = Pessoa(nome, cpf, telefone, email)
    endereco = Ender(rua, numero, cidade, estado, cep)
    user = User(pessoa, endereco)
    return user


def menu():
    while True:
        escolha = input("""
[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair
Escolha uma opção: """)

        match escolha:
            case '1':
                print("-Sacar-")
                valor = float(input("Digite o valor do saque: "))
                saque(valor)
            case '2':
                print("-Depositar-")
                valor = float(input("Digite o valor do depósito: "))
                deposito(valor)
            case '3':
                print("-Extrato-")
                extrato()
            case '4':
                print("-Sair-")
                print("Saindo...")
                time.sleep(2)
                print("Finalizado")
                break
            case _:
                print("Opção inválida! Tente novamente.")

usuario = criar_usuario()
conta_corrente = ContaCorrente(usuario)

print("\n=== Conta ===")
print(ContaCorrente)

menu()
