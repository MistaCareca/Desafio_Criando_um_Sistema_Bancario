from operacoes import operacoes, saldo  

def extrato():
    print("\nHistórico de Operações:")
    if not operacoes:
        print("Nenhuma operação registrada.")
        return
    
    for operacao in operacoes:
        print(f"Tipo: {operacao[0]}, Valor: R$ {operacao[1]}")
    print(f"Saldo disponível: {saldo['valor']}") 
