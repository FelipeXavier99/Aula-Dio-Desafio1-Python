saldo = 1000
limite_saque = 0
extrato= ""

while True:
    pergunta = int(input("Digite a operação:\n"
                         "1 - Depósito\n"
                         "2 - Sacar\n"
                         "3 - Extrato\n"
                         "4 - Sair\n"))

    if pergunta == 4:
        break
    
    if pergunta == 1:
        deposito = int(input("Digite o valor do depósito: "))
        saldo += deposito
        ## extrato += f"Depósito: R$ {deposito: 2f}\n"
    elif pergunta == 2 and limite_saque <= 2:
        saque = int(input("Digite o valor do saque: "))
        if saque <= 500 and saldo > 0:   # Verificando limite de saque
            saldo -= saque
            limite_saque += 1
        else:
            print("Limite de saque excedido (R$500) ou está Zerado")
    elif pergunta == 3:
        print("Extrato - Seu saldo é =", saldo)
    else:
        print("Operação Inválida")

print("Encerrando o programa.")
