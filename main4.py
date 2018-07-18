#!/usr/bin/python3

def find_sim(seq1, seq2, k):

    # seq1 = GAGCCGT
    # seq2 = GAGGGGT
    # k = 5

    # list() = [], set(), dict() = {}

    set1 = set()
    set2 = set()

    for i in range(len(seq1)-k):
        set1.add(seq1[i:i+k])
    for i in range(len(seq2)-k):
        set2.add(seq2[i:i+k])

    set3 = set1 & set2

    A = len(set1) - len(set3)
    B = len(set3)
    C = len(set2) - len(set3)

    prienik = len(set3)
    zjednotenie = len(set1) + len(set2) - prienik

    return prienik / zjednotenie, A, B, C

f = open('all_7.fasta')
reads = f.readlines()
f.close()

vystup = ''

for i in range(len(reads)):
    # if i % 2 == 0:    <--- the same
    if reads[i][0] == '>':
        s1 = reads[i][1:-1]
    else:
        for j in range(i-1, len(reads)):
            if reads[j][0] == '>':
                s2 = reads[j][1:-1]
            else:
                sim, A, B, C = find_sim(reads[i], reads[j], 1)
                vystup += '{}\t{}\t{}\t{}\t{}\t{}\n'.format(s1, s2, sim, A, B, C)

g = open('random.4sim', 'w')
g.write(vystup)
g.close()