function [ shiftingSurf ] = ShiftMir (dX, dY, dZ, MirIN)
  MirIN.X = MirIN.X + dX;
  MirIN.Y = MirIN.Y + dY;    
  MirIN.Z = MirIN.Z + dZ;
  shiftingSurf = struct('X',MirIN.X ,'Y',MirIN.Y , 'Z', MirIN.Z);
end

