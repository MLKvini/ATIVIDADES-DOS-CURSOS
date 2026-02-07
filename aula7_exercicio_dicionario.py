ecommerce = {
'livro':25.15,
'tablet':3000.0,
'fone':500.0,
'videogame':2000.0,
'celular':1550.0,
}

carrinho = {
'produtos':[],
'valores':[]
}

produto1 = input('produto: ')
produto2 = input('produto: ')
produto3 = input('produto: ')

carrinho['produtos'].append(produto1)
carrinho['produtos'].append(produto2)
carrinho['produtos'].append(produto3)
carrinho['valores'].append(ecommerce[produto1])
carrinho['valores'].append(ecommerce[produto2])
carrinho['valores'].append(ecommerce[produto3])

soma =  sum(carrinho['valores'])

print('Total -  R$', soma)

print(carrinho)

formas_pagamentos =  ['pix','cc','cd']
print('escolha a  forma de pagamento: ', formas_pagamentos)
escolhe_forma = input('COLOCA A FORMA DE PAGAMNETO: ')
indice = formas_pagamentos.index(escolhe_forma)
print('Forma de pagamento: ', formas_pagamentos[indice])
print('VOLTE SEMPRE ')