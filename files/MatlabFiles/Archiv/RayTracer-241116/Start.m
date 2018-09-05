clear all; close all; clc;
x = -100 : 5 : 100;
y = -100 :5 :100;
x1 = -100:5: 100;


[X,Y] = meshgrid(x,y);
[X1,Y1] = meshgrid(x1,y);
figure
Z=(0.001*X.^2 +0.001*Y.^2)+ 50;
hold on
Z1=(0.001*X1.^2 +0.001*Y1.^2)/1;
figure
mesh(X,Y,Z);
hold on
mesh(X1, Y1,Z1);
axis  'equal'
xlabel ('X')
ylabel('Y')
zlabel('Z')

aX_Deg = 0;
aY_Deg = 0;
aZ_Deg = 0;
aX_Rad = Deg2Rad(aX_Deg); 
aY_Rad = Deg2Rad(aY_Deg); 
aZ_Rad = Deg2Rad(aZ_Deg); 




Rx = 	[ 		1			0 						0		; ... 
				0 		cos(aX_Rad) 		sin(aX_Rad)	;...
				0	  -sin(aX_Rad)		cos(aX_Rad)	];
	 
Ry = 	[	cos(aY_Rad) 		0 		  -sin(aY_Rad)	;...
				0 				1 					0		;...
			sin(aY_Rad) 		0  		cos(aY_Rad)	];
			
Rz = 	[	cos(aZ_Rad)   sin(aZ_Rad) 			0	;...
		  -sin(aZ_Rad) 	 cos(aZ_Rad) 			0	;...
				0 			    	0 					1	];
				

Xnew = a11.*X + a12.*Y + a13.*Z;
Ynew = a11.*X + a12.*Y + a13.*Z;
Znew = a11.*X + a12.*Y + a13.*Z;
mesh(Xz30, Yz30, Zz30);
axis  'equal'