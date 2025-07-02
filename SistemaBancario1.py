menu = """

    ---- Selecione uma opção ----

        [1] Depositar
        [2] Sacar
        [3] Estrato 
        [4] Sair"
        
    -----------------------------
    =>"""

saldo = 0.00
limite = 500.00
extrato = ""
n_saque = 0
lim_saldo = 3

continuar = True

while continuar:

    opc = input(menu)

    if opc == "1":
        valor = float(input("Insira o valor a ser depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\033[32mDepósito: R${valor:.2f}\033[m\n"
            print(f"\nDeposito realizado com sucesso!")

        else:
            print("\nFalha na operação! O valor inserido é inválido!")

    elif opc == "2":
        valor = float(input("Insira o valor do saque: "))

        excedeu_saque = n_saque>=lim_saldo
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if excedeu_saque:
            print("\nFalha na operação! Número máximo de saques execido.")

        elif excedeu_saldo:
            print("\nFalha na operação! Não há saldo suficiente.")

        elif excedeu_limite:
            print(f"\nFalha na operação! Valor do saque excede o limite de R${limite:.2f}")

        elif valor > 0:
            extrato += f"\033[31mSaque: R${valor:.2f}\033[m\n"
            saldo -= valor
            n_saque += 1
            print("\nSaque realizado com sucesso!")

        else:
            print("\nFalha na operação! O valor inserido é inválido.")

    elif opc == "3":
        print("\n----------- EXTRATO -----------\n")
        print("Não houve movimentações por enquanto." if not extrato else extrato)
        print(f"\n Saldo atual: \033[33mR${saldo:.2f} \033[m")
        print("________________________________")

    elif opc == "4":
        print("\nAgradecemos pela preferência, volte sempre!")
        continuar = False



