saldo = 0
while True:
    print('[1] Depositar')
    print('[2] Sacar')
    print('[3] Mostrar Saldo')
    print('[0] Sair')
    opcao = int(input("Opção: "))
    if opcao == 1:
        valor = float(input("Valor: "))
        saldo += valor
    elif opcao == 2:
        valor = float(input("Valor: "))
        if valor < saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente!!!")
    elif opcao == 3:
        print(f'Saldo: {saldo}')
    elif opcao == 0:
        print("Já vai tarde!!!")
        break
    else:
        print("Opção inválida!!!")
