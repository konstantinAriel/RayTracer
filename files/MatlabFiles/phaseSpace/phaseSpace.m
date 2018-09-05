clear all;  close all; clc;
m =1;
n =2;
a = 8;
b = 16;
Nx = 10;
Ny = 10;
A0 = 1;
B0 = 1;
A=A0*(pi*n)^2;
B=B0*(pi*m)^2;

Ka = (2*n)/a;
Kb = (2*m)/b;

if m == 0
    yConst = b/2;           %max of MODE  - Y 
else
    yConst = b/(2*m);  %max of MODE  - Y 
end
yConstVector(1:Ny) = yConst; 
x = linspace(0, a,  Nx);
y = linspace(0, b,  Ny);
[X,Y] = meshgrid(x, y);

sax = sinc(Ka.*(X - (a/2)));
sby = sinc(Kb.*(Y - (b/2)));

b11 = (1 + sax);
b12 = (1 - sby);

a11 = (1 - sax);
a12 = (1 + sby);

xy =(y-(b/2))'*(x - (a/2));

Bb11b12 = B*(b11.*b12);
Aa11a12 = A*(a11.*a12);
Sxy  = (xy/4) .*(Bb11b12  + Aa11a12);
% SxyMatrix = ones(Ny, 1);
% SxyMatrix =SxyMatrix*Sxy; 
figure (1)
%plot(x, Sxy)
mesh(X,Y, Sxy)
title('Sxy')
xlabel('X')

% figure (2)
% plot(y, Sxy)
% xlabel('Y')

% figure (3)
% plot(x, a11)
%hold on
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%   1
xVector = X(1,:);
%yConst = 
Smax = Sxy(Nx);
%%
Nxnew = 20;
finishPoint = Nxnew-1;
for i = 1:(finishPoint)
Snormal(i) = (Smax/(Nxnew)) * i;
end
%% find X
% Mean Root Squars

epsilon =0.00001;
for j = 1:finishPoint
   Sj =  Snormal(j);
   %Sj  = a11(j);
    Xmin = 0;
    Xmax = a;
    Xmean = ( Xmax + Xmin ) / 2;
%      sax1 =  (sinc(Ka*Xmean));
%      sby1 = (sinc(Kb*yConst)) ;
%      a = 1-sax1;
%      b= 1+sby1;
%      xy1= (Xmean*yConst)/4;

    saxCmean = sinc(Ka.*(Xmean-(a/2)));  %Vector
    sbyCmean = sinc(Kb*yConst);  % Number
 
    b11Cmean = (1 + saxCmean);  % vector
    b12Cmean = (1 - sbyCmean);  % Number

    a11Cmean = (1-saxCmean);  % Vector
    a12Cmean = (1+ sbyCmean); % Number
    Bb11b12Cmean = B*(b11Cmean*b12Cmean);  
    Aa11a12Cmean = A*(a11Cmean*a12Cmean);
    
     Si = (((Xmean)*yConst)/4) * (Bb11b12Cmean  + Aa11a12Cmean);
     %Si = ((Xmean*yConst)/4) *A* (1+sinc(Kb*yConst)) * (1- sinc(Ka*Xmean));
     %Si = (1- sinc(Ka*Xmean));
     dS = (Si-Sj) ;
     %disp(' ================================== ')
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
    
            Si = (((Xmean - (a/2))*yConst)/4) * (Bb11b12Cmean  + Aa11a12Cmean);
            %Si = ((Xmean*yConst)/4) *A* (1+sinc(Kb*yConst)) * (1- sinc(Ka*Xmean));
            
           %Si =  (1- sinc(Ka*Xmean));
            dS =  (Si-Sj);
        end
    %disp( ' -----------------------------------------------  ' )
    end
    XmeanArray(j) = (Xmean);
end
%%
xx = ones(1,finishPoint);
% Create stem
figure (4)
stem(XmeanArray, xx);
xlim([0 5])
hold on;
%%  Take  a rays from X-distribution
[xSize, ySize] = size(XmeanArray);
XmeanArrayPad = zeros(1, ySize+2);
[xSizePad, ySizePad] = size(XmeanArrayPad);
XmeanArrayPad(1, 2:ySizePad-1) = XmeanArray;
XmeanArrayPad(1) = 0;
XmeanArrayPad(ySizePad) = a;

xRayArray = zeros(1, ySizePad-1);
for  XmeanIndex = 1:ySizePad-1
    
    x1 = XmeanArrayPad(XmeanIndex);
    x2 = XmeanArrayPad(XmeanIndex+1);
    xRay = (x1 + x2) / 2;
    xRayArray(1, XmeanIndex)  =  xRay;
end
xxPad = ones(1,finishPoint+1);
stem(xRayArray, xxPad, 'red');

for  XmeanIndex = 1 : ySizePad - 1
    x1 = XmeanArrayPad(XmeanIndex);
    x2 = XmeanArrayPad(XmeanIndex + 1);
    deltaxRay = (x2 - x1);
    deltaxRayArray(1, XmeanIndex)  = deltaxRay;
end

figure (5)
plot(deltaxRayArray)



