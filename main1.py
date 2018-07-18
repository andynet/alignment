import random

n = int(input('Zadaj pocet sekvencii: '))
m = int(input('Zadaj dlzku sekvencii: '))
text = ''

for i in range(n):
    text += '>seq{}\n'.format(i)
    for j in range(m):
        text += random.choice(['A', 'T', 'C', 'G'])
    text += '\n'

f = open('random.fasta', 'w')
f.write(text)
f.close()