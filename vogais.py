#exercício 05

def contaVogais():
    vogais = 'aeiou'
    frase = input('Digite uma frase: ')
    qtd_vogais = 0
    for c in frase.lower():
        if c in vogais:
            qtd_vogais += 1
    print(f'A frase possui {qtd_vogais} vogais')

contaVogais()
