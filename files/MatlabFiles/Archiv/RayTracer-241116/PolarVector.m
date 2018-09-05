function [Ray, RefRay]  = PolarVector (Ray, Normal, AmplE)

x0 = Ray.X0;
y0 = Ray.Y0;
z0 = Ray.Z0;

xM = Normal.X0;
yM = Normal.Y0;
zM = Normal.Z0;

Nx = Normal.kX;
Ny = Normal.kY;
Nz = Normal.kZ;

kX = Ray.kX;
kY = Ray.kY;
kZ = Ray.kZ;
k = [kX kY kZ];

Ex = kZ;
Ez = -kY;
Ey = -(kX*Ex +kZ*Ez)/kY;
E = [Ex Ey Ez];
absE = sqrt(E*E');
E11 = E./absE;
absE1 = sqrt(E*E');
orhogonal = k*E';

x1 = x0 + Ex*AmplE;
y1 = y0 + Ey*AmplE;
z1 = z0 + Ez*AmplE;

absE2 = sqrt((x1-x0)^2 + (y1-y0)^2 + (z1-z0)^2);

Ray = struct ('X0', x0, 'Y0', y0, 'Z0',z0, 'X', x1, 'Y', y1, 'Z', z1, 'kX', Ex, 'kY', Ey, 'kZ',Ez);

n = [Nx Ny Nz];
k = [Ex Ey Ez];

c1 = Rotor (n, k);
c2 = Rotor(c1, n);
  
N1  =(k*n')*n;
absN = sqrt(n*n');
kref=(-c2+N1);
abskref = sqrt(kref*kref');
kref  = kref./abskref;
abskref1 = sqrt(kref*kref');

RefX = kref(1);
RefY = kref(2);
RefZ = kref(3);

%absRefK = sqrt(kref*kref');
%RefX = kref(1)/absRefK;
%RefY = kref(2)/absRefK;
%RefZ = kref(3)/absRefK;
%absRefK2 = sqrt(RefX^2+RefY^2+RefZ^2);

kRef_Index = find(kref == max(kref));

switch kRef_Index
    case 1 
		xRef = AmplE;
		tRef = (xRef - xM)/RefX;
		yRef = yM + RefY*tRef;
		zRef = zM + RefZ*tRef;
    case 2
		yRef = AmplE;
		tRef = (yRef - yM)/RefY;
		xRef = xM + RefX*tRef;
		zRef = zM + RefZ*tRef;
    case 3
		zRef = AmplE;
		tRef = (zRef - zM)/RefZ;
		xRef = xM + RefX*tRef;
		yRef = zM + RefY*tRef;
end

RefRay = struct('X0', xM, 'Y0', yM, 'Z0', zM,...
					 'X',xRef, 'Y', yRef, 'Z', zRef,...
					 'kX', RefX, 'kY', RefY, 'kZ', RefZ);

end

