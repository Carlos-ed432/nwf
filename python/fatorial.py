def fatorial(a=0,metd=False):
    f = 1  # recebe o valor da fatorial
    for v in range(a,0,-1): # conta o número digitado para trás e somando
        f*=v
    if metd==True:
        print(a,end='')
        for va in range(a,0,-1):
            print(f" x {va}",end='')
    if metd==False:
        print(end=' ')
    else:
        print(end=' = ')
    return f
    
print(fatorial (7,metd=True))