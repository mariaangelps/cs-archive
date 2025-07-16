%Circuit 1

V1=0;
V2= 5;
V3= 12;
V4= 15;
V5=18;


I1=0;
I2=0.0049;
I3=0.0119;
I4=0.0149;
I5=0.0179;


R1= V1/I1;
R2= V2/I2;
R3= V3/I3;
R4= V4/I4;
R5= V5/I5;

VV=[V1,V2,V3,V4,V5]
II=[I1,I2,I3,I4,I5]
 
figure(1)
scatter(II,VV)

%Circuit 2

Vs1=0;
Vs2=5;
Vs3=7;
Vs4=9;

AddVolt= 6;

Is= 0.00601;
Is1= 0.1104;
Is2= 0.01302;
Is3= 0.1503;

Rs1=(AddVolt+Vs1)/Is;
Rs2=(AddVolt+Vs2)/Is1;
Rs3=(AddVolt+Vs3)/Is2;
Rs4=(AddVolt+Vs4)/Is3;

VVs=[Vs1, Vs2, Vs3, Vs4];
IIs=[Is, Is1, Is2, Is3];
figure(2)
scatter(IIs, VVs)