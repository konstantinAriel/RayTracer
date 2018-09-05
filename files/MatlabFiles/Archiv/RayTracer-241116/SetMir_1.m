function inputMir = SetMir_1
Fx = 300;
Fy = 300;
Cz  = 1;
dXdY = 5;
L = 50;
X = -100 : dXdY : 100;
Y = -100 : dXdY : 100;
inputMir = struct( 'Fx', Fx, 'Fy', Fy, 'Cz', Cz, 'dXdY', dXdY, 'L', L, 'X', X,'Y', Y);
end
