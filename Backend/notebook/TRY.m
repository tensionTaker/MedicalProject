Gp_num = [10 4];
Gp_dem = [1 4 4 0];
Gp = tf(Gp_num, Gp_dem);

t = 0:0.02:10;

DataOut = step(Gp_num, Gp_dem,t);

plot(t, t, "--", t, DataOut)
%v = [0 10 0 10]; axis(v); 
grid

%Gc = tf([9.33*1 1.15*9.33],[1 4.3])


%controlSystemDesigner()







