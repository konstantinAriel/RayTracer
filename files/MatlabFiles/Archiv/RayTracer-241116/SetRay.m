function Ray = SetRay (M, O, Ray0)

x0 = M.s0.X + Ray0.dS(1,1);
y0 = M.s0.Y + Ray0.dS(1,2);
z0 = M.s0.Z + Ray0.dS(1,3);

kX = Ray0.K(1,1); 
kY = Ray0.K(1,2);
kZ = Ray0.K(1,3);

Cx =  M.surfParam.Cx;
Cz =  M.surfParam.Cz;
Cxz = M.surfParam.Cxz;
Cxx = M.surfParam.Cxx;
Czz = M.surfParam.Czz;
Cy =  M.surfParam.Cy;
dx = O.dx;
dy = O.dy;
dz = O.dz;

	%aMir = (Cxx*kX^2 + 2*Cxz*kX*kZ + Czz*kZ^2);
	%bMir = 2*Cxx*kX*x0 + Cz*kZ - Cy*kY - Cx*kX + 2*Cxz*kZ*x0 + 2*Cxz*kX*z0 + 2*Czz*kZ*z0;
	%cMir = Cy*dy - Cy*y0 + Cx*x0 + Cz*z0 + Cxx*x0^2 + Czz*z0^2 + 2*Cxz*x0*z0;

 aMir = (Cxx*kX^2 + 2*Cxz*kX*kZ + Czz*kZ^2);
 bMir = 2*Cxx*kX*(x0+dx) + Cz*kZ - Cy*kY - Cx*kX + 2*Cxz*kZ*(x0+dx) + 2*Cxz*kX*(z0+dz) + 2*Czz*kZ*(z0+dz);
 cMir = -Cy*(y0+dy) + Cx*(x0+dx) + Cz*(z0+dz) + Cxx*(x0+dx)^2 + Czz*(z0+dz)^2 + 2*Cxz*(x0+dx)*(z0+dz);
 
%CoeffMir = [ - Cxx*kX^2 - Czz*(cos(a_Rad)*kZ + kY*sin(a_Rad))^2 - 2*Cxz*kX*(cos(a_Rad)*kZ + kY*sin(a_Rad)),... 
%					2*Cxy*(dx - x0)*(cos(a_Rad)*kY + kZ*sin(a_Rad)) - Cy*(cos(a_Rad)*kY + kZ*sin(a_Rad)) - Cz*(cos(a_Rad)*kZ - kY*sin(a_Rad)) - Cx*kX - 2*Cyy*(cos(a_Rad)*kY + kZ*sin(a_Rad))*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0) + 2*Cxx*kX*(dx - x0) - 2*Cxy*kX*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0),...
%					Cx*(dx - x0) - Cy*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0) - Cxx*(dx - x0)^2 - Cyy*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0)^2 + Cz*(dz - cos(a_Rad)*z0 + sin(a_Rad)*y0) + 2*Cxy*(dx - x0)*(cos(a_Rad)*y0 - dy + sin(a_Rad)*z0)];
 
p = [aMir bMir cMir];     % aMir*x^2 + bMir*x  + cMir = 0
t = roots(p)  ;                           
[tX, ~] = size(t);
if tX == 1
% t1 = (-B+sqrt(B^2-4*A*C))/(2*A);
% t2 = -B-(B^2-4*A*C); 

x1 = x0+ kX*t(1,1);
y1 = y0 +kY*t(1,1);
z1 = z0+kZ*t(1,1);
elseif tX == 2
x1 = x0 + kX*t(2,1);
y1 = y0 + kY*t(2,1);
z1 = z0 + kZ*t(2,1);
end


Ray = struct ('X0', x0, 'Y0', y0,'Z0', z0,...
             'X', x1, 'Y', y1, 'Z', z1,...
             'kX', kX, 'kY', kY, 'kZ', kZ);  
    
    
end

