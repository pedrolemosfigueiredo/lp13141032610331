# -*- coding: utf8 -*-
print type(1), type(3.4), type((3+3j)+2)
print type("treta"), type(True and False)
a = '1'
b = "Uma"
print type(a), type(b)
print type([1,2,3,[2,3]]), type((1,2,3))
class Teste:
    pass
print type(Teste)
obj = Teste()
print type(obj)
def func():
    return 3
print type(func)

print type(range(0,10))
print type(xrange(0,10))
print type(a>10 if 10 else 2)
print type(a) == type("string") if "uma string" else "nao sei"

expression = ((3+3j)+2)+3.2

if type(expression) == complex:
    print "True"
else:
    print "False"
