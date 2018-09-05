function [Xin, Kin, Xout, Kout] = ChekedABCDE_Matrix( Ray_S_1, RefRay_1_2, Ray_1_2, RefRay_2_3, S)

    iR =  [1 2 2 3 3 ];
    iC = [2 1 3 2 3];
    for i = 1:5
        Xin(1,i) = Ray_S_1(iR(1,i), iC(1,i)).X0;
        Xin(2,i) = Ray_S_1(iR(1,i), iC(1,i)).Y0;
        Xin(3,i) = Ray_S_1(iR(1,i), iC(1,i)).Z0;
        
        Kin(1,i) = Ray_S_1(iR(1,i), iC(1,i)).kX;
        Kin(2,i) = Ray_S_1(iR(1,i), iC(1,i)).kY;
        Kin(3,i) = Ray_S_1(iR(1,i), iC(1,i)).kZ;
        
        Xout(1,i) = S(3,1) - RefRay_2_3(iR(1,i), iC(1,i)).X;
        Xout(2,i) = S(3,2) - RefRay_2_3(iR(1,i), iC(1,i)).Y;
        Xout(3,i) = S(3,3) - RefRay_2_3(iR(1,i), iC(1,i)).Z;
        
        Kout(1,i) = RefRay_2_3(iR(1,i), iC(1,i)).kX;
        Kout(2,i) = RefRay_2_3(iR(1,i), iC(1,i)).kY;
        Kout(3,i) = RefRay_2_3(iR(1,i), iC(1,i)).kZ;
    end
end

