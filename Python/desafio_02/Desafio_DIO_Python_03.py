salario = float(input())

aumento1 = 0.17
aumento2 = 0.13
aumento3 = 0.12
aumento4 = 0.10
aumento5 = 0.05

if salario <= 600.00:
    novo_salario = salario+(salario*aumento1)
    print("Novo salario: {:.2f} ".format(novo_salario) + "\nReajuste ganho: {:.2f} ".format(novo_salario-salario) + "\nEm percentual: {:.0f} % ".format(aumento1*100))
    #print("Reajuste de: {:.2f}".format(novo_salario-salario))
    #print("O reajuste em percentual é {:.1f}%".format(aumento1*100))
elif salario <= 900.00:
    novo_salario = salario+(salario*aumento2)
    print("Novo salario: {:.2f} ".format(novo_salario) + "\nReajuste ganho: {:.2f} ".format(novo_salario-salario) + "\nEm percentual: {:.0f} % ".format(aumento2*100))
    #print("Reajuste de: {:.2f}".format(novo_salario-salario))
    #print("O reajuste em percentual é {:.1f}%".format(aumento2*100))
elif salario <= 1500.00:
    novo_salario = salario+(salario*aumento3)
    print("Novo salario: {:.2f} ".format(novo_salario) + "\nReajuste ganho: {:.2f} ".format(novo_salario-salario) + "\nEm percentual: {:.0f} % ".format(aumento3*100))
    #print("Reajuste de: {:.2f}".format(novo_salario-salario))
    #print("O reajuste em percentual é {:.1f}%".format(aumento3*100))
elif salario <= 2000.00:
    novo_salario = salario+(salario*aumento4)
    print("Novo salario: {:.2f} ".format(novo_salario) + "\nReajuste ganho: {:.2f} ".format(novo_salario-salario) + "\nEm percentual: {:.0f} % ".format(aumento4*100))
    #print("Reajuste de: {:.2f}".format(novo_salario-salario))
    #print("O reajuste em percentual é {:.1f}%".format(aumento4*100))
else:
    novo_salario = salario+(salario*aumento5)
    print("Novo salario: {:.2f} ".format(novo_salario) + "\nReajuste ganho: {:.2f} ".format(novo_salario-salario) + "\nEm percentual: {:.0f} % ".format(aumento5*100))
    #print("Reajuste de: {:.2f}".format(novo_salario-salario))
    #print("O reajuste em percentual é {:.1f}%".format(aumento5*100))
