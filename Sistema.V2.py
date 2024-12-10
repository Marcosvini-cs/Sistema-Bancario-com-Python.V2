def menu():
    menu = '''
    ==========MENU==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [l] Listar contas
    [nu] Novo usuário
    [i] Informações
    [q] Sair
    ========================
    => '''
    return input(menu)

def saque(*, valor_saque, limite, saldo, extrato, numero_saques):
    
    if valor_saque <= saldo:
        if valor_saque <= limite:
            saldo -= valor_saque
            extrato += f'Saque: R${valor_saque:.2f}\n'
            numero_saques += 1
            print('\nSaque realizado com sucesso!')

        else:
            print('-=-'*21)
            print('Operação falhou! O valor informado extrapola limite por saque.')
            print('-=-'*21)
        
    else:
        print('-=-'*18)
        print('Operação falhou! O valor informado extrapola seu saldo')
        print('-=-'*18)

    return extrato, saldo, numero_saques

def deposito(saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print('\nDeposito realizado com sucesso!')

    else:
        print('-=-'*16)
        print("Operação falhou! O valor informado é inválido.")
        print('-=-'*16)

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        print("\n================ EXTRATO ================")
        print(extrato)
        print(f'\n|Seu saldo: R${saldo:.2f}|')
        print("==========================================")
    else: 
        print('\nAinda não ocorreu nenhuma movimentação.')

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    if contas:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(linha)
    
    else:
        print('\nNão há contas')

def main():
    saldo = 0
    limite = 500
    extrato = ''''''
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = '0001'

    while True:
        opcao = menu()

        match opcao:
            case 'd':
                valor = float(input('Informe o valor do depósito: '))

                saldo, extrato = deposito(saldo, extrato, valor)
                
            case 's':
                if numero_saques == limite_saques:
                    print('\nVocê atingiu o limite de saques.')
                    continue

                print(f'|Seu saldo: R${saldo:.2f}|')

                valor_saque = float(input('Informe o valor do saque: '))

                extrato, saldo, numero_saques = saque(valor_saque= valor_saque,
                                                       limite= limite, saldo= saldo,
                                                         extrato= extrato,
                                                           numero_saques= numero_saques)

            case 'e':
                exibir_extrato(saldo, extrato= extrato)

            case 'nc':
                numero_conta = len(contas) + 1
                conta = criar_conta(agencia, numero_conta, usuarios)

                if conta:
                    contas.append(conta)
                    print(contas)

            case 'l':
                listar_contas(contas)

            case 'nu':
                criar_usuario(usuarios)

            case 'i':
                print('''- O limite por saque é R$500,00
    - Só pode ser realizado 3 saques diários''')

            case 'q':
                break

            case e:
                print('-=-'*23)
                print('Operação inválida, por favor selecione novamente a operação desejada.')
                print('-=-'*23)
main()