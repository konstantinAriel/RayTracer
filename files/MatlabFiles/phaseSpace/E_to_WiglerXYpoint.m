clc; close all; clear all;
load('xyPoints.mat')
%%
a = 5;          % mm
b = 6;          % mm
% x0 = a-5;         %(0, 0)  center of wavegude;   x = a/2 - right boder of the wave gude; y = b/2 up border of the wave gude  
% y0 = b-b;
c = 3e11;       %  light speed  [mm/sec]
f = 3e12;       %frequency  [3 THz]
l = (c/f) ;     % wave length  (0.1 - 0.3 mm)
%%
NKx = 100;
NKy = 100;
K0x = (m*pi)/a;
K0y = (n*pi)/b;
% Kx = linspace((-2*pi/l)*a, (2*pi/l)*a, NKx);
% Ky = linspace((-2*pi/l)*b, (2*pi/l)*b, NKy);

Kxy =ones(1, NKx);
% Kx = Kx./sqrt(1+Kx.^2);
% Kxy =  Kxy/sqrt(1+Kx.^2);
% Ky = linspace(-2*pi/l, 2*pi/l, NKy);
Kx = linspace(-2*pi/l, 2*pi/l, NKx);
Ky = linspace(-2*pi/l, 2*pi/l, NKy);
[KxMesh, KyMesh] = meshgrid(Kx,Ky);
Kn2 = KxMesh.^2 + KyMesh.^2;
K0z2 = (2*pi/l)^2 - Kn2;
%%
[xsX, ysX] = size(xRayArray);
[xsY, ysY] = size(yRayArray);
for xi = 1: ysX
    for yi = 1:ysY
x0 = xRayArray(1,xi);
y0 = yRayArray(1,yi);
a1x =  (a/2 - abs(x0));
a21x = 2*K0x*(x0+a/2);
a31x = (KxMesh + K0x);
a32x = (KxMesh - K0x);

a1y =  (b/2-abs(y0));
a21y = 2*K0y*(y0+b/2);
%a22x =(b/2-abs(y0));
a31y = (KyMesh + K0y);
a32y = (KyMesh - K0y);

A11x  = cos(a21x);
A12x = sinc((2*KxMesh*a1x)./pi);
A21x =  sinc((2*a1x*a31x)./pi);
A31x = sinc((2*a1x*a32x)./pi);

A11y = cos(a21y);
A12y = sinc((2*KyMesh*a1y)./pi);
A21y = sinc((2*a1y*a31y)./pi);
A31y = sinc((2*a1y*a32y)./pi);

fcX = a1x*(2*A11x.*A12x + A21x + A31x);
fsX = a1x*(2*A11x.*A12x - A21x - A31x);

fcY = a1y*(2*A11y*A12y + A21y + A31y);
fsY = a1y*(2*A11y*A12y - A21y - A31y);

%wX_xyKxKy_TM = (((K0x.^2).*K0z2)./Kn2).*fcX.*fsY;
wX_xyKxKy_TM = fcX.*fsY;
%wY_xyKxKy_TM = (((K0y.^2).*K0z2)./Kn2).*fsX.*fcY;
x0vector = x0.*ones(1,NKx);
% xx = x0 + Kx.* wX_xyKxKy_TM;

% xx = x0 + Kx.* wX_xyKxKy_TM;
% xy0Vector =  x0.*ones(1,NKx);
% xy = xy0Vector  + Kxy.* wX_xyKxKy_TM ;
    end
end
%%
%plot([x0vector ; xx],  [xy0Vector;   xy])
figure (1);
mesh(KxMesh, KyMesh, wX_xyKxKy_TM)

% title({['Wx -->  m = '  num2str(m) 'n = ' num2str(n) '  X = ' num2str(x0)]});
% xlabel({['X0 =  '  num2str(x0)]});
% ylabel ({['X = X0 + Wx*Kx']});
title({['Wx -->  m= '  num2str(m) ' n = ' num2str(n) '  X = ' num2str(x0)]});
xlabel({['Kx =  ']});
ylabel ({['Ky']});
colormap default; 
%xy = y0+ Ky.* wY_xyKxKy_TM;
[xW, yW] = size(wX_xyKxKy_TM);
% for i=0:yW
% [pks, locs, w, p] = findpeaks(wX_xyKxKy_TM); 
% 
% end
%%
yNum = 48;
[pks, locs, w, p] = findpeaks(abs(wX_xyKxKy_TM(yNum, :))); 
figure(2);
plot(KxMesh(yNum, :), (wX_xyKxKy_TM(yNum, :)));
hold on;
[xL, yL] = size(locs);
for iLocation = 1:yL
location = locs(iLocation);
stem(KxMesh(1, location), wX_xyKxKy_TM(yNum, location));
end