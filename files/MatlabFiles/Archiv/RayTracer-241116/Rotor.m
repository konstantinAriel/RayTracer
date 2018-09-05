function [ c ] = Rotor (i1 , i2)
  i1X = i1(1,1);
  i1Y = i1(1,2);
  i1Z = i1(1,3);
  i2X = i2(1,1);
  i2Y = i2(1,2);
  i2Z = i2(1,3);
  
    c(1,1) =  ((i1Y*i2Z) - (i1Z*i2Y));
    c(1,2) = -((i1X*i2Z) - (i1Z*i2X));
    c(1,3) =  ((i1X*i2Y) - (i1Y*i2X));
      
end

