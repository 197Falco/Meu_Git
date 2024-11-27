#Primeira coisa, declarar variável Menu

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = "" #variavel tipo string
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor #se for maior de 0, eu adiciono(atribuo) o valor ao meu saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor #Subtrai o valor de saque do saldo restante
            extrato += f"Saque: R$ {valor:.2f}\n" #\n fora das chaves #agrega à string extrato com o número do valor que saquei
            numero_saques += 1 #contabiliza 1 saque
        
        else:
            print("Operação falhou! O valor informado é invalido")
            
    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
       # print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    