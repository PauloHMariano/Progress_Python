import numpy as np
nota1 = float(input('Nota 1 '))
nota2 = float(input('Nota 2 '))
getit = [nota1, nota2]
media = np.mean(getit)

if media < 5.0:
    print('Você está reprovado. Sua nota é {}.'.format(media))
elif (media >= 5.0) and (media <=6.9):
    print('Recuperação. Sua nota é {}.'.format(media))
else:
    print('Aprovado, sua nota é {}.'.format(media))






