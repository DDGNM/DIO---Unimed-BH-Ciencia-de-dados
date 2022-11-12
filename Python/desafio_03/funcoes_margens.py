def preco (custo, margen_liquida):
    preco_result = custo + margen_liquida
    return preco_result

def aumento_preco (preco, percentual_aumento):
    aumento_result = preco + (preco+(percentual_aumento/100))
    return aumento_result

def desconto_preco (preco, percentual_desconto):
    desconto_result = preco - (preco-(percentual_desconto/100))
    return desconto_result

def margen_liquida (preco, custo):
    margen_liquida = (custo - preco)/100
    return margen_liquida