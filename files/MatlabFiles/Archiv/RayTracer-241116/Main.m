clear all; close all ; clc;
%%
dl=0;
Lx = 3800;
Lz = 1300;                          %   400+900            
Ly = 4000;                          %   900+ 3100

L00 = 400;
L33 = 700;

L11 = 400+dl;                   % 400 -  Focus for  M1           
L12 = Lz - L11;                 % 900 - Focus for M2

L22 = Ly -L12;                  % 3100 - Focus for M3
L32 = Lx-L22 ;                 % 700   - Focus for M4

rTline = 125;
%%
V1 =  struct('X',0,           'Y',  L11/2,            'Z', L11);
V2 = struct ('X',0,           'Y', -L12/2,           'Z', L11);
V3 = struct ('X',L22,      'Y',  Ly+L22/2,    'Z', Lz);
V4 = struct ('X',L22,      'Y',  Ly,                  'Z', Lz +L32/2);

S  = [0      -400    0;...
        0       0          400;...
        0       900     1300;...
        3100 4000  1300;...
        3800 4000  600 ];
    
M1 = SetMir(L11, V1, [-90 0 0],  [0 0 0],  rTline*2, S(1,:), S(2,:));
M2 = SetMir(L12, V2, [90 0  0],  [0 0 1300], rTline*2, S(2,:), S(3,:));
M3 = SetMir(L22, V3, [-90 0 0],  [0 4000 1300], rTline*2, S(3, :), S(4,:));
M4 = SetMir(L32, V4, [180 0 0],    [3800 4000 1300], rTline*2, S(4,:), S(5,:));


%%
Ploting (M1);
Ploting (M2);
 Ploting(M3);
 Ploting(M4)
LW = 2;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 plot3 ([-rTline    -rTline],          [-L00            rTline],        [-rTline     -rTline],              '--b', 'Linewidth', LW);        %TLine - S-M1
 plot3 ([rTline       rTline],          [-L00          -rTline],        [rTline        rTline],               '--b', 'Linewidth', LW);        %TLine - S-M1
% 
 plot3 ([-rTline     -rTline],         [rTline         rTline],         [-rTline       Lz-rTline],        '--b', 'Linewidth', LW);         %TLine - M1-M2
 plot3 ([rTline       rTline],          [-rTline      -rTline],         [rTline        Lz+rTline],       '--b',  'Linewidth', LW);         %TlINE - M1-M2
% 
 plot3 ([-rTline     -rTline],         [ rTline       Ly+rTline],   [Lz-rTline   Lz-rTline],      '--b',  'Linewidth', LW);         %TLine - M2-M3
 plot3 ([rTline        rTline],         [-rTline       Ly- rTline ],  [Lz+rTline  Lz+rTline],     '--b',  'Linewidth', LW);         %Tline -M2-M3
% 
 plot3 ([ -rTline     Lx-rTline],    [Ly+rTline  Ly+rTline],  [Lz-rTline   Lz-rTline],      '--b',  'Linewidth', LW);         %TLine - M3-M4
 plot3 ([rTline        Lx+rTline],  [Ly- rTline  Ly- rTline ],  [Lz+rTline  Lz+rTline],     '--b',  'Linewidth', LW);         %Tline -M3-M4
% 
 plot3 ([Lx-rTline  Lx-rTline],   [Ly+rTline  Ly+rTline ],  [Lz-rTline   Lz-L33],         '--b',  'Linewidth', LW);         %TLine - M4-R
 plot3 ([Lx+rTline Lx+rTline],  [Ly- rTline  Ly- rTline ],  [Lz+rTline  Lz-L33],         '--b',  'Linewidth', LW);         %Tline -M4-R
% 
plot3 ([V1.X M1.f.X], [V1.Y M1.f.Y],  [V1.Z M1.f.Z], 'Linewidth', 2)   %FOCUS  LINE M1
plot3 ([V2.X M2.f.X], [V2.Y M2.f.Y],  [V2.Z M2.f.Z], 'Linewidth', 2)   %FOCUS  LINE M2
plot3 ([V3.X M3.f.X], [V3.Y M3.f.Y], [V3.Z M3.f.Z], 'Linewidth', 2)    %FOCUS  LINE M3
plot3 ([V4.X M4.f.X], [V4.Y M4.f.Y], [V4.Z M4.f.Z], 'Linewidth', 2)    %FOCUS  LINE M3

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
zMax = 50;
kmax = 50/400;
% AmplE = 100;
% 
 %K =[ 0 1 -0.05;  0  1  -0.02; 0 1  -0.01;  0  1   0;   0  1  0.01;   0  1  0.02;  0  1  0.05; ];                     % Ky-Kz 
%K =[-0.05 1 -0.05 ;  -0.02  1  -0.02; -0.01  1  -0.01;  0  1   0;   0.01  1  0.01;   0.02  1  0.02;  0.05  1  0.05; ];     %Ky-KxKz
%K =[ 1 -0.05 0;  1 -0.02  0; 1 -0.01  0;  1  0   0;   1  0.01  0;   1  0.02  0;  1  0.05  0;];                                                %Kx-Ky
%K =[ 0 -0.05 1;  0 -0.02  1; 0 -0.01  1;  0  0   1;   0  0.01  1;   0  0.02  1;  0  0.05  1;];  
 %dS = 5*[0 0  -5; 0 0 -4;  0 0 -2;  0 0 0; 0  0 2; 0 0 4; 0 0 5; -5 0  0; -4 0 0;  -2 0 0;  0 0 0; 2 0 0; 0 0 4; 0 0 5];
 dS =10* [0  0  -5;  0 0 0;  0 0 5];
 K =[ 0 1  -0.05 ; 0  1   0;  0  1  0.05 ]; 
%   dS =10* [-5  0  0;  0 0 0;  5 0 0];
%  K =[ -0.05 1  0 ; 0  1   0;  0.05  1  0]; 
% dS =10* [-5 0  -5; -4 0 -4;  -2 0 -2;  0 0 0; 2  0 2; 4 0 4; 5 0 5; -5 0  0; -4 0 0;  -2 0 0;  0 0 0; 2 0 0; 0 0 4; 0 0 5];
 %dS =10* [0 -5  0; 0 -4 0;  0 -2 0;  0 0 0; 0  2 0; 0 4 0; 0 5 0; -5 0  0; -4 0 0;  -2 0 0;  0 0 0; 2 0 0; 4 0 0; 5 0 0];
 %dS =5* [-6 0  0; -4 0 0;  -2 0 0;  0 0 0; 2  0 0; 4 0 0; 6 0 0];
 [nx, ny] = size(K);
 [mx, my] = size (dS);
% %  
  Kmin =1;
  Kmax =3;
% %  
 dSmin = 1;
  dSmax =3;
% %  
  for i = dSmin:dSmax
      for j=Kmin:Kmax
          dS1 = dS(i,: );
x10 =dS1(1,1)+M1.S.X;
x20 = dS1(1,2)+M1.S.Y;
x30 = dS1(1,3)+M1.S.Z;

%%    S  -  M_1 - M_2

k = 1;  l=1;

dX_S_1 = [x10 x20 x30];
K_S_1 = K(j, :);

 Ray_S_1_in(k,1)  = struct('K', K_S_1, 'dX', dX_S_1);
 
[Ray_S_1(i,j), Normal_1_1(i,j), RefRay_1_2(i,j)]  = RaysData (M1, Ray_S_1_in(k,1));

 plot3([Ray_S_1(i,j).X0, Ray_S_1(i,j).X], [Ray_S_1(i,j).Y0, Ray_S_1(i,j).Y], [Ray_S_1(i,j).Z0, Ray_S_1(i,j).Z]);                                                                                          %  OutRay  from Source
 plot3([RefRay_1_2(i,j).X0, RefRay_1_2(i,j).X],[RefRay_1_2(i,j).Y0, RefRay_1_2(i,j).Y],[RefRay_1_2(i,j).Z0, RefRay_1_2(i,j).Z]);                                                       %  Reflected Ray from Mirror
 %plot3 ([Normal_1_1(i,j).X0, Normal_1_1(i,j).X], [Normal_1_1(i,j).Y0, Normal_1_1(i,j).Y], [Normal_1_1(i,j).Z0, Normal_1_1(i,j).Z]);                                                  %  Normal to Mirror in cross with Ray
 
 %	[ePolarRay, rPolarRay] = PolarVector (Ray11(i,j), Normal1(i,j), AmplE);  
%  	%plot3([ePolarRay.X0, ePolarRay.X],[ePolarRay.Y0, ePolarRay.Y],[ePolarRay.Z0, ePolarRay.Z], 'r', 'Linewidth', 2);  
%  	%plot3([rPolarRay.X0, rPolarRay.X],[rPolarRay.Y0, rPolarRay.Y],[rPolarRay.Z0, rPolarRay.Z], 'r', 'Linewidth', 2);  

%%   M_1 - M_2 - M_3
dX_1_2 = [RefRay_1_2(i,j).X  RefRay_1_2(i,j).Y  RefRay_1_2(i,j).Z];
K_1_2  =  [RefRay_1_2(i,j).kX RefRay_1_2(i,j).kY RefRay_1_2(i,j).kZ];

 Ray_1_2_in (k,1) = struct('K', K_1_2, 'dX', dX_1_2);
 [Ray_1_2(i,j), Normal_2_2(i,j), RefRay_2_3(i,j)]  = RaysData (M2, Ray_1_2_in(k,1));
           
  plot3 ([Ray_1_2(i,j).X0, Ray_1_2(i,j).X], [Ray_1_2(i,j).Y0, Ray_1_2(i,j).Y], [Ray_1_2(i,j).Z0, Ray_1_2(i,j).Z]);     
  plot3([RefRay_2_3(i,j).X0, RefRay_2_3(i,j).X],[RefRay_2_3(i,j).Y0, RefRay_2_3(i,j).Y],[RefRay_2_3(i,j).Z0, RefRay_2_3(i,j).Z]);  
 %plot3 ([Normal_2_2.X0, Normal_2_2.X], [Normal_2_2.Y0, Normal_2_2.Y], [Normal_2_2.Z0, Normal_2_2.Z]);                                %  Normal to Mirror in cross with Ray

% % % %%  M_2 - M_3 - M_4
dX_2_3 = [RefRay_2_3(i,j).X  RefRay_2_3(i,j).Y  RefRay_2_3(i,j).Z];
K_2_3 = [RefRay_2_3(i,j).kX RefRay_2_3(i,j).kY RefRay_2_3(i,j).kZ];

 Ray_2_3_in (k,1) = struct('K', K_2_3, 'dX', dX_2_3);
 [Ray_2_3(i,j), Normal_3_3(i,j), RefRay_3_4(i,j)]  = RaysData (M3, Ray_2_3_in(k,1));
           
 plot3 ([Ray_2_3(i,j).X0, Ray_2_3(i,j).X], [Ray_2_3(i,j).Y0, Ray_2_3(i,j).Y], [Ray_2_3(i,j).Z0, Ray_2_3(i,j).Z]);     
 plot3([RefRay_3_4(i,j).X0, RefRay_3_4(i,j).X],[RefRay_3_4(i,j).Y0, RefRay_3_4(i,j).Y],[RefRay_3_4(i,j).Z0, RefRay_3_4(i,j).Z]);  
% plot3 ([Normal_3_3.X0, Normal_3_3.X], [Normal_3_3.Y0, Normal_3_3.Y], [Normal_3_3.Z0, Normal_3_3.Z]);                                %  Normal to Mirror in cross with Ray            

%%  M_3 - M_4 - R 

dX_3_4 = [RefRay_3_4(i,j).X  RefRay_3_4(i,j).Y  RefRay_3_4(i,j).Z];
K_3_4 = [RefRay_3_4(i,j).kX RefRay_3_4(i,j).kY RefRay_3_4(i,j).kZ];

 Ray_3_4_in (k,1) = struct('K', K_3_4, 'dX', dX_3_4);
 [Ray_3_4(i,j), Normal_4_4(i,j), RefRay_4_R(i,j)]  = RaysData (M4, Ray_3_4_in(k,1));
           
 plot3 ([Ray_3_4(i,j).X0, Ray_3_4(i,j).X], [Ray_3_4(i,j).Y0, Ray_3_4(i,j).Y], [Ray_3_4(i,j).Z0, Ray_3_4(i,j).Z]);     
 plot3([RefRay_4_R(i,j).X0, RefRay_4_R(i,j).X],[RefRay_4_R(i,j).Y0, RefRay_4_R(i,j).Y],[RefRay_4_R(i,j).Z0, RefRay_4_R(i,j).Z]); 
 %plot3 ([Normal_4_4.X0, Normal_4_4.X], [Normal_4_4.Y0, Normal_4_4.Y], [Normal_4_4.Z0, Normal_4_4.Z]);                                %  Normal to Mirror in cross with Ray   
  
%  Test ( M1, M2, Ray11(i,j),  RefRay1(i,j), Ray22(i,j), RefRay2(i,j), ePolarRay, rPolarRay);
  %pause 
     end
  end
  
  [Xin, Kin, Xout, Kout]  = ChekedABCDE_Matrix(Ray_S_1, RefRay_1_2, Ray_1_2, RefRay_2_3, S)
  %%
  figure
 
  plot(Xin(1,:), Xout(1,:))
  grid
  figure
  plot(Kin(1,:), Kout(1,:))
  grid
  %%
%  

