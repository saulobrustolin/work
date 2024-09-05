a = int(input('Digite o n°: '))

def exec(a):
    y = [0, 1]

    i = 0
    while i < a:
        z = y[i + 1] + y[i]
        y.append(z)
        if z < a:
            i += 1
            continue
        break
    return y
    
if a:
    if a in exec(a):
        print('Esse número pertence a Fibonacci.')
    else:
        print('Esse número NÃO pertence a Fibonacci.')
