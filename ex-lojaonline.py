from time import sleep
print('---' * 10)
print('LOJAS ONLINE') #Nome Fictício
print('---' * 10)
gasto = tot1000 = maior = 0
maiscaro = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor do produto: R$'))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('---' * 15)
    gasto += valor
    if valor > 1000:
        tot1000 += 1
    if valor == 1:
        maior = valor
        maiscaro = produto
    else:
        if valor > maior:
            maior = valor
            maiscaro = produto
    if continua == 'N':
        print('Vamos finalizar a sua compra. Aguarde um Momento!')
        sleep(2)
        print('---' * 30)
        break
print(f'O total gasto na compra foi de R${gasto:.2f}!')
print(f'Produtos que custam mais de R$1.000,00: {tot1000}')
print(f'O produto mais caro foi o {maiscaro}, custando um valor de R${maior:.2f}!')
print('---' * 30)
print('Obrigado, volte sempre!!')

