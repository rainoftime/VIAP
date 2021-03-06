from z3 import *
set_param(proof=True)
_p1=Int('_p1')
_p2=Int('_p2')
a=Int('a')
c=Int('c')
K=Int('K')
m=Int('m')
l=Int('l')
Z=Int('Z')
a1=Int('a1')
K1=Int('K1')
m1=Int('m1')
l1=Int('l1')
c1=Int('c1')
Z1=Int('Z1')
_N1=Const('_N1',IntSort())
_n1=Int('_n1')
power=Function('power',IntSort(),IntSort(),IntSort())
_s=Solver()
_s.add(ForAll([_p1],Implies(_p1>=0, power(0,_p1)==0)))
_s.add(ForAll([_p1,_p2],Implies(power(_p2,_p1)==0,_p2==0)))
_s.add(ForAll([_p1],Implies(_p1>0, power(_p1,0)==1)))
_s.add(ForAll([_p1,_p2],Implies(power(_p1,_p2)==1,Or(_p1==1,_p2==0))))
_s.add(ForAll([_p1,_p2],Implies(And(_p1>0,_p2>=0), power(_p1,_p2+1)==power(_p1,_p2)*_p1)))
_s.set("timeout",60000)
_s.add(a1 == a)
_s.add(K1 == K)
_s.add(Z1 == Z)
_s.add(c1 == _N1 + 1)
_s.add(m1 == (power(Z,(_N1+1))*a-a)/(Z-1))
_s.add(l1 == power(Z,_N1))
_s.add(_N1 >= K - 1)
_s.add(ForAll([_n1],Implies(And((_n1<_N1),_n1>=0),_n1 + 1 < K)))
_s.add(Or(_N1==0,_N1 < K))
_s.add(_N1>=0)
_s.add(K>0)
_s.add(Z>1)
_s.add(a>0)
_s.add(Not((power(Z,(_N1+1))*a-a)/(Z-1)==(power(Z,K)*a-a)/(Z-1)))
if sat==_s.check():
	print "Counter Example"
	print _s.model()
elif unsat==_s.check():
	_s.check()
	if os.path.isfile('j2llogs.logs'):
		file = open('j2llogs.logs', 'a')
		file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
		file.close()
	else:
		file = open('j2llogs.logs', 'w')
		file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
		file.close()
	print "Successfully Proved"
else:
	print "Failed To Prove"