%Maria Palacios 

%Table 2.3

x1= 30.47;
x2= 45;
x3= 90;
x4= -45;
x5= 0;
x6= 45;

y1=sind(x1); y2=cosd(x1); y3=tand(x1); y4=secd(x1);

y1a= sind(x2); y2a=cosd(x2); y3a=tand(x2); y4a=secd(x2); 

y1b= sind(x3); y2b=cosd(x3); y3b= tand(x3); y4b=secd(x3);

y1c= sind(x4); y2c= cosd(x4); y3c= tand(x4); y4c= secd(x4);

y1d= sind(x5); y2d= cosd(x5); y3d= tand(x5); y4d= secd(x5);

y1e= sind(x6); y2e= cosd(x6); y3e= tand(x6);y4e= secd(x6);

%Table 2.4 

%sin/cos

A= (y1/y2);
A1= (y1a/y2a);
A2= (y1b/y2b);
A3= (y1c/y2c);
A4= (y1d/y2d);
A5= (y1e/y2e);

%sin^2+cos^2
B= y1^2+y2^2;
B1= y1a^2+y2a^2;
B2= y1b^2+y2b^2;
B3= y1c^2+y2c^2;
B4= y1d^2+y2d^2;
B5= y1e^2+y2e^2;

%1+tan^2

C= 1+(y3)^2;
C1= 1+(y3a)^2;
C2= 1+(y3b)^2;
C3= 1+(y3c)^2;
C4= 1+(y3d)^2;
C5= 1+(y3e)^2;

%sec^2

D= (y4)^2;
D1=(y4a)^2;
D2=(y4b)^2;
D3=(y4c)^2;
D4= (y4d)^2;
D5= (y4e)^2;


% Two link robot

%Table 2.5

l1= 50;
l2=50;
a= 0;
b=0;
c=0;
d=90;
e=30;
f=45;
g= 30;
h=60;
i=180;
j=0;
k=270;
l=30;
m=360;
n=90; 


a1=l1* cosd(a);
a2=l1* sind(a);
a3= l2* cosd(a + b);
a4= l2* sind (a +b);

c1= l1*cosd(c);
c2= l1*sind(c);
c3= l2*cosd(c+d);
c4= l2*sind(c+d);

e1= l1*cosd (e);
e2= l1*sind (e);
e3= l2*cosd (e+f);
e4= l2*sind (e+f);

g1= l1*cosd (g);
g2= l1*sind (g);
g3= l2*cosd (g+h);
g4= l2*sind (g+h);

i1= l1*cosd (i);
i2= l1*sind (i);
i3= l2*cosd (i+j);
i4= l2*sind (i+j);

k1= l1*cosd (k);
k2= l1*sind (k);
k3= l2*cosd (k+l);
k4= l2*sind (k+l);

m1= l1*cosd (m);
m2= l1*sind (m);
m3= l2*cosd (m+n);
m4= l2*sind (m+n);


Xa= a1+a3;
Xc= c1+c3;
Xe= e1+e3;
Xg= g1+g3;
Xi= i1+i3;
Xk= k1+k3;
Xm= m1+m3;

Ya= a2+a4;
Yc= c2+c4;
Ye= e2+e4;
Yg= g2+g4;
Yi= i2+i4;
Yk= k2+k4;
Ym= m2+m4;

%Table 2.6 Sine and Cosine Law

Px1= 55;
Px2= 75;
Px3= 15;
Px4= 32;
Px5= 71;
Py1= 75;
Py2= 60;
Py3= 63;
Py4= 14;
Py5= 70;

% P(55,75)
R= sqrt((Px1)^2+ (Py1)^2);
Z= atand (Py1/Px1);
Be= ((l1)^2 +(l2)^2 - (R)^2 )/ ((2)*l1*l2);
betha= acosd(Be); 

Angle2= 180-betha;

Al= ((l2)/(R)) * sind(betha);

Alpha= asind(Al);

Angle1= Z-(Alpha); 

% P(75,60)

R1= sqrt((Px2)^2+ (Py2)^2);
Z1= atand (Py2/Px2);
Be1= ((l1)^2 +(l2)^2 - (R1)^2 )/ ((2)*l1*l2);
betha1= acosd(Be1); 

P2Angle2= 180-betha1;

Al1= ((l2)/(R1)) * sind(betha1);

Alpha1= asind(Al1);

P2Angle1= Z1-(Alpha1); 


%P(15,63)
R2= sqrt((Px3)^2+ (Py3)^2);
Z2= atand (Py3/Px3);
Be2= ((l1)^2 +(l2)^2 - (R2)^2 )/ ((2)*l1*l2);
betha2= acosd(Be2); 

P3Angle2= 180-betha2;

Al2= ((l2)/(R2)) * sind(betha2);

Alpha2= asind(Al2);

P3Angle1= Z2-(Alpha2); 


%P(32,14)
R3= sqrt((Px4)^2+ (Py4)^2);
Z3= atand (Py4/Px4);
Be3= ((l1)^2 +(l2)^2 - (R3)^2 )/ ((2)*l1*l2);
betha3= acosd(Be3); 

P4Angle2= 180-betha3;

Al3= ((l2)/(R3)) * sind(betha3);

Alpha3= asind(Al3);

P4Angle1= Z3-(Alpha3); 


%P(71,70)

R4= sqrt((Px5)^2+ (Py5)^2);
Z4= atand (Py5/Px5);
Be4= ((l1)^2 +(l2)^2 - (R4)^2 )/ ((2)*l1*l2);
betha4= acosd(Be4); 

P5Angle2= 180-betha4;

Al4= ((l2)/(R4)) * sind(betha4);

Alpha4= asind(Al4);

P5Angle1= Z4-(Alpha4); 
