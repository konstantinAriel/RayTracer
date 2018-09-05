function Ploting (M1)
%%Original Mirrror1
figure (1);
mesh( M1.X, M1.Y, M1.Z );  % Mirror 1
hold on;
grid on;
xlabel('X');
ylabel('Y');
zlabel('Z');
axis 'equal';
% plot3 ([0 100],  [0 0], [0 0] , '--r', 'Linewidth',2);
% plot3([0 0], [0 100], [0 0], '--r', 'Linewidth', 2);
% plot3([0 0], [0 0 ], [0 100], '--r', 'Linewidth', 2)
view(310,20);
%view(-90,0);
%colormap([0 0 0]);
set(gcf, 'renderer', 'opengl')
%% Rotated Mirror
%figure (2)
%mesh( outMir_1.X, outMir_1.Y, outMir_1.Z );
%hold on;
%view(90,0);
%axis 'equal';
end

