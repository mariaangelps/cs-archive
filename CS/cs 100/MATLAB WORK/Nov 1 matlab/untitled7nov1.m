
syms x y z1 z2 eqns
z1=3*x-2*y -3;
z2=1*x+2*y -11;

eqns=[z1==0,z2==0]
[sol.X, sol.Y]=solve(eqns)