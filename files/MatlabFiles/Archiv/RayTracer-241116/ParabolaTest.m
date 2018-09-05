clear all; 
close all; clc;

ax =gca;
A=.0001; 
B=.0001;
inputSurf = [xMin xStep xMax yMin yStep yMax Rx Fx Ry Fy C];
%rotateMatrix = [
[X Y] = meshgrid(x,y);
C=1;
    for j=1:10:100
      % C=j;
       Z=(A*X.^2+B*Y.^2);
       Znew=-X/sqrt(2)+Z/sqrt(2);
       Xnew=X/sqrt(2)+Z/sqrt(2);
       mesh(X,Y,Z)
       axis equal
       colormap('gray')
       title({'A=',num2str(A),' B=',num2str(B)})
       view(24,18);
       hold on
       
       pause(0.1);
    end
    grid;
    figure(2)
    mesh(Xnew,Y,Znew)
view(24,18);
