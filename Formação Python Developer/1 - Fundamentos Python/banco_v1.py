# deposito tem que ser positivo e armazenado em uma variável para extrato
# saque no max 3 no dia e valor max por saque 500 reais, se nao tiver saldo mostra mensagem, salva na variavel para extrato
# extrato

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao.lower() == "d":
        deposito = float(input("Digite o valor do deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Crédito: R${deposito:.2f}\n"
        else: print("Valor invalido")
    
    elif opcao.lower() == "s":
        saque = float(input("Digite o valor de saque: "))
        if (saque > 0 and saque <= 500) and saque <= saldo:
            if numero_saques < limite_saque:
                saldo -= saque
                extrato += f"Débito: R${saque:.2f}\n"
                numero_saques += 1
            else:
                print("Limite de saque excedido!")
        else:
            print("Valor de saque negado!")
        
    
    elif opcao.lower() == "e":
        print("########## EXTRATO ##########")
        print(extrato)
        print(f"Saldo: {saldo:.2f}")
        print("#############################")
    
    elif opcao.lower() == "q":
        break

    else: print("Opção inexistente, tente novamente!")