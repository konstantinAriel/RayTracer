function [Ray, Normal, RefRay]  = RaysData (M,  Ray0)

L =1000;

i1 = M.I(1,1);
i2 = M.I(1,2);
i3 = M.I(1,3);
 x10 = Ray0.dX(1,1);
 x20 = Ray0.dX(1,2);
 x30 = Ray0.dX(1,3);
 X0 = [x10 x20 x30];

kX = Ray0.K(1,1);
kY = Ray0.K(1,2);
kZ = Ray0.K(1,3);

 absK = sqrt(Ray0.K*Ray0.K');
 k1 = kX/absK;
 k2 = kY/absK;
 k3 = kZ/absK;
 K = [k1 k2 k3];
% absK1 = sqrt(kX^2+kY^2+kZ^2)

dx1 = M.V.X;
dx2 = M.V.Y;
dx3 = M.V.Z;
dX = [dx1 dx2 dx3];

a11 = M.a11;
a22 = M.a22;
a3 = M.a3;

%aMir = (Cxx*kX^2 + 2*Cxz*kX*kZ + Czz*kZ^2);
%bMir = 2*Cxx*kX*x0 + Cz*kZ - Cy*kY - Cx*kX + 2*Cxz*kZ*x0 + 2*Cxz*kX*z0 + 2*Czz*kZ*z0;
%cMir = Cy*dy - Cy*y0 + Cx*x0 + Cz*z0 + Cxx*x0^2 + Czz*z0^2 + 2*Cxz*x0*z0;
K1 = K(1,i1);
K2 = K(1, i2);
K3 = K(1,i3);
 A = a11*K(1,i1)^2 +  a22*K(1,i2)^2;
 B = 2*a11*K(1,i1)*(X0(1,i1)-dX(1,i1)) - a3*K(1,i3)+ 2*a22*K(1,i2)*(X0(1,i2)-dX(1,i2));
 C = -a3*(X0(1,i3)-dX(1,i3)) +a11*(X0(1,i1)-dX(1,i1))^2 + a22*(X0(1,i2)-dX(1,i2))^2;
 
%CoeffMir = [ - Cxx*kX^2 - Czz*(cos(a_Rad)*kZ + kY*sin(a_Rad))^2 - 2*Cxz*kX*(cos(a_Rad)*kZ + kY*sin(a_Rad)),... 
%				2*Cxy*(dx - x0)*(cos(a_Rad)*kY + kZ*sin(a_Rad)) - Cy*(cos(a_Rad)*kY + kZ*sin(a_Rad)) - Cz*(cos(a_Rad)*kZ - kY*sin(a_Rad)) - Cx*kX - 2*Cyy*(cos(a_Rad)*kY + kZ*sin(a_Rad))*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0) + 2*Cxx*kX*(dx - x0) - 2*Cxy*kX*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0),...
%				Cx*(dx - x0) - Cy*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0) - Cxx*(dx - x0)^2 - Cyy*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0)^2 + Cz*(dz - cos(a_Rad)*z0 + sin(a_Rad)*y0) + 2*Cxy*(dx - x0)*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0)];
 
p = [A B C];     % aMir*x^2 + bMir*x  + cMir = 0
t = roots(p);              
[tX, ~] = size(t);

%    p1 = (-B+sqrt((B^2)-(4*A*C)))/(2*A);
%    p2 = (-B-sqrt((B^2)-(4*A*C)))/(2*A);
%    p = [p1 p2]
 

%  minP = min(abs(p))
%  X1 = (X0' + minP.*K')'

 if tX == 1
% % x1 = x0 + D*kX*t(1,1);
% % y1 = y0 + D*kY*t(1,1)
% % z1 = z0 + D*kZ*t(1,1)
% 
 X1 = (X0' + t.*K')';
% % Xcross = [x1 y1 z1];
 elseif tX == 2
C =t>0;
x  = [C(1,1) 0; 0 C(2,1)];
A = t'*x;
y  = find(A);
P = min(A(1, find(A)));
X1 = (X0' + P.*K')';
% % % x1 = x0 + kX*t(t1);
% % % y1 = y0 + kY*t(t1);
% % % z1 = z0 + kZ*t(t1);
% 
% % x1 =  X0(1,1) + kX*t(2,1);
% % y1 =  X0(1,1) + kY*t(2,1);
% % z1 =  X0(1,1) + kZ*t(2,1);
% t= abs(t(2,1));
% X1 = (X0' + t.*K')';
% % Xcross = [x1 y1 z1];
 end
 
% b = a11*(z2 - dz)^2+a22*(x2 - dx)^2;
% d = - a3*(y2 - dy);
% a= b+d;
% if a > 0.0001 || a < (-0.001)
% disp('Error');
% end
% end
%chekMirror =  ((Cxx*(x1 - dx)^2 + 2*Cxz*(x1 - dx)*(z1 - dz) + Czz*(z1 - dz)^2 + Cx*(x1 - dx) + Cz*(z1 - dz))) - Cy*(y1 - dy)

Ray = struct ('X0', X0(1,1), 'Y0', X0(1,2),'Z0', X0(1,3),...
             'X', X1(1,1), 'Y', X1(1,2), 'Z', X1(1,3),...
             'kX', K(1,1), 'kY', K(1,2), 'kZ', K(1,3));
%%  Normal
N1 = (2*a11*(X1(1,i1)-dX(1,i1)) );
N2 = (2*a22*(X1(1,i2)-dX(1,i2)) );
N3 = - a3;

absNormal =sqrt( [N1 N2 N3] * [N1 N2 N3]');
N1 = N1/absNormal;
N2 = N2/absNormal;
N3 = N3/absNormal;
N = [N1 N2 N3];
%Nx =  (2*Cxx*(x1-dx) + 2*Cxy*x1*(cos(a_Rad) + sin(a_Rad) - dy) + Cx*x1);
%Ny =  (2*Cxy*(x1-dx)*cos(a_Rad) + 2*Cyy*(cos(a_Rad)*y1+sin(a_Rad)*z1-dy)*cos(a_Rad) + Cy*cos(a_Rad) - Cz*sin(a_Rad));
%Nz =  -(2*Cxy*(x1-dx)*sin(a_Rad) + 2*Cyy*(cos(a_Rad)*y1 + sin(a_Rad)*z1 - dy)*sin(a_Rad) + Cy*sin(a_Rad) - Cz*cos(a_Rad));

%xN =  x1 - 100;
%yN = (Ny/Nx)*(xN - x1) + y1;
%zN = (Nz/Nx)*(xN - x1) + z1;

xN1 = X1(1,1) -N(1, i1)*L;
xN2 = X1(1,2) - N(1,i2)*L;
xN3 = X1(1,3) - N(1,i3)*L;
xN = [xN1 xN2 xN3];
Normal   = struct('X0', X1(1,1), 'Y0', X1(1,2), 'Z0', X1(1,3),...
                  'X',xN(1,1),  'Y', xN(1,2),  'Z', xN(1,3),...
		 	         'kX', N1,  'kY', N2,  'kZ', N3);
%%  Reflected
n = [N(1,i1)  N(1,i2)  N(1,i3)];
k = [K(1,1) K(1,2)  K(1,3)];
c1 = Rotor (n , k);
c2 = Rotor(c1, n);
  
N11  =(k*n')*n;
absN = sqrt(n*n');
kref=(c2-N11)/absN;

RefX = kref(1);
RefY = kref(2);
RefZ = kref(3);
Kref = [RefX  RefY  RefZ];
absRefK = sqrt(kref*kref');
RefX = kref(1)/absRefK;
RefY = kref(2)/absRefK;
RefZ = kref(3)/absRefK;
%absRefK2 = sqrt(RefX^2+RefY^2+RefZ^2);
 MaxKref = max(abs(Kref));
 RefTemp = (abs(Kref) == max(abs(Kref)));
 RefIndex = find(RefTemp);
 Rx1 = Kref*RefTemp';
mR  = [M.R.X  M.R.Y  M.R.Z];
tRef = (mR(1,RefIndex) - X1(1, RefIndex))/Rx1;

Xr = X1' + tRef.*Kref';
Xr(RefIndex,1) = mR(1 , RefIndex);

% % if  abs(RefY) < abs(RefZ)
% % zRef = M.R.Z;
% % tRef = (zRef - z1)/RefZ;
% % xRef = x1 + RefX*tRef;
% % yRef = y1 + RefY*tRef;
% % elseif abs(RefZ) < abs(RefY)
% % yRef = M.R.Y;
% % tRef = (yRef - D*y1)/RefY;
% % xRef = x1 + RefX*tRef;
% % zRef = z1 + RefZ*tRef;
% % end

RefRay = struct('X0', X1(1,1), 'Y0', X1(1,2), 'Z0', X1(1,3),...
					 'X',Xr(1,1), 'Y', Xr(2,1), 'Z',Xr(3,1),...
					 'kX', RefX, 'kY', RefY, 'kZ', RefZ);

end

