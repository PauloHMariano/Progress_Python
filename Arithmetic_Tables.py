import sys, time
x1 = int(input('Por favor insira um número para calcular a sua tabuada: '))
tabuada_range = range(0, 11)

for n in tabuada_range:
    resultado = n * x1
    sys.stdout.write('\r{} x {} = {}'.format(x1, n, resultado))
    time.sleep(2)
