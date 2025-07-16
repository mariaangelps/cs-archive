%Circuit 1
V5= 5;
V12= 12;
V15= 15;
V18= 18;
I5=18.2;
I12=50;
I15= 60;
I18=80.6;

R5=V5/I5;
R12=V12/I12;
R15=V15/I12;
R18=V18/I18;

VV=[V5,V12, V15,V18];
II=[I5,I12,I15,I18];


figure(1)
scatter(II,VV)
xlabel ('I')
ylabel ('V')

% Circuit 2
Vs5= 5;
Vs7= 7;
Vs9= 9;

AddV= 5.88;

Is5= 16.7;
Is7= 19.2;
Is9= 23.7;

Rs5= Vs5+AddV/Is5;
Rs7= Vs7+AddV/Is7;
Rs9= Vs9+AddV/Is9;

VVs=[Vs5,Vs7,Vs9];
IIs=[Is5,Is7,Is9];
figure(2)
scatter(IIs,VVs)

%Circuit 3
Volt=7;
Volt2=9;
Volt3=11;
V7=(1.11);
V9=(1.43);
V11=(1.75);

I7= 5.6;
I9= 7.2;
I11= 8.8;

P1= V7*I7/1000;
P2= V9*I9/1000;
P3= V11*I11/1000;



V3=[Volt, Volt2, Volt3];
II3=[I7, I9, I11];
Pt= [P1, P2, P3];



figure(3)
scatter(II3,V3,Pt)
