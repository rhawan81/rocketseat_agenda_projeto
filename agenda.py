def adicionar_infos(lista_de_contatos,nome,telefone,email):
    agenda = {"nome":nome,
"celular":telefone,
"email":email,
"favorito":False}
    lista_de_contatos.append(agenda)
    print(f'Contato {nome} adicionado com sucesso')
    return
    
def ver_agenda(lista_de_contatos):
    for indice,contatos in enumerate(lista_de_contatos,start=1):
        status = "✓" if contatos["favorito"] else " "
        nome_cliente = contatos["nome"]
        email_cliente = contatos["email"]
        tel  = contatos["celular"]
        
        print(f'{indice}. {nome_cliente} | seu email é {email_cliente} |  com telefone {tel} | seu status é [{status}]')
    return
def editar_contato(lista_de_contato, indice_contato, novo_nome=None, novo_celular=None):
    indice_ajustado = indice_contato - 1
    if indice_ajustado >= 0 and indice_ajustado < len(lista_de_contato):
        # Atualiza apenas os campos fornecidos
        if novo_nome:
            lista_de_contato[indice_ajustado]["nome"] = novo_nome
        if novo_celular:
            lista_de_contato[indice_ajustado]["celular"] = novo_celular
        print(f'Contato {indice_contato} foi atualizado.')
    else:
        print('Índice de contato inválido')
    
def marca_desmarcar_favorito(lista_de_contatos,novo_indice):
    indice_novo = novo_indice - 1
    if lista_de_contatos[indice_novo]["favorito"] == True:
        lista_de_contatos[indice_novo]["favorito"] = False
        print(f'Contato "{lista_de_contatos[indice_novo]["nome"]}" desmarcado como favorito.')
    else:
        
            lista_de_contatos[indice_novo]["favorito"] = True
            print(f'Contato "{lista_de_contatos[indice_novo]["nome"]}" marcado como favorito!')


def deletar_contato(lista_de_contatos, indice_contato):
    # Ajusta o índice do usuário (começa em 1) para o índice da lista (começa em 0)
    indice_ajustado = indice_contato - 1
    
    # Verifica se o índice é válido para evitar erros
    if 0 <= indice_ajustado < len(lista_de_contatos):
        # Remove o contato da lista usando .pop() e guarda o contato removido
        contato_removido = lista_de_contatos.pop(indice_ajustado)
        print(f'Contato "{contato_removido["nome"]}" foi removido com sucesso.')
    else:
        # Mensagem de erro se o número não existir na lista
        print('Índice de contato inválido.')

lista_de_contatos = []
while True:
    print("""1.Salvar Contato
2.Ver Agenda contatos
3.Editar Contato
4.Marcar Favorito
5.Deletar contato
6.Sair da Agenda""")
    
    escolha_user = int(input('Oque Deseja Fazer na Agenda:'))

    if escolha_user == 1:
        nome = input('Nome do contato que deseja adicionar:')
        telefone = input('Informe o numero para cadastrar:')
        email = input('Informe o email do cliente:')
        adicionar_infos(lista_de_contatos,nome,telefone,email)
        
    elif escolha_user == 2:
       ver_agenda(lista_de_contatos)
    elif escolha_user == 3:
        if not lista_de_contatos:
            print('Agenda vazia.')
        else:
            ver_agenda(lista_de_contatos)
            try:
                contato_indice = int(input('Informe o número que deseja atualizar: '))
            except ValueError:
                print('Entrada inválida, informe um número.')
                continue

            novo_nome = None
            mudar_nome = input('Deseja mudar o nome? (sim/nao): ').strip().lower()
            if mudar_nome == 'sim':
                novo_nome = input('Digite o novo nome: ').strip()

            novo_celular = None
            mudar_cel = input('Deseja mudar o celular? (sim/nao): ').strip().lower()
            if mudar_cel == 'sim':
                novo_celular = input('Digite o novo número: ').strip()

            editar_contato(lista_de_contatos, contato_indice, novo_nome, novo_celular)
        
    elif escolha_user == 4:
        ver_agenda(lista_de_contatos)
        indice_tarefa = int(input('digite o numero da tarefa que deseja completar'))
        marca_desmarcar_favorito(lista_de_contatos,indice_tarefa)
        
        
    elif escolha_user == 5:
        if ver_agenda(lista_de_contatos):   
            try:
                indice_para_deletar = int(input('Digite o número do contato que deseja deletar: '))
                deletar_contato(lista_de_contatos, indice_para_deletar)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    
    elif escolha_user == 6:
        print('Saindo Da Agenda, ate logo')
        break