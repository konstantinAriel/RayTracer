function Test (Mr1, Mr2, Ray11, RefRay1, Ray22, RefRay2, ePolarRay, rPolarRay)
  Rin_1 =  [Ray11.kX Ray11.kY Ray11.kZ];
  
  Ref_1 =  [RefRay1.kX RefRay1.kY RefRay1.kZ];  
  Ein_1 =  [ePolarRay.kX ePolarRay.kY ePolarRay.kZ];	
  Eref_1 = [rPolarRay.kX rPolarRay.kY rPolarRay.kZ];
  Rin_2 =  [Ray22.kX Ray22.kY Ray22.kZ];
  Ref_2 =  [RefRay2.kX RefRay2.kY RefRay2.kZ];
  
  S =  [Ray11.X0 Ray11.Y0 Ray11.Z0];             % Source 1 
  M1 = [Ray11.X Ray11.Y Ray11.Z];                %  Mirror 1 - RefRay1(X0 Y0 Z0)
  M2 = [Ray22.X Ray22.Y Ray22.Z];                % Mirror 2  - RefRay2( X0 Y0 Z0)
  F =  [RefRay1.X RefRay1.Y RefRay1.Z];          % Focus 1 - Ray22 ( X0 Y0 Z0)
  R =  [RefRay2.X RefRay2.Y RefRay2.Z] ;         % Reciever 1 
  
  absRin_1 = sqrt(Rin_1*Rin_1');
  absRef_1 = sqrt(Ref_1*Ref_1');
  absEin_1 = sqrt(Ein_1*Ein_1');
  absEref_1 = sqrt(Eref_1*Eref_1');
  absRin_2 = sqrt(Rin_2*Rin_2');
  absRef_2 = sqrt(Ref_2*Ref_2');
  
  m1Y = ((Mr1.C.Cxx*(Ray11.X - Mr1.f.X).^2 + 2*Mr1.C.Cxz*(Ray11.X - Mr1.f.X).*(Ray11.Z - Mr1.f.Z) + Mr1.C.Czz*(Ray11.Z - Mr1.f.Z).^2 + Mr1.C.Cx.*(Ray11.X - Mr1.f.X) + Mr1.C.Cz.*(Ray11.Z - Mr1.f.Z)))...
		- (Ray11.Y - Mr1.f.Y);
  m2Y = ((Mr2.C.Cxx*(Ray22.X - Mr2.f.X).^2 + 2*Mr2.C.Cxz*(Ray22.X - Mr2.f.X).*(Ray22.Z - Mr2.f.Z) + Mr2.C.Czz*(Ray22.Z - Mr2.f.Z).^2 + Mr2.C.Cx.*(Ray22.X - Mr2.f.X) + Mr2.C.Cz.*(Ray22.Z - Mr2.f.Z)))...
		- (Ray22.Y - Mr2.f.Y);
		%disp '***********************************'
end

