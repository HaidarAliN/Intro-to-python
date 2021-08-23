#List Jumps:
def list_jumps(jumps):
    i = 0
    lst = [0]
    while(True):
        i = i + jumps[i]
        if i in lst:
            return 'cycle'
        lst.append(i)
        if i >= len(jumps) or i<0:
            return 'out-of-bounds'

#Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    primelist = list(range(2,n+1))
    for i in range(0,n//2):
        for j in range(i+2,n//2+1):
            if i < len(primelist) and j*primelist[i] in primelist:
                primelist.remove(j*primelist[i])
    return primelist


