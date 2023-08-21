DEPOSITO = None

def aplicacao():
    
    saldo_conta = 0
    valor_deposito = 0
    valor_saque = 0
    LIMITE_SAQUE = 0

    while True:
        menu()
        opcao = input("Escolha um opção: ")
    
        if opcao.lower() == "d":
            v_deposito = float(input("Qual valor deseja depositar? R$: "))
            d = deposito(v_deposito)
            valor_deposito += d
        elif opcao.lower() == "e":
            saldo_conta = valor_deposito - valor_saque
            extrato(valor_deposito, valor_saque, saldo_conta)
        elif opcao.lower() == 's':
            v_saque = float(input("Qual valor deseja sacar? R$: "))
            if v_saque > saldo_conta:
                print("SALDO INSUFICIENTE!")
            elif LIMITE_SAQUE == 3:
                print("LIMITE DE SAQUE EXCEDIDO!")
            else:
                LIMITE_SAQUE += 1
                print("AQUI" ,LIMITE_SAQUE)
                s = saque(v_saque, LIMITE_SAQUE)
                valor_saque += s
        elif opcao.lower() == "q":
            break
    
    print(saldo_conta)
    

def menu():
    print("""
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
    """)

def deposito(valor_deposito):
    total_depositado = 0

    if valor_deposito <= 0.0:
        print("Não é permitido depósitos com valores negativos. Operação encerrada!")
    else:
        total_depositado += valor_deposito
        while True:
            escolha = input("Deseja realizar outro depósito? (s/n) ")
            if escolha.lower() == 's':
                valor_deposito = float(input("Qual valor deseja depositar? R$: "))
                total_depositado += valor_deposito
            else:
                break   
    
    return total_depositado

def saque(valor_saque, LIMITE_SAQUE):
    total_saque = 0
    print(LIMITE_SAQUE)
    
    if valor_saque >= 500:
        print("Limite por saque excedido! Operação encerrada!")
    else:
        total_saque += valor_saque
        while True:
            escolha = input("Deseja realizar outro saque? (s/n) ")
            if escolha.lower() == 's':
                LIMITE_SAQUE += 1
                print(LIMITE_SAQUE)
                valor_saque = float(input("Qual valor deseja sacar? R$: "))
                total_saque += valor_saque
                if LIMITE_SAQUE == 3:
                    print("Limite diário de saque excedido!")
                    break
            else:
                break
    
    return total_saque

def verificarSaldo():
    
    return

def extrato(deposito, saque, saldo):
    print("(+) Depósitos R$: ", deposito)
    print("(-) Saques R$: ", saque)
    print("(=) Saldo Total R$: ", saldo)

aplicacao()