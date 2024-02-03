#exercicio 3

pergunta = input("Escolha o método de conversão: \n(F) Fahrenheit para Celcius \n(C) Celcius para Fahrenheit \n A sua escolha é:  ")

if pergunta == "F":
    temperaturaC = float(input("Digite a temperatura atual em Celcius: "))

    def converteF():
        f = (temperaturaC * 1.8) + 32
        print(f'A temperatura em Fahrenheit é {f}')

    converteF()
else:
    temperaturaF = float(input("Digite a temperatura em Fahrenheit: "))

    def converteC():
        c = (temperaturaF - 32) / 1.8
        print(f'A temperatura em Celcius é {c}')

    converteC()