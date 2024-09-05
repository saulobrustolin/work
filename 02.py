a = str(input('Digite o texto: '))
b = str(input('Digite a letra que deseja encontrar e contar: '))

def exec(a, b):
    if a.find(b) != -1 or a.find(b.upper()):
        x = a.count(b) + a.count(b.upper())
        return x
    return
if a:
    c = exec(a, b)
    if c:
        print(f'A letra \'{b}\' foi encontrada {c} vezes.')
    else:
        print(f'Essa letra não foi encontrada no texto. ;/')
