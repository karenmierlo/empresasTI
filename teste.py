total = 5000
passo = 867
saldo = total

x, inicio, fim = 0, 0, 0
lista = []

while saldo > 0:   

    fim = fim+passo
    print(f'saldo: {saldo}')

    if saldo < passo:
        fim = inicio + (saldo-1)
        # lista.append((inicio, inicio+saldo))
    else:
        fim = inicio + (passo -1)
        # lista.append((inicio, fim))        

    lista.append((inicio,fim))

    saldo = saldo-passo
    # inicio = inicio + passo +1
    inicio = fim + 1 

for x, y in lista:
    print(x, y)
