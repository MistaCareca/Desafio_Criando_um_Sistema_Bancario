from datetime import date

saldo = {"valor": 0}
operacoes = []
controle_saque = {
    "limite": 0,
    "data_ultimo_saque": date.today().strftime('%d/%m/%Y')
}