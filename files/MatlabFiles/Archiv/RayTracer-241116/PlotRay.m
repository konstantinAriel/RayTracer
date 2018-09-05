function rIn = PlotRay( rOut,L )
   M = zeros(4,4);
   M(1:2,1:2) = [1 L; 0 1];
   M(3:4, 3:4) = [1 L; 0 1];
	rIn =  M*rOut;
end

