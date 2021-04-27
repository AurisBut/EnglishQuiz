mano_vardas = 'gustyte'

bandymas = input('Nori zaisti? (T/N)- ')
spejimas = input('mama atspek mano varda- ')

while bandymas == 'T':
    if spejimas != mano_vardas:
        print('Neteisingai')
        bandymas = input('Nori zaisti? (T/N)- ')
    else:
        print('atspejai')
        break
    bandymas = input('Nori zaisti? (T/N)- ')
