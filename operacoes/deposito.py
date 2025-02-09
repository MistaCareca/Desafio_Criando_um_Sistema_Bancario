from operacoes import saldo, operacoes  

def deposito(valor_deposito):
    if valor_deposito <= 0:
        print("Valor inválido para depósito.")
        return saldo["valor"] 
    
    saldo["valor"] += valor_deposito  
    operacoes.append(["Depósito", valor_deposito])
    print(f"Depósito de R$ {valor_deposito} realizado com sucesso. Novo saldo: R$ {saldo['valor']}")
    return saldo["valor"]
