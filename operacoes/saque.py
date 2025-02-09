from datetime import date
from operacoes import saldo, operacoes, controle_saque  

def saque(valor_saque):
    global controle_saque  

    data_atual = date.today().strftime('%d/%m/%Y')

    if controle_saque["data_ultimo_saque"] != data_atual:
        controle_saque["limite"] = 0  
        controle_saque["data_ultimo_saque"] = data_atual  

    if controle_saque["limite"] >= 3:
        print("Você já atingiu o limite de 3 saques hoje.")
        return saldo["valor"]
    
    if valor_saque > 500:
        print("Operação inválida: O valor máximo por saque é R$ 500.")
        return saldo["valor"]

    if valor_saque > saldo["valor"]:
        print("Operação inválida: saldo insuficiente.")
        print(f"Saldo disponível: {saldo['valor']}")
        return saldo["valor"]

    saldo["valor"] -= valor_saque
    controle_saque["limite"] += 1 
    operacoes.append(["Saque", valor_saque]) 
    print(f"Saque de R$ {valor_saque} realizado com sucesso. Novo saldo: R$ {saldo['valor']}")
    return saldo["valor"]
