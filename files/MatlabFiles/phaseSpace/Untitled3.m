clc; close all; clear all;
f1 = 1;
f2 = 3;
t = 0:f1/100:10/f1;
y1 = sin(2*pi*f1.*t);
y2 = sin(2*pi*f2.*t);
y3 = y1+y2;
figure (1)
plot(t,y1, t, y2)
figure (2)
plot(t,y3);

%%
close all
Fs = 1;
fc = 1;
Wn = (2/Fs)*fc;
b = fir1(3,0.5,'low');

y = filter(b,1,y3);
figure(3)
plot(t,y)