f = open('random.fasta')
read = f.readlines()
vystup = ''

for riadok in read:
    if riadok[0] == '>':
        vystup += riadok
    else:
        cg = 0
        for j in range(len(riadok)):
            if riadok[j] == 'C' or riadok[j] == 'G':
                cg += 1
        cg_content = cg / len(riadok)
        vystup += 'CG_content = {} \n'.format(cg_content)

g = open('random.stats', 'w')
g.write(vystup)
g.close()