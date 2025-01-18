def banco():
    disponivel = 2000

    print("Digite 's' para sacar, 'd' para depositar, 't' para transferir, 'v' para ver saldo, ou pressione outra tecla para sair:")
    acao = input("O que deseja fazer? ")

    def fazer(acao):
        nonlocal disponivel  # Para acessar a variável disponivel da função externa

        if acao == "s":
            sim_e_nao = input("Confirme para sacar ('s' - sim, 'n' - não): ")

            if sim_e_nao == "s":
                valor_sacar = int(input("Informe o valor que deseja sacar: "))

                if 0 < valor_sacar <= disponivel:
                    disponivel -= valor_sacar
                    status = "sucesso"
                    print("Seu saque foi um " + status + ". Valor sacado: " + str(valor_sacar) + ". Valor disponível: " + str(disponivel))
                else:
                    print("Valor inválido.")
                    return fazer(acao)

            elif sim_e_nao == "n":
                print("Volte ao início se quiser selecionar outra opção.")
                return banco()

            else:
                print("Você saiu do saque!")
                return banco()

        elif acao == "d":
            sim_e_nao = input("Confirme para depositar ('s' - sim, 'n' - não): ")

            if sim_e_nao == "s":
                valor_depositar = int(input("Informe o valor que deseja depositar: "))

                if valor_depositar > 0:
                    disponivel += valor_depositar
                    status = "sucesso"
                    print("Seu depósito foi um " + status + ". Valor depositado: " + str(valor_depositar) + ". Valor disponível: " + str(disponivel))
                else:
                    print("Valor inválido.")
                    return fazer(acao)

            elif sim_e_nao == "n":
                print("Volte ao início se quiser selecionar outra opção.")
                return banco()

            else:
                print("Você saiu do depósito!")
                return banco()

        elif acao == "t":
            sim_e_nao = input("Confirme para transferir ('s' - sim, 'n' - não): ")

            if sim_e_nao == "s":
                valor_transferir = int(input("Informe o valor que deseja transferir: "))

                if 0 < valor_transferir <= disponivel:
                    disponivel -= valor_transferir
                    status = "sucesso"
                    print("Sua transferência foi um " + status + ". Valor transferido: " + str(valor_transferir) + ". Valor disponível: " + str(disponivel))
                else:
                    print("Valor inválido.")
                    return fazer(acao)

            elif sim_e_nao == "n":
                print("Volte ao início se quiser selecionar outra opção.")
                return banco()

            else:
                print("Você saiu da transferência!")
                return banco()

        elif acao == "v":
            print("Seu saldo: " + str(disponivel))

        else:
            print("Você saiu!")

    fazer(acao)


banco()

