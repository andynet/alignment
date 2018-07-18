def get_options(kmer, d):

    n = 4 ** kmer
    s = set()

    # print((n + 3) * (n + 2) * (n + 1) / 6)
    max_size = 2*d - 2 * kmer + 2

    for i in range(0, n + 3):
        for j in range(i + 1, n + 3):
            for k in range(j + 1, n + 3):
                string = '1' * (n + 3)
                string = string[0:i] + '0' + string[i + 1:j] + '0' + string[j + 1:k] + '0' + string[k + 1:n + 3]
                pole = string.split('0')

                A, B, C, D = len(pole[0]), len(pole[1]), len(pole[2]), len(pole[3])

                if 0 < A + B <= d - kmer + 1 and 0 < B + C <= d - kmer + 1 and A + B + C > 0:
                    perc = B / (A + B + C)
                    s.add(perc)

                    print('A = {}\tB = {}\tC = {}\tD = {}\t Perc = {}'.format(A, B, C, D, perc))

                if k > max_size + 2:
                    break
            if j > max_size + 1:
                break
        if i > max_size:
            break

    # results:
    # minimal length of sequences with maximal degrees of distinguishing = 4**kmer + kmer - 1

    return len(s)

f = open('')
for i in range(1, 401):
    for j in range(1, min([i,21])):

        density = get_options(j, i)
        i, j,