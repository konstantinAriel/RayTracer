function [ surfNew] = ChoseRotateAxis (a_Deg, surfOld, rotateAxis )
a_Rad = Deg2Rad(a_Deg)
    Rx = 	[	cos(a_Rad) 	0  -sin(a_Rad)	;...
					0 		  	1 		0			;...
				sin(a_Rad) 	0  cos(a_Rad)	];
    
    Ry = 	[	1			0 			0			; 
				0 	cos(a_Rad) sin(a_Rad)		;...
				0	  -sin(a_Rad) cos(a_Rad)	];
    
    Rz = 	[	cos(a_Rad) sin(a_Rad) 0		;...
			  -sin(a_Rad) cos(a_Rad) 0		;...
					0 			   0 		1		];
    switch rotateAxis
        
		case    'X'
        Xnew = Rx(1,1).*surfOld.X + Rx(1,2).*surfOld.Y + Rx(1,3).*surfOld.Z;
        Ynew = Rx(2,1).*surfOld.X + Rx(2,2).*surfOld.Y + Rx(2,3).*surfOld.Z;
        Znew = Rx(3,1).*surfOld.X + Rx(3,2).*surfOld.Y + Rx(3,3).*surfOld.Z;
		
        case  'Y'
        Xnew = Ry(1,1).*surfOld.X + Ry(1,2).*surfOld.Y + Ry(1,3).*surfOld.Z;
        Ynew = Ry(2,1).*surfOld.X + Ry(2,2).*surfOld.Y + Ry(2,3).*surfOld.Z;
        Znew = Ry(3,1).*surfOld.X + Ry(3,2).*surfOld.Y + Ry(3,3).*surfOld.Z;
        
       case  'Z'
        Xnew = Rz(1,1).*surfOld.X + Rz(1,2).*surfOld.Y + Rz(1,3).*surfOld.Z;
        Ynew = Rz(2,1).*surfOld.X + Rz(2,2).*surfOld.Y + Rz(2,3).*surfOld.Z;
        Znew = Rz(3,1).*surfOld.X + Rz(3,2).*surfOld.Y + Rz(3,3).*surfOld.Z;
end
surfNew = struct('X', Xnew, 'Y', Ynew, 'Z', Znew);
end



