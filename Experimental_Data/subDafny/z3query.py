from z3 import *
set_param(proof=True)
_p1=Int('_p1')
_p2=Int('_p2')
Y=Int('Y')
X=Int('X')
r=Int('r')
l=Int('l')
Y1=Int('Y1')
X1=Int('X1')
r1=Int('r1')
l1=Int('l1')
_N1=Const('_N1',IntSort())
r5=Function('r5',IntSort(),IntSort())
l5=Function('l5',IntSort(),IntSort())
_N2=Const('_N2',IntSort())
_n2=Int('_n2')
_n1=Int('_n1')
_s=Solver()
_s.set("timeout",60000)
_s.add(Y1 == Y)
_s.add(X1 == X)
_s.add(r1 == If(Y < 0,X + _N1,r5(_N2)))
_s.add(l1 == If(Y < 0,Y + _N1,l5(_N2)))
_s.add((Y + _N1==0))
_s.add(ForAll([_n1],Implies(And((_n1<_N1),_n1>=0),(Y + _n1!=0))))
_s.add(Or(_N1==0,(Y + _N1 - 1!=0)))
_s.add(ForAll([_n2],Implies(_n2>=0,r5(_n2 + 1) == r5(_n2) - 1)))
_s.add(ForAll([_n2],Implies(_n2>=0,l5(_n2 + 1) == l5(_n2) - 1)))
_s.add(r5(0) == X)
_s.add(l5(0) == Y)
_s.add((l5(_N2)==0))
_s.add(ForAll([_n2],Implies(And((_n2<_N2),_n2>=0),(l5(_n2)!=0))))
_s.add(Or(_N2==0,(l5(_N2 - 1)!=0)))
_s.add(_N1>=0)
_s.add(_N2>=0)
_s.add(X>=0)
_s.add(Y>=0)
_s.add(Not(r1==X - Y))
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