import sys, time
x1 = int(input('Please inset a number to calculate its arithmetic table: '))
tabuada_range = range(0, 11)

for n in tabuada_range:
    resultado = n * x1
    sys.stdout.write('\r{} x {} = {}'.format(x1, n, resultado))
    time.sleep(2)
