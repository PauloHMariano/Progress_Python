import numpy as np
nota1 = float(input('Input Grade 1 '))
nota2 = float(input('Input Grade 2 '))
getit = [nota1, nota2]
media = np.mean(getit)

if media < 5.0:
    print('Your not approved. Your grade is {}.'.format(media))
elif (media >= 5.0) and (media <=6.9):
    print('Retake test needed. Your grade is {}.'.format(media))
else:
    print('Approved, your grade is {}.'.format(media))






