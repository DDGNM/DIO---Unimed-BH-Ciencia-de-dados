estados = input().split()
print(estados)
i=0
tamanho = len(estados)
while i < tamanho:
    resposta = estados[i]
    if resposta == "esquerda":
        print("ingles", end="\n")
    elif resposta == "direita":
        print("frances",end="\n")
    elif resposta == "nenhuma":
        print("portugues",end="\n")
    else :
        print("caiu",end="\n")
    i += 1
    #break
