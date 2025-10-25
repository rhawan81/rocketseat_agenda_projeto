
# --- 1. DEFINIÇÃO DE TODAS AS FUNÇÕES ---

def adicionar_infos(lista_de_contatos, nome, telefone, email):
    """Adiciona um novo contato à lista."""
    agenda = {"nome": nome,
              "celular": telefone,
              "email": email,
              "favorito": False}
    lista_de_contatos.append(agenda)
    print(f'Contato {nome} adicionado com sucesso')
    return

def ver_agenda(lista_de_contatos):
    """Mostra todos os contatos da lista."""
    print("\n--- SUA AGENDA ---")
    if not lista_de_contatos:
        print('Agenda vazia.')
        return

    for indice, contatos in enumerate(lista_de_contatos, start=1):
        status = "✓" if contatos["favorito"] else " "
        nome_cliente = contatos["nome"]
        email_cliente = contatos["email"]
        tel = contatos["celular"]
        print(f'[{status}] {indice}. {nome_cliente} | Email: {email_cliente} | Telefone: {tel}')
    print("------------------\n")
    return

def editar_contato(lista_de_contato, indice_contato, novo_nome=None, novo_celular=None, novo_email=None):
    """Edita nome, celular ou email de um contato existente."""
    indice_ajustado = indice_contato - 1
    
    if 0 <= indice_ajustado < len(lista_de_contato):
        # Atualiza apenas os campos que foram fornecidos (não são None)
        if novo_nome:
            lista_de_contato[indice_ajustado]["nome"] = novo_nome
        if novo_celular:
            lista_de_contato[indice_ajustado]["celular"] = novo_celular
        # Bônus: adicionei a edição de email também
        if novo_email:
             lista_de_contato[indice_ajustado]["email"] = novo_email
             
        print(f'Contato {indice_contato} foi atualizado.')
    else:
        print('Erro: Índice de contato inválido')

def deletar_contato(lista_de_contatos, indice_contato):
    """Remove um contato da lista pelo seu índice."""
    indice_ajustado = indice_contato - 1
    if 0 <= indice_ajustado < len(lista_de_contatos):
        # .pop() remove o item e o retorna, para podermos mostrar o nome
        contato = lista_de_contatos.pop(indice_ajustado)
        print(f'Contato "{contato["nome"]}" (posição {indice_contato}) removido com sucesso.')
    else:
        print('Erro: Índice de contato inválido')

def toggle_favorito(lista_de_contatos, indice_contato):
    """Marca ou desmarca um contato como favorito."""
    indice_ajustado = indice_contato - 1
    if 0 <= indice_ajustado < len(lista_de_contatos):
        contato_atual = lista_de_contatos[indice_ajustado]
        # Inverte o valor booleano: True vira False, False vira True
        contato_atual['favorito'] = not contato_atual['favorito']
        
        status = 'favorito' if contato_atual['favorito'] else 'não favorito'
        print(f'Contato "{contato_atual["nome"]}" agora está {status}.')
    else:
        print('Erro: Índice de contato inválido')

def ver_favoritos(lista_de_contatos):
    """Mostra apenas os contatos marcados como favoritos."""
    print("\n--- CONTATOS FAVORITOS ---")
    # Cria uma lista temporária apenas com contatos onde 'favorito' é True
    favoritos = [c for c in lista_de_contatos if c.get('favorito')]
    
    if not favoritos:
        print('Não há contatos marcados como favoritos.')
        return

    for indice, contatos in enumerate(favoritos, start=1):
        nome_cliente = contatos['nome']
        email_cliente = contatos['email']
        tel = contatos['celular']
        print(f'[✓] {indice}. {nome_cliente} | Email: {email_cliente} | Telefone: {tel}')
    print("--------------------------\n")

# --- 2. INICIALIZAÇÃO DA LISTA ---
lista_de_contatos = []

# --- 3. LOOP PRINCIPAL DO PROGRAMA ---
while True:
    print("""
1. Salvar Contato
2. Ver Agenda contatos
3. Editar Contato
4. Deletar Contato
5. Marcar/Desmarcar Favorito
6. Ver Favoritos
7. Sair da Agenda""")

    try:
        escolha_user = int(input('O que Deseja Fazer na Agenda: '))

        if escolha_user == 1:
            nome = input('Nome do contato que deseja adicionar: ')
            telefone = input('Informe o numero para cadastrar: ')
            email = input('Informe o email do cliente: ')
            adicionar_infos(lista_de_contatos, nome, telefone, email)

        elif escolha_user == 2:
            ver_agenda(lista_de_contatos)

        elif escolha_user == 3:
            if not lista_de_contatos:
                print('Agenda vazia. Nada para editar.')
                continue
                
            ver_agenda(lista_de_contatos)
            try:
                contato_indice = int(input('Informe o número que deseja atualizar: '))
                
                # Verifica se o índice é válido ANTES de pedir os dados
                if not (0 < contato_indice <= len(lista_de_contatos)):
                    print("Erro: Índice inválido.")
                    continue
                    
            except ValueError:
                print('Entrada inválida, informe um número.')
                continue

            # Inicia as variáveis como None
            novo_nome = None
            novo_celular = None
            novo_email = None # Adicionei o email

            # Pergunta para cada campo
            mudar_nome = input('Deseja mudar o nome? (sim/nao): ').strip().lower()
            if mudar_nome == 'sim':
                novo_nome = input('Digite o novo nome: ').strip()

            mudar_cel = input('Deseja mudar o celular? (sim/nao): ').strip().lower()
            if mudar_cel == 'sim':
                novo_celular = input('Digite o novo número: ').strip()

            mudar_email = input('Deseja mudar o email? (sim/nao): ').strip().lower()
            if mudar_email == 'sim':
                novo_email = input('Digite o novo email: ').strip()

            # Chama a função de editar
            editar_contato(lista_de_contatos, contato_indice, novo_nome, novo_celular, novo_email)

        elif escolha_user == 4:
            if not lista_de_contatos:
                print('Agenda vazia. Nada para deletar.')
                continue
                
            ver_agenda(lista_de_contatos)
            try:
                contato_indice = int(input('Informe o número do contato que deseja deletar: '))
                deletar_contato(lista_de_contatos, contato_indice)
            except ValueError:
                print('Entrada inválida, informe um número.')
                continue

        elif escolha_user == 5:
            if not lista_de_contatos:
                print('Agenda vazia.')
                continue
                
            ver_agenda(lista_de_contatos)
            try:
                contato_indice = int(input('Informe o número do contato para marcar/desmarcar favorito: '))
                toggle_favorito(lista_de_contatos, contato_indice)
            except ValueError:
                print('Entrada inválida, informe um número.')
                continue

        elif escolha_user == 6:
            ver_favoritos(lista_de_contatos)

        elif escolha_user == 7:
            print('Saindo Da Agenda, até logo')
            break
            
        else:
            print('Opção inválida. Escolha um número entre 1 e 7.')

    except ValueError:
        print('Erro: Por favor, digite um número válido para a opção do menu.')