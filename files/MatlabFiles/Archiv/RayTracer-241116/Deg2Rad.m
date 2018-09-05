function   a_Rad = Deg2Rad(a_Deg )
    [~,y] = size(a_Deg);
    a_Rad = zeros(1,y);
    for i=1:y
   a_Rad(1,i) = a_Deg(1,i)*pi/180;
    end
end

