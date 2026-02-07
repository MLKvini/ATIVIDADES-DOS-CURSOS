import random

alatorio = random.randint(1,10)
chute = int(input('chute um numero: '))

if alatorio == chute:
    print('acertei em cheio')
    print('o numero é ', alatorio)
else:
    print('errou feio')
    print('o numero é :', alatorio) 
