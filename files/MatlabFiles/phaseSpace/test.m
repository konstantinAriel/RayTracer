clc
close all
clear all

% dimensions of waveguide
aa = 30; % horizontal
bb = 15; % vertical

% number of steps
h = 2*aa;

% step size
dx = aa/h;
dy = aa/h;

x = 0:dx:aa-1;
y = 0:dy:bb-1;

Lx = length(x);
Ly = length(y);


% Generating sparsh matrix A
A = zeros(Ly*Lx,Ly*Lx);

for l = 1: Ly*Lx
    
    
    %% for corners
    if l == 1
        A(l,l) = 4;
        A(l,l+1) = -2;
        A(l,l+Lx) = -2;        
    end
    
    if l == Lx
        A(l,l) = 4;
        A(l,l-1) = -2;
        A(l,l+Lx) = -2;        
    end
    
    if l == 1+Lx*(Ly-1)
        A(l,l) = 4;
        A(l,l-Lx) = -2;
        A(l,l+1) = -2;        
    end
    
    if l == Lx*Ly
        A(l,l) = 4;
        A(l,l-1) = -2;
        A(l,l-Lx) = -2;        
    end
    
    %% for edges
    
    if l>1 && l<Lx    % Bottom edge
        A(l,l) = 4;
        A(l,l-1) = -1;
        A(l,l+1) = -1;
        A(l,l+Lx) = -2;
    end
    
      
     if l>1+Lx*(Ly-1) && l<Lx*Ly     % Top edge
        A(l,l) = 4;
        A(l,l-1) = -1;
        A(l,l+1) = -1;
        A(l,l-Lx) = -2;
     end
    
     a1 = 1+Lx:Lx:Lx*(Ly-2)+1; % Right edge
      if find(a1 == l) ~= 0
        A(l,l) = 4;
        A(l,l+1) = -2;
        A(l,l-Lx) = -1;
        A(l,l+Lx) = -1;
     end
     
     a2 = 2*Lx:Lx:Lx*(Ly-1); % Left edge
      if find(a2 == l) ~= 0
        A(l,l) = 4;
        A(l,l-1) = -2;
        A(l,l-Lx) = -1;
        A(l,l+Lx) = -1;
      end
     
     
      %% for all other points
      a3 = [1:Lx 1+Lx*(Ly-1):Lx*Ly a1 a2 ]; % defining edges
      
      b = (find(a3 == l) ~= 0);
      if b == 1
          c = 0;
      else c = 1;
      end
      
      if c == 1
         A(l,l) = 4;
         A(l,l-1) = -1;
         A(l,l+1) = -1;
         A(l,l+Lx) = -1;  
         A(l,l-Lx) = -1;  
      end
      
end


[phi,lam] = eig(A); % Calculating eigen value and eigen vector of A
hz = zeros(Ly,Lx); % initailising 
Hz = zeros(Ly,Lx,Lx*Ly); % intialising magnetic field vector for every eigen value
kc = zeros(1,Lx*Ly); % intialising propagation constant vector

for m = 1:Lx*Ly 
    
    Lam(m) = lam(m,m); % eigen values
    kc(m) = sqrt(Lam(m))/dx; % finding propagation constant vector
    Phi = phi(:,m); % assigning field corresponding to every propagation mode
    
    % converting column matrix of corresponding field to 2-D field matrix
    p = 1;
    for n = 1:Lx:Lx*(Ly-1)+1
    hz(p,:) = Phi(n:n+Lx-1);
    p = p+1;
    end
    
    Hz(:,:,m) = hz; % storing field matrix of every mode   
   end

%  surf(x,y,Hz(:,:,2)) % plotting H field

 
 %% finding Ex and Ey for each mode, using  Ex = -j*w*mu/Kc^2 dHz/dy, Ey = j*w*mu/Kc^2 dHz/dx
 %% Normalising Ex and Ey for each mode, using  Ex = (-j*w*mu/Kc^2 dHz/dy)*sqrt(epsilon/mu), Ey = (j*w*mu/Kc^2 dHz/dx)*sqrt(epsilon/mu)
 
 Lm = min(aa,bb)/6; % defining wavelength
 K  = 2*pi/Lm; % defining wave number
%  KK = K./(kc.^2); % w/c*Kc^2 for normailsed E-field
KK = 1/K;
 
 Exx = zeros(Ly,Lx); % initialising Ex field
 Eyy = zeros(Ly,Lx); % initialising Ey field
 
 for m = 1: Lx*Ly % for every mode
     H = Hz(:,:,m);
 for ll = 2:Ly-1
     for mm = 2:Lx-1
     Exx(ll,mm) = -1*KK*(H(ll+1,mm)-H(ll,mm)); % calculating Ex field 
     
     Eyy(ll,mm) = KK*(H(ll,mm+1)-H(ll,mm)); % calculating Ey field 
     end    
 end
 Ex(:,:,m) = Exx;
 Ey(:,:,m) = Eyy;
 E(:,:,m) = sqrt((Exx.^2)+(Eyy.^2)); % Calculting E-field
 MaxE = max(max(E(:,:,m)));
 En(:,:,m) = E(:,:,m)/MaxE; % normalised w.r.t  maximum value
 end
  
modes = zeros(Lx*Ly,3);
kc_th = zeros(1,Lx*Ly); % intialsing theoretical value of Kc, propagation constant
 for q = 1:Lx*Ly
     [M,N]= modefinders(En(:,:,q),Lx,Ly);
     modes(q,1) = M ; 
     modes(q,2) = N ; 
     modes(q,3) = q ; % position of eigenvalue
     kc_th(q) = pi*(sqrt(((M/aa)^2)+((N/bb)^2)));
 end
 
 
 
 
a11 = 0; a22 = 0; a33 = 0; a44 =0; a55 = 0; a66 = 0;
a77 = 0; a88 = 0; a99 = 0; a100 =0; 
 % plotting modes
 for s = 1:Lx*Ly
     
     % for 10 mode
     if (modes(s,1)== 1) &&  (modes(s,2)== 0) 
         a11 = a11+1;
       p10(a11) = modes(s,3);
       k10(a11) = kc(p10(a11));
     end
     
     % for 01 mode
     if (modes(s,1)== 0) &&  (modes(s,2)== 1) 
         a22 = a22+1;
       p01(a22) = modes(s,3);
       k01(a22) = kc(p01(a22));
       
     end
     
     % for 11 mode
     if (modes(s,1)== 1) &&  (modes(s,2)== 1) 
         a33 = a33+1;
         p11(a33) = modes(s,3);
       k11(a33) = kc(p11(a33));
             
     end
     
     % for 20 mode
     if (modes(s,1)== 2) &&  (modes(s,2)== 0) 
         a44 = a44+1;
       p20(a44) = modes(s,3);
       k20(a44) = kc(p20(a44));
              
     end
     
     % for 02 mode
     if (modes(s,1)== 0) &&  (modes(s,2)== 2) 
         a55 = a55+1;
       p02(a55) = modes(s,3);
       k02(a55) = kc(p02(a55));
             
     end
     
     % for 21 mode
     if (modes(s,1)== 2) &&  (modes(s,2)== 1) 
         a66 = a66+1;
       p21(a66) = modes(s,3);
       k21(a66) = kc(p21(a66));
              
     end
     
     % for 12 mode
     if (modes(s,1)== 1) &&  (modes(s,2)== 2) 
         a77 = a77+1;
       p12(a77) = modes(s,3);
       k12(a77) = kc(p12(a77));
             
     end
     
     % for 22 mode
     if (modes(s,1)== 2) &&  (modes(s,2)== 2) 
         a88 = a88+1;
       p22(a88) = modes(s,3);
       k22(a88) = kc(p22(a88));
             
     end
     
     % for 30 mode
       if (modes(s,1)== 3) &&  (modes(s,2)== 0) 
           a99 = a99+1;
       p30(a99) = modes(s,3);
       k30(a99) = kc(p30(a99));
      
       end
     
     % for 03 mode
     if (modes(s,1)== 0) &&  (modes(s,2)== 3) 
         a100 = a100+1;
       p03(a100) = modes(s,3);
       k03(a100) = kc(p03(a100));
              
     end
     
 end
 
 % for 10 mode 
 K10 = min(k10); % dominent mode by Eigen value
 l10 = find(k10 == K10); 
 P10 = p10(l10);% location of dominent mode
 K10_th = kc_th(P10); % theoretical value
 surf(x,y,En(:,:,P10))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE10 mode')
 goodplot()
 figure
 
 % for 01 mode 
 K01 = min(k01); % dominent mode
 l01 = find(k01 == K01); 
 P01 = p01(l01);% location of dominent mode
 K01_th = kc_th(P01);
 surf(x,y,En(:,:,P01))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE01 mode')
 goodplot()
 figure
 
 % for 11 mode 
 K11 = min(k11); % dominent mode
 l11 = find(k11 == K11); 
 P11 = p11(l11);% location of dominent mode
 K11_th = kc_th(P11);
 surf(x,y,En(:,:,P11))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE11 mode')
 goodplot()
 figure
 
 % for 20 mode 
 K20 = min(k20); % dominent mode
 l20 = find(k20 == K20); 
 P20 = p20(l20);% location of dominent mode
 K20_th = kc_th(P20);
 surf(x,y,En(:,:,P20))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE20 mode')
 goodplot()
 figure
 
 % for 02 mode 
 K02 = min(k02); % dominent mode
 l02 = find(k02 == K02); 
 P02 = p02(l02);% location of dominent mode
 K02_th = kc_th(P02);
 surf(x,y,En(:,:,P02))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE02 mode')
 goodplot()
 figure
 
  % for 21 mode 
 K21 = min(k21); % dominent mode
 l21 = find(k21 == K21); 
 P21 = p21(l21);% location of dominent mode
 K21_th = kc_th(P21);
 surf(x,y,En(:,:,P21))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE21 mode')
 goodplot()
 figure
 
 % for 12 mode 
 K12 = min(k12); % dominent mode
 l12 = find(k12 == K12); 
 P12 = p12(l12);% location of dominent mode
 K12_th = kc_th(P12);
 surf(x,y,En(:,:,P12))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE12 mode')
 goodplot()
 figure
 
 % for 22 mode 
 K22 = min(k22); % dominent mode
 l22 = find(k22 == K22); 
 P22 = p22(l22);% location of dominent mode
 K22_th = kc_th(P22);
 surf(x,y,En(:,:,P22))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE22 mode')
 goodplot()
 figure
 
 % for 30 mode 
 K30 = min(k30); % dominent mode
 l30 = find(k30 == K30); 
 P30 = p30(l30);% location of dominent mode
 K30_th = kc_th(P30);
 surf(x,y,En(:,:,P30))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE30 mode')
 goodplot()
 figure
 
 % for 03 mode 
 K03 = min(k03); % dominent mode
 l03 = find(k03 == K03); 
 P03 = p03(l03);% location of dominent mode
 K03_th = kc_th(P03);
 surf(x,y,En(:,:,P03))
 xlabel('x \rightarrow')
 ylabel('\leftarrow y ')
 zlabel('Normalized Electric field \rightarrow')
 title('Electric field Distribution for TE03 mode')
 goodplot()
