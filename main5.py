n = 7
abeceda = ['A', 'C', 'T', 'G']


def gen_seq(n, abeceda, i, seq, file):

    if len(seq) == n:
        file.write('>seq{}\n{}\n'.format(i, seq))
        i += 1
        return i
    else:
        for letter in abeceda:
            i = gen_seq(n, abeceda, i, '{}{}'.format(seq, letter), file)
        return i

f = open('all.fasta', 'w')
gen_seq(n, abeceda, 1, '', f)
f.close()