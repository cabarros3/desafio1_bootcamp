#exercicio 04

dinheiroCarteira = int(input("Quanto dinheiro você tem na carteira: "))
print(f'Você tem {dinheiroCarteira} e com essa quantia: ')

def dolarAmericano():
    conv_americano = dinheiroCarteira / 4.91
    print(f'Você pode comprar {conv_americano} dólares americanos')

dolarAmericano()

def pesoArgentino():
    conv_argentino = dinheiroCarteira / 0.02
    print(f'Você pode comprar {conv_argentino} pesos argentinos')

pesoArgentino()

def dolarAutraliano():
    conv_australiano = dinheiroCarteira / 3.18
    print(f'Você pode comprar {conv_australiano} dolares australianos')

dolarAutraliano()

def dolarCanadense():
    conv_canadense = dinheiroCarteira / 3.64
    print(f'Você pode comprar {conv_canadense} dolares canadenses')

dolarCanadense()

def francoSuico():
    conv_suico = dinheiroCarteira / 0.42
    print(f'Você pode comprar {conv_suico} francos suiços')

francoSuico()

def euro():
    conv_euro = dinheiroCarteira / 5.36
    print(f'Você pode comprar {conv_euro} euros')

euro()

def libra():
    conv_libra = dinheiroCarteira / 6.21
    print(f'Você pode comprar {conv_libra} libras esterlinas')

libra()