infile = open('cards.dat', 'r')
outfile = open('email.dat', 'w')

for line in infile.readlines():
  if line.find('EMAIL')>0:
    outfile.write(line[line.find(':')+1:])

infile.close()
outfile.close()
