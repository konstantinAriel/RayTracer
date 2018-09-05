function [surfParam, rotateParam, shiftParam, surfSizeParam, Center, F, M, Source] = SetMir_1 (L1, L2, L3)
%% Surf [mm]

Fz = L3/2;
Fx = 10000000;

dx = 0;  
dy = -Fz    %% dY > 0  => to Left
dz = -400;     %% dz < 0  =>  to UP

shiftParam = struct('dx', dx, 'dy', dy, 'dz', dz); 

xCenter =  dx; 
yCenter = -dy; 
zCenter = -dz;
Center = struct('X',xCenter, 'Y',yCenter, 'Z',zCenter);
xF = dx; 
yF = Fz - dy 
zF = -dz;
F = struct('X',xF, 'Y',yF, 'Z',zF);
xM = dx ;
yM = Fz - dy;
zM = -2*Fz - dz;
M = struct ('X',xM, 'Y',yM, 'Z',zM);
xS = dx; yS = (yM+(2*Fz)); zS = (-2*Fz) - dz;
Source  = struct('X',xS, 'Y',yS, 'Z',zS);
 
Czz = -1/(4*Fz); % x^2
Cxx = 1/(4*Fx); % y^2

Cz = 0;       % x  
Cx = 0;       % y
Cxz = 0;      % x*y 
Cy = 1;
surfParam = struct('Fx', Fx, 'Fz', Fz,...
						'Cx', Cx, 'Cz', Cz, 'Cxz', Cxz, 'Cxx', Cxx,...
						'Czz', Czz, 'Cy', Cy);
						
%% Rotate [Degree]
a_Degre  = 0; 
a_Rad = Deg2Rad(a_Degre);
rotateDirection = 'X';
rotateParam = struct('a_Rad', a_Rad, 'rotateDirection', rotateDirection);

%% Shifting [mm];

%% SurfSize
dXdZ = 5;
diamX = 250;
diamZ = 250;

surfSizeParam = struct('diamX', diamX, 'diamZ', diamZ, 'dXdZ', dXdZ);

%inputMir = struct( 'Fx', Fx, 'Fy', Fy, 'Cz', Cz, 'dXdY', dXdY, 'L', L, 'X', X,'Y', Y);
end
