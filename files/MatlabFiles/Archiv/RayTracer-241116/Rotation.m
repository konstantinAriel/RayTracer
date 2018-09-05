
function [M] =  Rotation (angel_degre)
 angel_Rad =  Deg2Rad(angel_degre);
x_Rad =angel_Rad(1,1);
y_Rad = angel_Rad(1,2);
z_Rad = angel_Rad(1,3);
 Rx = 	[	1			0 			0			; 
				0 	cos(x_Rad) sin(x_Rad)		;...
				0	  -sin(x_Rad) cos(x_Rad)	];
				
    Ry = 	[	cos(y_Rad) 	0  -sin(y_Rad)	;...
					0 		  	1 		0			;...
				sin(y_Rad) 	0  cos(y_Rad)	];
    
    Rz = 	[	cos(z_Rad) sin(z_Rad) 0		;...
			  -sin(z_Rad) cos(z_Rad) 0		;...
					0 			   0 		1		];
M= Rx*Ry*Rz;
end
