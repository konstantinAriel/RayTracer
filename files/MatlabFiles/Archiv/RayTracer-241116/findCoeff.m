clc;
syms t Cxx Czz Cxz Cx Cy Cz dx dy dz kx ky kz x0 y0 z0 X Y Z Yr Zr cs sn;
 parabola = (...
               Cxx*(x0 + dx + kx*t)^2 +...
            2*Cxz*(x0 + dx + kx*t)*(z0 + dz + kz*t) +...
            Czz*(z0 + dz + kz*t)^2 + Cx*(x0 + dx + kx*t) +...
            Cz*(z0 + dz + kz*t)...
                                )...
          - Cy*(y0+ dy + ky*t);
% X = (x0 + kx*t);
% Y = (y0 + ky*t);
% Z = (z0 + kz*t);
% Yr = Y*cs + Z*sn;
% Zr = Z*cs - Y*sn;
% parabola = - (...
%                Cxx*(X-dx)^2 +...
%             2*Cxy*(X-dx)*(Yr-dy) +...
%             Cyy*(Yr-dy)^2 + Cx*(X-dx) +...
%             Cy*(Yr-dy))-Cz*(Zr-dz);
 [coefT, aaa] = coeffs(parabola,t)
% [a, b] = solve(parabola,Zr)