'''
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
R- Eu ligo o interruptor 1 e espero 5 minutos, desligo o mesmo e ligo o interruptor 2. Vou até a sala 1 e faço as seguintes condições:
1ª: if lampada == desligada and lampada == quente:
        interruptor1: sala1
    elif lampada == ligada:
        interruptor2: sala1
    else:
        interruptor3: sala1

Volto até os interruptores. Desligo o 2° interruptor, ligo o 3° interruptor, vou até a sala 2 e faço a 2ª condicional:
2ª: if lampada == on:
        interruptor3: sala2
    else:
        interruptor3: sala3

A lampada da 1ª sala foi identificada na primeira ida, e o interruptor da 2ª sala foi identificada na segunda ida, então o interruptor que sobrar é da última sala.
'''
