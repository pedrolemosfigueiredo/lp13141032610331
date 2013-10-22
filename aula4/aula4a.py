# -*- coding: utf-8 -*-
# autor: Pedro Figueiredo
# data: 30 de Setembro de 2013
# Entrada e saída de dados

import math

print"\n----------strop----------"
#strop.py
s = "mas que belo dia"
x = 'q'
if x in s:
    print "a letra 'q' encontra-se em s"
    t = " em Amsterdão"
    pass
print s+t
print 3 * t
print s[5], s[5:8], s[5:12:2]
print len(t), len(s)
print min(s), max(t)
print "indique de 'q' =", s.index('q')
print "vezes em que aparece 'm' = ", t.count('m')
#strop.py

print "\n----------strop2----------"
#strop2.py
s1 = "anda um espectro pela Europa"
i = s1.find('ctro',3,20)
print s1[i:i+5]
print s1.strip('a')
t = s1.partition(' ')
print t
l= """
Alma minha gentil, que te partiste

Alma minha gentil, que te partiste
Tao cedo desta vida, descontente,
Repousa la no Ceu eternamente
E viva eu ca na terra sempre triste.
""".splitlines()
print l
#strop2.py

print "\n----------formatar----------"
#formatar.py
x = 23.4
s1 = "raiz quadrada"
y = 255
s2 = "Temos {:^40} de x = {valor:2.4f} ".format(s1,valor =x)
s2 += "e y = 0x{yy:X}".format(yy=y)
s2 += "\nA percentagem = {0:2.1%}".format(34/100.0)
print s2
#formatar.py

print "\n----------ficheiro----------"
#ficheiro.py
f = open("teste.txt", "w")
s = "treta"
for k in range(10): f.write(s); f.write("\n")
f.close()
f = open("teste.txt", "r")
f.seek(5)
print f.tell()
x = f.read(10)
print x
c = 0
for line in f:
    print "{0}: ".format(c), line
    c+=1
    pass
f.close()
with open("teste.txt", "r") as f:
    x = f.readline()
    if x == 'treta\n':
        print "voila"
#ficheiro.py

print "\n----------serialização----------"
#seria.py
import pickle
class Teste:
    def __init__(self,x):
        self.x = x
        pass
    pass
obj = Teste(49)
f = open("teste.dat", "w")
p = pickle .dump(obj,f)
f.close()
del obj
obj = pickle.load(open("teste.dat","r"))
print obj.x
#seria.py

print "----------importar e exportar csv----------"
#lercsv.py
import csv

with open('listacompras.csv','rb') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print ", ".join(linha)
        pass
    pass
with open('notas.csv', 'wb') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['Programacao 1', 14])
    escritor.writerow(['Programacao 2', 15])
    escritor.writerow(['Linguagens de Programacao', 19])
    pass
#lercsv.py

print "----------suporte sqlite3--------"
#bd1.py
import sqlite3

conexao = sqlite3.connect('teste.db')
c = conexao.cursor()
c.execute('DROP TABLE IF EXISTS disc')
c.execute('CREATE TABLE disc (nome text, nota number)')
conexao.commit()
notas = [('P1', 15), ('P2', 15), ('LP', 19)]
c.executemany('INSERT INTO disc VALUES (?,?)', notas)
conexao.commit()
c.execute("SELECT * FROM disc WHERE nota > 16")
print "uma...", c.fetchone()
k = 0; soma = 0.0
for linha in c.execute("SELECT * FROM disc"):
    print linha; soma += linha[1]; k += 1
    pass
print "media = {:2.2f}".format(soma/k)
conexao.close()
#bd1.py

print "----------Tratamento de exceções----------"
#exce.py
import sys
try:
    f = open('ficha.text')
    s = f.readline()
    i = int(s.strip())
    pass
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    pass
except ValueError:
    print "Could not convert data to an integer."
    pass
except:
    print "Unexpected error:", sys.exec_info()[0]
    raise
#exce.py
