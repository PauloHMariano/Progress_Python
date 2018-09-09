tot18 = totH = totM20 = 0
while True:
    print("-------INPUT FORM-------")
    try:
        x2 = int(input("Please insert your age: "))
        if x2 <= 0 or x2 == "":
            print("Please insert a correct value")
            continue
    except ValueError:
        print("Insert a correct value")
        continue
    gender = " "
    while gender not in "MF" or gender == "":
        gender = str(input("What is your gender [M/F]: ").upper())
    if gender == "F" and x2 == 20:
        totM20 += 1
    if gender == "M":
        totH += 1
    if x2 >= 18:
        tot18 += 1
    final = " "
    while final not in "CE" or final == "":
        final = str(input("Would you like to continue or exit [C/E].").upper())
    if final == "E":
        break

print(f'The total of input(s) which is/are 18 or older is {tot18}')
print(f'The total of man/men who was/were input is {totH}')
print(f'The total of woman/women who is/are 20 years old is {totM20}')


