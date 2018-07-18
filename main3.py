f = open('random.fasta')
reads = f.readlines()
f.close()

vystup = ''

for riadok in reads:
    if riadok[0] == '>':
        vystup += riadok
    else:
        for j in range(len(riadok)-3):
            if riadok[j:j+3] == 'ATG':
                for k in range(j, len(riadok)-3, 3):
                    if riadok[k:k+3] in ['TGA', 'TGG', 'TAG']:
                        code_seq = riadok[j:k+3]
                        vystup += 'code seq: = {} \n'.format(code_seq)
                        break

g = open('random.code_seq', 'w')
g.write(vystup)
g.close()