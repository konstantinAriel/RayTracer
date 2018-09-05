clear all; close all; clc;
m = 1;
n = 2;
a = 8;
b = 16;
Nx = 100;
Ny = 100;
Nxnew =102;
Nynew = 102;
A0 = 1;
B0 = 1;
A=A0*(pi*m)^2;
B=B0*(pi*n)^2;

if n == 0
    yConst = b/2;           %max of MODE  - Y
    yN = 25;
elseif n == 1
        yN = 25;
elseif n == 2
      yN = 15;
elseif n==3
       yN = 18;
else
       yConst = b/(2*n);  %max of MODE  - Y
end

Ka = (2*m)/a;
Kb = (2*n)/b;

x = linspace(0, a,  Nx);
y = linspace(0, b, Ny);
[X,Y] = meshgrid(x,y);
%%
Sz =(sin((m*pi*X)/a).*cos((n*pi*Y)/b)).^2 + (cos((m*pi*X)/a).*sin((n*pi*Y)/b)).^2;
figure(20)
mesh(X,Y, Sz)
xlabel('X, [mm]')
ylabel('Y, [mm]')
title('Vector Pointing')
%%
sax = sinc(Ka.*X);
sby = sinc(Kb.*Y);

b11 = (1 + sax);
b12 = (1 - sby);

a11 = (1 - sax);
a12 = (1 +  sby);

xy = (y)'*(x);

Bb11b12 = B*(b11.*b12);
Aa11a12 = A*(a11.*a12);
Sxy  = (Bb11b12  + Aa11a12);
SxyT  =  (X.*Y/4) .*(Bb11b12  + Aa11a12);

figure(1)                                                                                                                                                 % figure 1 - Sxy
mesh(X, Y, SxyT)
title('SxyT')

% % % figure(2)                                                                                                                                                 % figure 2 - SxyT   n = '  num2str(yN)
% % % plot(x, SxyT(yN, :))
% % % title({['SxyT   n = '  num2str(yN)]})

%%   find X  - Mean Root Squars

xC = linspace(0, a,  Nx);
if n == 0
    yConst = b/2;           %max of MODE  - Y
    yN = 52;
elseif n == 1
        yN = 52;
         yConst = b/(2*n); 
elseif n == 2
      yN = 26;
       yConst = b/(2*n); 
elseif n==3
       yN = 18;
        yConst = b/(2*n); 
end

%%
saxC = sinc(Ka.*xC);
sbyC = sinc(Kb.*yConst);

b11C = (1 + saxC);
b12C = (1 - sbyC);

a11C = (1 - saxC);
a12C = (1 +  sbyC);

xy = yConst*xC;

Bb11b12C = B*(b11C.*b12C);
Aa11a12C = A*(a11C.*a12C);
%SxyConst  = (Bb11b12  + Aa11a12);
SzConst  =  (xC.*yConst/4) .*(Bb11b12C  + Aa11a12C);
figure(3)                                                                                                                                                 % figure 3 - SzConst,  -->   yConst = '  num2str(yConst)]}
plot(xC, SzConst)
title({['SzConst,  -->   yConst = '  num2str(yConst)]})

Smax = SzConst(Nx);

finishPoint = Nxnew-1;
for i = 1:(finishPoint)
Snormal(i) = (Smax/(Nxnew)) * i;
end
 
epsilon =0.00001;
for j = 1:finishPoint
   Sj =  Snormal(j);
    Xmin = 0;
    Xmax = a;
    Xmean = ( Xmax + Xmin ) / 2;
    
    saxCmean = sinc(Ka*(Xmean));  %Vector
    sbyCmean = sinc(Kb*yConst);  % Number
 
    b11Cmean = (1 + saxCmean);  % vector
    b12Cmean = (1 - sbyCmean);  % Number

    a11Cmean = (1-saxCmean);  % Vector
    a12Cmean = (1+ sbyCmean); % Number
    
    Bb11b12Cmean = B*(b11Cmean*b12Cmean);  
    Aa11a12Cmean = A*(a11Cmean*a12Cmean);
    
     Si = ((Xmean*yConst)/4) * (Bb11b12Cmean  + Aa11a12Cmean);

     dS = (Si-Sj) ;
     
    while  abs(dS)  > epsilon
        if Xmax == Xmin
            dS = epsilon/2;
        else
            if  dS > 0
                Xmax = Xmean;
            else
                Xmin = Xmean;
            end
             Xmean = ( Xmax + Xmin ) / 2;
             saxCmean = sinc(Ka.*(Xmean));  %Vector
             sbyCmean = sinc(Kb*yConst);  % Number
 
            b11Cmean = (1 + saxCmean);  % vector
            b12Cmean = (1 - sbyCmean);  % Number

            a11Cmean = (1-saxCmean);  % Vector
            a12Cmean = (1+ sbyCmean); % Number
            
             Bb11b12Cmean = B*(b11Cmean*b12Cmean);  
            Aa11a12Cmean = A*(a11Cmean*a12Cmean);
    
            Si = (((Xmean )*yConst)/4) * (Bb11b12Cmean  + Aa11a12Cmean);
           
            dS =  (Si-Sj);
        end
    end
    XmeanArray(j) = (Xmean);
end
XmeanArray = XmeanArray-(a/2);
%%
xx = ones(1,finishPoint);
% Create stem
figure (4)                                                                                                                                                % figure 4 -  distribution  for X
stem(XmeanArray, xx, 'blue');
title('distribution  for X')
xlim([0 a])
hold on;

[xSize, ySize] = size(XmeanArray);
% XmeanArrayPad = zeros(1, ySize+2);
% [xSizePad, ySizePad] = size(XmeanArrayPad);
% XmeanArrayPad(1, 2:ySizePad-1) = XmeanArray;
% XmeanArrayPad(1) = 0;
% XmeanArrayPad(ySizePad) = a;
xRayArray = zeros(1, ySize-1);
for  XmeanIndex = 1:ySize-1
    x1 = XmeanArray(XmeanIndex);
    x2 = XmeanArray(XmeanIndex+1);
    xRay = (x1 + x2) / 2;
    xRayArray(1, XmeanIndex)  =  xRay;
end
%xRayArray = xRayArray-(a/2);
xxPad = ones(1, finishPoint-1);
stem(xRayArray, xxPad, 'red');                                                                                                             %   stem(xRayArray, xxPad, 'red');   
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%   find Y  - Mean Root Squars

yC = linspace(0, b,  Ny);
if m == 0
    xConst = a/2;          %max of MODE  - Y
    xN = 52;
elseif m == 1
        xN = 52;
         xConst = a/(2*m); 
elseif m == 2
      xN = 26;
       xConst = a/(2*m); 
elseif m==3
       xN = 18;
        xConst = a/(2*m); 
end

% % % figure(10)                                                                                                                                               % figure 10  -'SxyT   Xn = '  num2str(xN)]
% % % plot(y, SxyT(:, xN))
% % % title({['SxyT   Xn = '  num2str(xN)]})

saxCx = sinc(Ka*xConst);
sbyCx = sinc(Kb.*yC);

b11Cx = (1 + saxCx);
b12Cx = (1 - sbyCx);

a11Cx = (1 - saxCx);
a12Cx = (1 +  sbyCx);

xyx = yC*xConst;

Bb11b12Cx = B*(b11Cx.*b12Cx);
Aa11a12Cx = A*(a11Cx.*a12Cx);
%SxyConst  = (Bb11b12  + Aa11a12);
SzConstx  =  (xConst.*yC/4) .*(Bb11b12Cx  + Aa11a12Cx);
figure(11)                                                                                                                                               % figure 11  -   'SzConstX,  -->   xConst = '  num2str(xConst)  
plot(yC, SzConstx)
title({['SzConstX,  -->   xConst = '  num2str(xConst)]})

SmaxX = SzConstx(Ny);

finishPointX = Nynew-1;
for i = 1:(finishPointX)
SnormalX(i) = (SmaxX/(Nynew)) * i;
end
 
epsilon =0.00001;
for j = 1:finishPointX
   Sjx =  SnormalX(j);
    Ymin = 0;
    Ymax = b;
    Ymean = ( Ymax + Ymin ) / 2;
    
    saxCmeanx = sinc(Ka*xConst);  %Vector
    sbyCmeanx = sinc(Kb*Ymean);  % Number
 
    b11Cmeanx = (1 + saxCmeanx);  % vector
    b12Cmeanx = (1 - sbyCmeanx);  % Number

    a11Cmeanx = (1-saxCmeanx);  % Vector
    a12Cmeanx = (1+ sbyCmeanx); % Number
    
    Bb11b12Cmeanx = B*(b11Cmeanx*b12Cmeanx);  
    Aa11a12Cmeanx = A*(a11Cmeanx*a12Cmeanx);
    
    Six = ((Ymean*xConst)/4) * (Bb11b12Cmeanx  + Aa11a12Cmeanx);

    dSx = (Six-Sjx) ;
     
    while  abs(dSx)  > epsilon
        if Ymax == Ymin
            dSx = epsilon/2;
        else
            if  dSx > 0
                Ymax = Ymean;
            else
                Ymin = Ymean;
            end
             Ymean = ( Ymax + Ymin ) / 2;
             saxCmeanx = sinc(Ka*xConst);  %Vector
             sbyCmeanx = sinc(Kb*Ymean);  % Number
 
            b11Cmeanx = (1 + saxCmeanx);  % vector
            b12Cmeanx = (1 - sbyCmeanx);  % Number

            a11Cmeanx = (1-saxCmeanx);  % Vector
            a12Cmeanx = (1+ sbyCmeanx); % Number
            
             Bb11b12Cmeanx = B*(b11Cmeanx*b12Cmeanx);  
            Aa11a12Cmeanx = A*(a11Cmeanx*a12Cmeanx);
    
            Six = ((Ymean *xConst)/4) * (Bb11b12Cmeanx  + Aa11a12Cmeanx);
           
            dSx =  (Six-Sjx);
        end
    end
    YmeanArray(j) = Ymean;
end
YmeanArray = YmeanArray - (b/2);
yy = ones(1,finishPointX);
% Create stem
figure (12)                                                                                                                                              % figure 12  - distribution  for Y     
stem(YmeanArray, yy, 'blue');
title('distribution  for Y')
xlim([0 b])
hold on;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Take  a rays from Y-distribution
[xySize, yySize] = size(YmeanArray);
% YmeanArrayPad = zeros(1, yySize+2);
% [xySizePad, yySizePad] = size(YmeanArrayPad);
% YmeanArrayPad(1, 2:yySizePad-1) = YmeanArray;
% YmeanArrayPad(1) = 0;
% YmeanArrayPad(ySizePad) = b;

yRayArray = zeros(1, yySize-1);
for  YmeanIndex = 1:ySize-1
    y1 = YmeanArray(YmeanIndex);
    y2 = YmeanArray(YmeanIndex+1);
   yRay = (y1 + y2) / 2;
   yRayArray(1, YmeanIndex)  =  yRay;
end
%  yRayArray = yRayArray - (b/2);
 yyPad = ones(1, finishPointX - 1);
 stem(yRayArray, yyPad, 'red');

% for  XmeanIndex = 1 : ySize- 1
%     x1 = XmeanArrayPad(XmeanIndex);
%     x2 = XmeanArrayPad(XmeanIndex + 1);
%     deltaxRay = (x2 - x1);
%     deltaxRayArray(1, XmeanIndex)  = deltaxRay;
% end
%%
[xGrid, yGrid]  = meshgrid(XmeanArray, YmeanArray);
[xxSize, xySize] = size(XmeanArray);
[yxSize, yySize] = size(YmeanArray);
zGrid = zeros(xySize, yySize);
figure(30)                                                                                                                                               %  figure 30 - XY distribution 2D-Grid
mesh(xGrid, yGrid, zGrid);
xlabel('X, [mm]')
ylabel('Y, [mm]')
xlim([-a/2 a/2]);
ylim([-b/2 b/2]);
hold on;
[yRayArrayGrid, xRayArrayGrid] = meshgrid(yRayArray, xRayArray);
plot(xRayArrayGrid, yRayArrayGrid, '.r')
title({['XY distribution 2D-Grid   ||||     m = '  num2str(m)  '   n = ' num2str(n) '  Number of Points Ny = '  num2str(Nynew)  '  Nx = ' num2str(Nxnew)]})
view(0, 90);
axis equal
%%
save('xyPoints100x100.mat', 'xRayArray', 'yRayArray', 'm', 'n')