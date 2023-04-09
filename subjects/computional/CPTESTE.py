# Introdução do Programa:
print('\n| Bem vindo ao seguro bike da porto ! | ')
# Flag 1:
programa = ''
# Repetição (Não finaliza até o usuário querer): 
while programa != 'FIM':
    print('\nEscolha uma opção: ')
    print('[ 1 ] Ajuda. \n[ 2 ] Suporte. \n[ 3 ] F.A.Q. \n[ 4 ] Contato com um atendente. \n[ F ] Terminar programa. ')
    # Input da Opção:
    opcao = input('Opção: ')
    # Verificação da Opção
    if opcao.isnumeric():
        # True (é uma das 4 opções de retorno):
        opcao = int(opcao)
        match opcao:
            case 1:
                print('\nOpção | Ajuda | selecionada. ')
                print('\nSelecione uma opção: ')
                print('[ 1 ] Ajuda com a documentação. \n[ 2 ] Ajuda com a Nota fiscal. \n[ 3 ] Ajuda com a foto da bike. \n[ 4 ] Outros. ')
                opcao = input('Opção: ')
                if opcao.isnumeric():
                    opcao = int(opcao)
                    match opcao:
                        case 1:
                            print('\nOpção | Ajuda com a documentação | selecionada. ')
                            print('| FIM |')
                        case 2:
                            print('\nOpção | Ajuda com a nota fiscal | selecionada. ')
                            print('| FIM |')
                        case 3:
                            print('\nOpção | Ajuda com a foto da bike | selecionada. ')
                            print('| FIM |')
                        case 4:
                            print('\nOpção | Outros | selecionada. ')
                            print('| FIM |')
                        case _:
                            print(f'| ERRO | \nOpção {opcao} não existe. ')
                else:
                    print('\n| ERRO | \nOpção inválida, digite um valor (NÚMERO) válido. ')    
            case 2:
                print('\nOpção | Suporte | escolhida. ')
                print('\nSelecione uma opção: ')
                print('[ 1 ] Problema com envio. \n[ 2 ] Problema com o envio da Nota Fiscal. \n[ 3 ] Problema com envio da proposta. \n[ 4 ] Problema em concluir a tarefa. \n[ 5 ] Outros. ')
                opcao = input('Opção: ')
                if opcao.isnumeric():
                    opcao = int(opcao)
                    match opcao:
                        case 1:
                            print('\nOpção | Problema com envio | selecionada. ')
                            print('| FIM |')
                        case 2:
                            print('\nOpção | Problema com o envio da Nota fiscal | selecionada. ')
                            print('| FIM |')
                        case 3:
                            print('\nOpção | Problema com o envio da proposta | selecionada. ')
                            print('| FIM |')
                        case 4:
                            print('\nOpção | Problema em concluir a tarefa | selecionada. ')
                            print('| FIM |')
                        case 5:
                            print('\nOpção | Outros | selecionada. ')
                            print('| FIM |')
                        case _:
                            print(f'| ERRO | \n Opção {opcao} não existe. ')
                else:
                    print('| ERRO | \nOpção inválida, digite um valor (NÚMERO) válido. ')
            case 3:
                print('\nOpção | F.A.Q. | escolhida. ')
                print('\nSelecione uma opção:')
                print('[ 1 ] Quais documentos são aceitos. \n[ 2 ] Como o sistema identifica a minha bike. \n[ 3 ] O que acontece se o sistema não identificar a minha bike. \n[ 4 ] Como funciona o sistema. \n[ 5 ] cancelar.')
                opcao = input('Opção: ')
                if opcao.isnumeric():
                    opcao = int(opcao)
                    match opcao:
                        case 1:
                            print('Opção | Quais documentos são aceitos | selecionada. ')
                            print('| FIM |')
                        case 2:
                            print('Opção | Como o sistema identifica a minha bike | selecionada. ')
                            print('| FIM |')
                        case 3:
                            print('Opção | O que acontece se o sistema não identificar a minha bike | selecionada. ')
                            print('| FIM |')
                        case 4:
                            print('Opção | Como funciona o sistema | selecionada. ')
                            print('| FIM |')
                        case 5:
                            print('Opção | cancelar | selecionada. ')
                        case _:
                            print(f'| ERRO | \n Opção {opcao} não existe. ')
                else:
                    print('| ERRO | \nOpção inválida, digite um valor (NÚMERO) válido. ')
            case 4:
                print('\nOpção | Contato com atendente | escolhida. ')
                print('\nConfirmação necessária, deseja falar com um atendente? \n[ 1 ] Sim. \n[ 2 ] Não')
                opcao = input('Opção: ')
                if opcao.isnumeric():
                    opcao = int(opcao)
                    match opcao:
                        case 1:
                            print('Número do Atendente #000000000. ')
                            print('| FIM |')
                        case 2:
                            print('Voltando ao menu ...')
                        case _:
                            print(f'| ERRO | \n Opção {opcao} não existe. ')
                else:
                    print('| ERRO | \nOpção inválida, digite um valor (NÚMERO) válido. ')
            case _:
                print(f'\n| ERRO | \nOpção {opcao} não existe. ')
    elif opcao.upper() == 'F':
        # True (é a opção final):
        programa = 'confirmacao'
        while programa == 'confirmacao':
            print('\nDeseja finalizar o programa? \n[ 1 ] Sair. \n[ 2 ] Cancelar. ')
            # Confirmação de finalização:
            opcao = input('Opção: ')
            if opcao.isnumeric():
                opcao = int(opcao)
                match opcao:
                    case 1:
                        # True (Fim do programa):
                        print('\n| Atendimento finalizado |\n ')
                        programa = 'FIM'
                    case 2:
                        # True (Fim do programa cancelado)
                        print('\n| Finalização cancelada | ')
                        programa = ''
                    case _:
                        print(f'\n| ERRO | \nOpção {opcao} não existe. ')
            else:
                # False (Opção inválida)
                print('\n| ERRO | \nOpção inválida, digite um valor (NÚMERO) válido. ')
    else:
        # False (opção inválida):
        print('\n| ERRO | \nOpção válida, digite um valor (NÚMERO) válido. ')
