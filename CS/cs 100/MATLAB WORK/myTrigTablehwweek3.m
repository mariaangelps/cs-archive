%myTrigTable

% 1. Create a table of all the 3 trig functions for angles from 0 to 2pi,
% with a spacing(:) of 0.1 radians.

x=0: 0.1: 2*pi;

s=sin(x);
c=cos(x);
t=tan(x);
disp('angle(radians) sine cosine tangent');
Table= [x', s', c' t']

%2.Create the following matrices:

a=[15,3,22 ; 3,8,5; 14,3,82]

b=[1;5;6]

c=[12,18,5,2]

%(a)Create a matrix called d from the third column of matrix a

d= [22;5;82]
%(b)Combine matrix b and matrix d to create matrix e, a two-dimensional
%matrix with three rows and two columns.

e= [b,d]

%(c) Combine matrix b and matrix d to create matrix f, a one-dimensional
%matrix with six rows and one column.

f=[b;d]

%(D) Create a matrix g from a and the first three elements of matrix c,
%with four rows and three columns.

j=c(1:4) % from row 1 to column 4

g=[a;c(1:3)] % g= [ matrix of a; extract of the first row to the third column


%(E) Create a matrix h with the first element equal to a13, the second
%element equal to c12 and the third element equal to b21.

a13= a(1,3) % extract element matrix a from row 1, column 3 

c12= c(1,2) % extract element matrix c from row 1, column 2 

b21= b(2,1) %extract element matrix b, from row 2, column 1 

h= [a13,b21,c12]





