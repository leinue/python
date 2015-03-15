def odd():
    funcs=[]
    for c in 'abdefg':
        funcs.append((lambda c=c:c))
    return funcs

for func in odd():
    print(func(),end=' ')
