function inputSurf = SetSurf_0
Fx = 1000;
Fy = 1000;
Cz  = 1;
dXdY = 5;
L = 0;
X = -100 : dXdY : 100;
Y = -100 : dXdY : 100;
inputSurf = struct( 'Fx', Fx, 'Fy', Fy, 'Cz', Cz, 'dXdY', dXdY, 'L', L, 'X', X,'Y', Y);
end
