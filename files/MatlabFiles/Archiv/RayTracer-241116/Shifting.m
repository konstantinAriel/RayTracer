function [ shiftingSurf ] = Shifting (dX, dY, dZ, rotatedSurf)
  rotatedSurf.X = rotatedSurf.X + dX;
  rotatedSurf.Y = rotatedSurf.Y + dY;    
  rotatedSurf.Z = rotatedSurf.Z + dZ;
  shiftingSurf = struct('X',rotatedSurf.X ,'Y',rotatedSurf.Y , 'Z', rotatedSurf.Z)
end

