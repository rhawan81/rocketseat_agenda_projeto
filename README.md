# Documentação das modificações em `agenda.py`

Este arquivo descreve as alterações realizadas no projeto para habilitar a edição de nome e celular de um contato quando o usuário escolhe a opção 3 ("Editar Contato"). As instruções abaixo devem ajudar você a entender o que foi alterado, porque e como testar.

## Resumo das mudanças

- Corrigida a função `editar_contato` (assinatura e comportamento):
  - Antes: a função estava com assinatura e parâmetros incorretos e causava problemas de chamada.
  - Agora: `def editar_contato(lista_de_contato, indice_contato, novo_nome=None, novo_celular=None):`
    - Atualiza somente os campos informados (nome e/ou celular).
    - Verifica se o índice informado é válido.
    - Usa a chave `"nome"` (minúscula) para manter consistência com o restante do código.

- Implementado o fluxo de entrada do usuário no bloco `elif escolha_user == 3`:
  - Exibe a agenda (se houver contatos).
  - Pergunta o índice do contato a editar (validação básica de entrada numérica).
  - Pergunta se deseja alterar o nome (sim/nao). Se "sim", pede o novo nome.
  - Pergunta se deseja alterar o celular (sim/nao). Se "sim", pede o novo número.
  - Chama `editar_contato` passando apenas os campos a alterar.
  - Mensagens de erro/aviso para agenda vazia e entrada inválida.

## Detalhes técnicos (o que foi mudado no código)

1. Função `editar_contato`:
   - Assinatura atual: `editar_contato(lista_de_contato, indice_contato, novo_nome=None, novo_celular=None)`
   - Comportamento:
     - Converte o índice do usuário para índice interno (0-based): `indice_ajustado = indice_contato - 1`.
     - Valida que `0 <= indice_ajustado < len(lista_de_contato)`.
     - Atualiza `lista_de_contato[indice_ajustado]["nome"]` se `novo_nome` foi informado.
     - Atualiza `lista_de_contato[indice_ajustado]["celular"]` se `novo_celular` foi informado.
     - Em caso de índice inválido, imprime mensagem apropriada.

2. Fluxo de edição no menu (opção 3):
   - Trata `Agenda vazia` caso não existam contatos.
   - Usa `try/except ValueError` ao converter entrada para inteiro.
   - Normaliza respostas de confirmação com `strip().lower()` (compara com 'sim').
   - Permite atualizar somente nome, somente celular, ambos ou nenhum (neste último caso a função é chamada sem alterações e apenas imprime que foi atualizado).

## Como testar manualmente (Windows PowerShell)

1. Abra um terminal no diretório do projeto (onde está `agenda.py`).

2. Execute o script:

```powershell
python "c:\Users\ZE LOKO DMC $\Documents\rockeatseat_projeto_agenda\agenda.py"
```

3. Passos para um teste simples:
   - Escolha 1 para adicionar um contato. Informe nome, telefone e email.
   - Escolha 2 para ver a agenda e confirmar o contato foi salvo.
   - Escolha 3 (Editar Contato):
     - O programa exibirá a lista numerada. Informe o número do contato a alterar.
     - Quando perguntado "Deseja mudar o nome? (sim/nao):" responda "sim" e digite o novo nome; ou "nao" para pular.
     - Quando perguntado "Deseja mudar o celular? (sim/nao):" responda "sim" e digite o novo número; ou "nao" para pular.
   - Escolha 2 novamente para verificar as alterações.

## Comandos úteis para verificação automática

- Checar sintaxe (rápido):

```powershell
python -m py_compile "c:\Users\ZE LOKO DMC $\Documents\rockeatseat_projeto_agenda\agenda.py"
```

Se o comando terminar sem mensagens de erro, o arquivo está sintaticamente válido.

## Observações, limitações e possíveis melhorias

- Validação de telefone: atualmente o programa aceita qualquer string; seria útil normalizar/validar o formato de telefone.
- Validação de nome: falta verificação para strings vazias; hoje se o usuário fornecer uma string vazia, o campo pode ser atualizado para vazio.
- Exclusão e marcação de favoritos ainda não foram implementadas (opções 4 e 5 atualmente vazias/noop).
- Testes automatizados: seria benéfico adicionar testes unitários simples (por exemplo, usando `unittest`) para a função `editar_contato`.

## Local das alterações

- `agenda.py` (arquivo principal) — implementações realizadas direto neste arquivo.

## Exemplo de interação (resumida)

1. Adicionar contato:
   - 1
   - Nome: Maria
   - Telefone: 11999999999
   - Email: maria@example.com

2. Editar contato:
   - 3
   - Informe o número que deseja atualizar: 1
   - Deseja mudar o nome? (sim/nao): sim
   - Digite o novo nome: Maria Silva
   - Deseja mudar o celular? (sim/nao): nao

3. Resultado: contato 1 terá `nome` alterado para "Maria Silva" e celular inalterado.

---

Se quiser, eu também posso:
- Adicionar validação mínima de formato para celular (ex.: aceitar apenas dígitos e tamanho mínimo).
- Implementar testes unitários para `editar_contato`.
- Completar as opções 4 (deletar) e 5 (favorito).

Diga qual destas melhorias você prefere que eu implemente em seguida.