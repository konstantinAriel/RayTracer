function outSurf = BuildSurf(inputSurf)
Cx = 1/(2*inputSurf.Fx);
Cy= 1/(2*inputSurf.Fy);
Cz = inputSurf.Cz;
%x = -2*inputSurf.Fx : inputSurf.dXdY : 2*inputSurf.Fx;
%y = -2*inputSurf.Fy : inputSurf.dXdY : 2*inputSurf.Fy;
[X,Y] = meshgrid(inputSurf.X, inputSurf.Y);
Z=(Cx*X.^2+Cy*Y.^2)/Cz;
outSurf = struct ('X', X, 'Y', Y, 'Z', Z);
end


