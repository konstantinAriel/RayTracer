clc;
%a = [ - Cxx*kx^2 - 2*Cxy*kx*ky - Cyy*ky^2, 2*Cxx*kx*(dx - x0) - Cy*ky - Cz*kz - Cx*kx + 2*Cxy*ky*(dx - x0) + 2*Cxy*kx*(dy - y0) + 2*Cyy*ky*(dy - y0), Cz*dz - Cz*z0 + Cx*(dx - x0) + Cy*(dy - y0) - Cxx*(dx - x0)^2 - Cyy*(dy - y0)^2 - 2*Cxy*(dx - x0)*(dy - y0)]

%[ - Cxx*kx^2 - Cyy*(cs*ky + kz*sn)^2 - 2*Cxy*kx*(cs*ky + kz*sn), 2*Cxy*(dx - x0)*(cs*ky + kz*sn) - Cy*(cs*ky + kz*sn) - Cx*kx - 2*Cyy*(cs*ky + kz*sn)*(cs*y0 - dy + sn*z0) + 2*Cxx*kx*(dx - x0) - 2*Cxy*kx*(cs*y0 - dy + sn*z0), Cx*(dx - x0) - Cz*(Zr - dz) - Cy*(cs*y0 - dy + sn*z0) - Cxx*(dx - x0)^2 - Cyy*(cs*y0 - dy + sn*z0)^2 + 2*Cxy*(dx - x0)*(cs*y0 - dy + sn*z0)]

[ - Cxx*kx^2 - Cyy*(cs*ky + kz*sn)^2 - 2*Cxy*kx*(cs*ky + kz*sn), 2*Cxy*(dx - x0)*(cs*ky + kz*sn) - Cy*(cs*ky + kz*sn) - Cz*(cs*kz - ky*sn) - Cx*kx - 2*Cyy*(cs*ky + kz*sn)*(cs*y0 - dy + sn*z0) + 2*Cxx*kx*(dx - x0) - 2*Cxy*kx*(cs*y0 - dy + sn*z0), Cx*(dx - x0) - Cy*(cs*y0 - dy + sn*z0) - Cxx*(dx - x0)^2 - Cyy*(cs*y0 - dy + sn*z0)^2 + Cz*(dz - cs*z0 + sn*y0) + 2*Cxy*(dx - x0)*(cs*y0 - dy + sn*z0)]
