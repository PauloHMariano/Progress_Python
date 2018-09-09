mylist = list(range(0,51))

def purify(odd):
    even = []
    for n in odd:
        if int(n) % 2 == 0:
            even.append(n)
    return even

print(purify(mylist))