clc;
close all;
clear all;
%%
load('xyPoints100x100.mat')
%rootF = 'C:\Users\konstantinsh\Google Drive\U4eba\Ariel University\TOAR_II\TEZA\MatlabFiles\phaseSpace\resultXls\';
rootF = 'C:\Users\konstantinsh\Desktop\resultXls';
%%
a = 8;          % mm
b = 16;         % mm
% x0 = 3.6;     %(0, 0)  center of wavegude;   x = a/2 - right boder of the wave gude; y = b/2 up border of the wave gude
% y0 = 5.28;
c = 3e11;       %  light speed  [mm/sec]
f = 3e12;   % frequency  [3 THz]
l = (c/f) ;     % wave length  (0.1 - 0.3 mm)

NKx = 100;
NKy = 100;
% Kx = linspace((-2*pi/l)*a, (2*pi/l)*a, NKx);
% Ky = linspace((-2*pi/l)*b, (2*pi/l)*b, NKy);
Kx = 0.395*linspace(-2*pi/l, 2*pi/l, NKx);
%Kx = linspace(-2*pi/l, 2*pi/l, NKx);
Kxy =ones(1, NKx);
% % Kx = Kx./sqrt(1+Kx.^2);
% Kxy =  Kxy/sqrt(1+Kx.^2);
Ky =0.395*linspace(-2*pi/l, 2*pi/l, NKy);
%Ky =linspace(-2*pi/l, 2*pi/l, NKy);
K0x = (m*pi)/a;
K0y = (n*pi)/b;
[KxMesh, KyMesh] = meshgrid(Kx,Ky);
Kn2 = KxMesh.^2 + KyMesh.^2;
aa = (2*pi/l)^2;
K0z2 = (2*pi/l)^2 - Kn2;
[xArraySize,~] = size(xRayArray');
[yArraySize,~] = size(yRayArray');
dKx = 0.395*4*pi/(l*NKx);
dKy = 0.395*4*pi/(l*NKy);
deltaAml = (dKx*dKy)/(xArraySize*yArraySize);
%%
%xArraySize=2;
step_index = 0;
for x_main = 1:xArraySize
    for y_main = 1:yArraySize
        step_index = step_index+1;
        x0 = xRayArray(x_main); %(0,0) center of wavegude; x = a/2 - right boder of the wave gude; y = b/2 up border of the wave gude
        y0 = yRayArray(y_main);
        %x0 = xRayArray(40)
        %y0 = yRayArray(50)
        a1x =  (a/2 - abs(x0));
        a21x = 2*K0x*(x0+a/2);
        a31x = (KxMesh + K0x);
        a32x = (KxMesh - K0x);
        a1y =  (b/2-abs(y0));
        a21y = 2*K0y*(y0+b/2);
        a22x =(b/2-abs(y0));
        a31y = (KyMesh + K0y);
        a32y = (KyMesh - K0y);
        
        A11x  = cos(a21x);
        A12x = sinc((2*KxMesh*a1x)./pi);
        A21x =  sinc((2*a1x*a31x)./pi);
        A31x = sinc((2*a1x*a32x)./pi);
        
        A11y = cos(a21y);
        A12y = sinc((2*KyMesh*a1y)./pi);
        A21y = sinc((2*a1y*a31y)./pi);
        A31y = sinc((2*a1y*a32y)./pi);
        
        fcX = a1x*(2*A11x.*A12x + A21x + A31x);
        fsX = a1x*(2*A11x.*A12x - A21x - A31x);
        
        fcY = a1y*(2*A11y*A12y + A21y + A31y);
        fsY = a1y*(2*A11y*A12y - A21y - A31y);
        
        wX_xyKxKy_TM = ((((K0x.^2).*K0z2)./Kn2).*fcX.*fsY)*deltaAml;
        %wX_xyKxKy_TM = fcX.*fsY;
        wY_xyKxKy_TM = ((((K0y.^2).*K0z2)./Kn2).*fsX.*fcY)*deltaAml;
        % x0vector = x0.*ones(1,NKx);
        % xx = x0 + Kx.* wX_xyKxKy_TM;
        % xx = x0 + Kx.* wX_xyKxKy_TM;
        % xy0Vector =  x0.*ones(1,NKx);
        % xy = xy0Vector  + Kxy.* wX_xyKxKy_TM ;
        %%
        %plot([x0vector ; xx],  [xy0Vector;   xy])
                %figure (x_main);
                mesh(KxMesh, KyMesh, (wX_xyKxKy_TM))
                title({['Wx -->  m= '  num2str(m) ' n = ' num2str(n) '  X = ' num2str(x0) '  Y = ' num2str(y0)]});
                xlabel({'Kx =  '});
                ylabel ({'Ky'});
                colormap default;
                %figure (10+y_main);
                mesh(KxMesh, KyMesh, (wY_xyKxKy_TM))
                title({['Wy -->  m= '  num2str(m) ' n = ' num2str(n) '  X = ' num2str(x0) '  Y = ' num2str(y0)]});
                xlabel({'Kx =  '});
                ylabel ({'Ky'});
                colormap default;
        
        %xy = y0+ Ky.* wY_xyKxKy_TM;
        %[xW, yW] = size(wX_xyKxKy_TM);
        % for i=0:yW
        % [pks, locs, w, p] = findpeaks(wX_xyKxKy_TM);
        %
        % end
        %%
        % %         BW = imbinarize(wX_xyKxKy_TM);
        % %         [B,L] = bwboundaries(BW,'noholes');
        % %         figure(5)
        % %         label2rgb(L);
        % %         statistics_data = regionprops(L);
        % %         centroids = cat(1, statistics_data.Centroid);
        
        % figure(3)
        % imshow(wX_xyKxKy_TM);
        % hold on
        % plot(centroids(:,1),centroids(:,2), 'b.')
        % for k = 1:length(B)
        %    boundary = B{k};
        %    plot(boundary(:,2), boundary(:,1), 'r', 'LineWidth', 2)
        % end
        % hold off
        %%
        %yNum = 37;
        
        % %         [pks, locs, w, p] = findpeaks(abs(wX_xyKxKy_TM(yNum, :)));
        % %         figure(30);
        % %         plot(KxMesh(yNum, :), (wX_xyKxKy_TM(yNum, :)));
        % %         hold on;
        % %         [xL, yL] = size(locs);
        % %         for iLocation = 1:yL
        % %             location = locs(iLocation);
        % %             stem(KxMesh(1, location), wX_xyKxKy_TM(yNum, location));
        % %         end
        % %         %%
        % %         yNum = 250;
        % %         [pks, locs, w, p] = findpeaks(abs(wX_xyKxKy_TM(yNum, :)));
        % %         figure(40);
        % %         plot(KxMesh(yNum, :), (wX_xyKxKy_TM(yNum, :)));
        % %         hold on;
        % %         [xL, yL] = size(locs);
        % %         for iLocation = 1:yL
        % %             location = locs(iLocation);
        % %             stem(KxMesh(1, location), wX_xyKxKy_TM(yNum, location));
        % %         end
        
        %%
        rootMN = [rootF     '\m_' num2str(m) '_n_' num2str(n)];
        rootFx = [rootMN    '\wx\'];
        rootFy = [rootMN    '\wy\'];
        
% % % %         fileNameXY = [rootMN '\xyPoints']
% % % %         fileNameKxKy = [rootMN '\KxKyPoints'];
% % % %         fileNameKxMesh = [rootMN '\KxMesh'];
% % % %         fileNameKyMesh = [rootMN '\KyMesh'];
% % % %         fileNameWx = [rootFx 'wx_X_' num2str(x_main) '_Y_ ' num2str(y_main)];
% % % %         fileNameWy = [rootFy 'wy_X_' num2str(x_main) '_Y_ ' num2str(y_main)];
        KxKy = [Kx' Ky'];
        XY = [xRayArray' yRayArray'];
% % % %         
% % % %                 xlswrite(fileNameXY,XY2xls);
% % % %                 xlswrite(fileNameKxKy,KxKy2xls);
% % % %                 xlswrite(fileNameKxMesh,KxMesh);
% % % %                 xlswrite(fileNameKyMesh,KyMesh);
% % % %                 xlswrite(fileNameWx,wX_xyKxKy_TM)
% % % %                 xlswrite(fileNameWy,wY_xyKxKy_TM)
        fileNameXY      = [rootMN    '\xyPoints.mat'];
        fileNameKxKy    = [rootMN    '\KxKyPoints.mat'];
        fileNameKxMesh  = [rootMN    '\KxMesh.mat'];
        fileNameKyMesh  = [rootMN    '\KyMesh.mat'];
        fileNameWx      = [rootFx    'wx_X_' num2str(x_main) '_Y_' num2str(y_main) '.mat'];
        fileNameWy      = [rootFy    'wy_X_' num2str(x_main) '_Y_' num2str(y_main) '.mat'];

        save(fileNameXY,    'XY');
        save(fileNameKxKy,  'KxKy');
        save(fileNameKxMesh,'KxMesh');
        save(fileNameKyMesh,'KyMesh');
        save(fileNameWx,     'wX_xyKxKy_TM');
        save(fileNameWy,     'wY_xyKxKy_TM');
        
    end
end