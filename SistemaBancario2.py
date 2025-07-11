saldo = 0.00
limite = 500.00
extrato = ""
n_saque = 0
lim_saldo = 3
usuarios = []
n_agencia = '0001'
contas = []
continuar = True


#Function depositar
def depositar (valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\033[32mDepósito: R${valor:.2f}\033[m\n"
        print(f"\n   Deposito realizado com sucesso!")

        return saldo, extrato

    else:
        print("\n   Falha na operação! O valor inserido é inválido!")



#Function sacar
def sacar (*, saldo, valor, extrato, n_saque, lim_saldo, limite):
    excedeu_saque = n_saque >= lim_saldo
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite

    if excedeu_saque:
        print("\n   Falha na operação! Número máximo de saques execido.")
        return saldo, extrato, n_saque

    elif excedeu_saldo:
        print("\n   Falha na operação! Não há saldo suficiente.")
        return saldo, extrato, n_saque

    elif excedeu_limite:
        print(f"\n   Falha na operação! Valor do saque excede o limite de R${limite:.2f}")
        return saldo, extrato, n_saque

    elif valor > 0:
        extrato += f"\033[31mSaque: R${valor:.2f}\033[m\n"
        saldo -= valor
        n_saque += 1
        print("\n   Saque realizado com sucesso!")

        return saldo, extrato, n_saque

    else:
        print("\n   Falha na operação! O valor inserido é inválido.")
        return saldo, extrato, n_saque

#Function extrato
def verextrato(extrato, saldo):
    print("\n----------- EXTRATO -----------\n")
    print("Não houve movimentações por enquanto." if not extrato else extrato)
    print(f"\nSaldo atual: \033[33mR${saldo:.2f} \033[m")
    print("________________________________")



#Function Cadastra cliente
def cadastracliente(usuarios):
    cpf_digitado = input("Para o cadastro de um novo usuário insira o cpf (apenas números): ")
    if filtra_cpf(cpf_digitado, usuarios):
        print("\n   Falha na operação! Este cpf não é válido para esta operação.")
    else:
        nome = str(input("Insira o nome: "))
        data_nasc = str(input("Insira a data de nascimento (dd-mm-aaaa): "))
        endereco = str(input("Insira o endereço (logradouro, nro - bairro - cidade/sigla estado): "))

        usuarios.append({'nome': nome, 'cpf': cpf_digitado, 'data_nasc': data_nasc, 'endereco': endereco})

        print('\n   Cadastro realizado com sucesso!!')



#Function responsável por criar uma conta corrente
def cria_conta(usuarios, n_agencia, n_conta):
    cpf_digitado = input("\nPara criar uma conta insira o cpf (apenas números): ")
    if filtra_cpf(cpf_digitado, usuarios):
        contas.append({'agencia':n_agencia, 'n_conta':n_conta, 'cpf':cpf_digitado})
        n_conta += 1
        print(f'\n   Conta criada com sucesso!')
        return n_conta
    else:
        print("\n   Falha na operação! Usuário não encontrado.")


#Function listar contas
def lista_conta(usuarios, contas):
    cpf_digitado = input("\nInsira o cpf (apenas números): ")
    if filtra_cpf(cpf_digitado, usuarios):
        conta_usuario = [c for c in contas if c['cpf'] == cpf_digitado]

        if conta_usuario:
            print("----- Conta(s) do usuário -----")
            for conta in conta_usuario:
                print(conta)
        else:
            print("\n   Falha na operação! Esse usuário não possui conta.")
    else:
        print("\n  Falha na operação! Usuário não encontrado.")


#Função de excluir conta
def exclui_conta(contas):
    n_conta_digitado = int(input("\n Insira o número da conta que deseja excluir:"))
    encontrou = False
    for n in contas:
        if n['n_conta'] == n_conta_digitado:
            print(n)
            resposta = input("\n Deseja mesmo exclir esta conta? (s/n)")
            if resposta == "s":
                contas.remove(n)
                print("\n    Conta excluida com sucesso!")
                break
            else:
                print("\n   Operação cancelada.")
            encontrou = True
            break
    if not encontrou:
        print("\n   Falha na operação! número de conta inválido.")


# Function para evitar a duplicidade de cpfs
def filtra_cpf(cpf_digitado, usuarios):
    for v in usuarios:
        if v['cpf'] == cpf_digitado:
            return True
    return False

menu = """

    ---- Selecione uma opção ----

        [1] Depositar   
        [2] Sacar
        [3] Extrato 
        [4] Criar usuário
        [5] Criar conta
        [6] Mostrar conta(s)
        [7] Excluir conta
        [8] Sair

    -----------------------------
    =>"""



while continuar:

    opc = input(menu)

#opção de depositar
    if opc == "1":
        valor = float(input("Insira o valor a ser depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)


# opção de sacar
    elif opc == "2":
        valor = float(input("Insira o valor do saque: "))
        saldo, extrato, n_saque = sacar(saldo=saldo, extrato=extrato, n_saque=n_saque, valor=valor,  lim_saldo=lim_saldo, limite=limite)


# opção de extrato
    elif opc == "3":
        verextrato(extrato, saldo)


# opção de cadastrar cliente
    elif opc == "4":
        cadastracliente(usuarios)


# opção de criar conta
    elif opc == "5":
        n_conta = len(contas) + 1
        cria_conta(usuarios, n_agencia, n_conta)

# opção de mostrar as contas do usuário
    elif opc == "6":
        lista_conta(usuarios, contas)

# opção de excluir a conta
    elif opc == "7":
        exclui_conta(contas)

# opção de sair
    elif opc == "8":
        print("\nAgradecemos pela preferência, volte sempre!")
        continuar = False
    else:
        print("\n   Falha na operação! Selecione uma opção válida.")


