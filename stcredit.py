
def bruteforce(cr, nbitem, itemprice):
    for b in range(nbitem):
        for c in range(b+1,nbitem):
            if itemprice[b]+itemprice[c] == cr:
                return[b+1,c+1]



f = open('input.txt', 'r')
ncase = int(f.readline())

for a in range(1,ncase+1):
    cCredit = int(f.readline())
    iItem = int(f.readline())
    pPrice = list(map(int, (str.split(f.readline(),' '))))
    solution = bruteforce(cCredit, iItem, pPrice)
    print('Case #'+str(a)+':', solution[0],solution[1])
f.close()
