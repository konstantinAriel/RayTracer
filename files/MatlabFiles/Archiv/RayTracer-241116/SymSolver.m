function [ T, RayOut, coefT ] = SymSolver(surfParam, rotateParam, shiftParam, surfSizeParam, Ray)

Cx = surfParam.Cx; Cy = surfParam.Cy; Cz = surfParam.Cz;
Cxy = surfParam.Cxy; Cxx = surfParam.Cxx; Cyy = surfParam.Cyy;

dx = shiftParam.dx; dy = shiftParam.dy; dz = shiftParam.dz;
a_Rad = rotateParam.a_Rad;
kx = Ray.kX; ky = Ray.kY; kz = Ray.kZ;
x0 = Ray.x0; y0 = Ray.y0; z0 = Ray.z0;

%Cxx*X^2 + Cyy*Y^2 - Cz*Z == 0;
%  x = (x0 + kx*t);
%  y = (y0 + ky*t);
%  z = (z0 + kz*t);
 syms t Cxx Cyy ;
 parabola = - (...
               Cxx*((x0 + kx*t)-dx)^2 +...
            2*Cxy*((x0 + kx*t)-dx)*((y0 + ky*t)-dy) +...
            Cyy*((y0 + ky*t)-dy)^2 + Cx*((x0 + kx*t)-dx) +...
            Cy*((y0 + ky*t)-dy)...
                                )...
                                + Cz*dz - Cz*(z0+t*kz);
 coefT = coeffs(parabola,t)
 %parabola = Cxx*(Ray.x0+Ray.kX*t)^2 + Cyy*(Ray.y0+Ray.kY*t)^2 - Cz*(Ray.z0+Ray.kZ*t) == 0 ;
 T = vpasolve(parabola, t);
 x1 = (x0 + kx*T(2,1));
 y1 = (y0 + ky*T(2,1));
 z1 = (z0 + kz*T(2,1));
 RayOut = struct('x0', x0, 'y0', y0,'z0', z0,...
             'x', x1, 'y', y1, 'z', z1,...
             'kX', kx, 'kY', ky, 'kZ', kz); 
end

