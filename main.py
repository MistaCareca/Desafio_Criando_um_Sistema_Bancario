from operacoes.saque import saque
from operacoes.deposito import deposito
from operacoes.extrato import extrato
import time

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

menu()
