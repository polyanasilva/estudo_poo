from utilitarios import cadastrar_categoria, cadastrar_transacao, saldo_total

# categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_viagens = cadastrar_categoria('Viagens')
categoria_lazer = cadastrar_categoria('Lazer')

# transacoes
cadastrar_transacao(
    descricao='Salário Jan/2025',
    valor = 1000,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao='Mesada mamãe',
    valor = 50,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao='Ingresso Show',
    valor = -150,
    categoria=categoria_lazer
)

cadastrar_transacao(
    descricao='Conta de luz',
    valor=-100,
    categoria=categoria_contas
)

total = saldo_total()
print(total)