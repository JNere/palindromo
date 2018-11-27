
while True:
    num = int(input('Digite um numero: '))
    val = str(num)
    if num <= 1000000:
        if str(num) == val[::-1]:
            print('O numero {} é PALINDROMO'.format(num))
        else:
            print('O numero {} não é PALINDROMO'.format(num))
    else:
        print('Digite numero menores que 1000000')

    cont = str(input("Deseja continuar (S/N)? ")).upper()
    if cont != 'S':
        break
