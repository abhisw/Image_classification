inp = open('tmp.txt', 'r')
out = open('pos_two.txt','w')

for line in inp:
    out.write('pos_two/'+line)
inp.close()
out.close()