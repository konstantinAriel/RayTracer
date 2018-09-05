function Mirror = SetMir (L, V, angel_degre, O,  dTline, S1,S2)
%% Surf [mm]
[M] =  Rotation (angel_degre);
F = L/2;
S = struct('X',S1(1,1),  'Y',S1(1,2),'Z',S1(1,3));
R = struct('X',S2(1,1),  'Y',S2(1,2),'Z',S2(1,3));
Fx = F;
Fz = F;
%% Shift
dx =V.X;
dy = V.Y;
dz = V.Z;
dXYZ = [dx 0 0; 0 dy 0; 0 0 dz];
%% Focus
dXYZ = dXYZ*[1; 1; 1];
Fvector  =  dXYZ + [F 0 0; 0 F 0; 0 0 F]*M(:,3);
f = struct('X',Fvector(1,1), 'Y',Fvector(2,1), 'Z',Fvector(3,1));

%%
 dxdy = 10;


a11 =  1/(4*F);
a22 =  1/(4*F);
%a11 = 1/1000000;
%a22 = 1/1000000;
a33 = 0;
a12 = 0;
a13 = 0;
a23 = 0;
a3 = [1 1 1]*M(:,3);
AA = [a11 a12 a13; a12 a22 a23; a13 a23 a33 ];

X = [1 2 3];
XSym = ['X'; 'Y';  'Z'];
X=int8(abs([1 2 3]*M));
i1 = X(1,1);
i2 = X(1,2);
i3 = X(1,3);

A = XSym(i1,1);
B = XSym(i2,1);
C = XSym(i3,1);
dx1 = dXYZ(i1,1);
dx2 = dXYZ(i2,1);
dx3 = dXYZ(i3,1);
O1x1 =O(1, i1);
O1x2 = O(1,i2);
absX = X<0; 
k=1;
 x1 = (-dTline/2+O1x1)*k : dxdy*5 : (dTline/2+O1x1)*k;
 x2 =(O1x2 - dTline/2)*k  : dxdy*5 :(O1x2 + dTline/2)*k ;
 %x1 = -1000:dxdy*k:1000;
 %x2 = -600: dxdy*k:1400;
[X1 ,X2] = meshgrid (x1, x2); 
X3 =  (a11*(X1 - dx1).^2 + a22*(X2 - dx2).^2 )/a3 +dx3;


 %% Build Mirror				
Mirror = struct ('a11', a11, 'a22', a22, 'a3', a3,'f', f, A, X1, B, X2, C, X3, 'S',S,  'R', R, 'V', V, 'I', [i1 i2 i3]);

end
