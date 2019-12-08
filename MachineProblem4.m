% User inputs
h0=input('Enter initial height:');
v=input('Enter magnitude of velocity:');
angle=input('Enter angle in degrees:');
ax=input('Enter x-component of the acceleration (with sign):');
ay=input('Enter y-component of the acceleration (with sign):');

%Error if y acceleration is 0 
if (ay==0)
    error('Error. Acceleration value must not be 0');
end

%get velocity x and y components
voy=v*sin(angle*(pi/180));
vox=v*cos(angle*(pi/180));

%compute for data
tpk=-voy/ay;% peak time for highest point
ytotal=h0+voy*tpk+(1/2)*ay*tpk^2; % total distance traveled in the y-axis
tdown=sqrt(2*ytotal/abs(ay)); %time from peak to ground
t_total=tpk+tdown; % total time of travel
s_horizontal=vox*t_total+(1/2)*ax*t_total; % total x distance traveled


t=linspace(0,t_total,10000);%create vector for x axis
y=h0+voy.*t+(1/2)*ay*t.^2;% substitute to get y-values at a specific time(t)

if (vox>0 && ax>=0)
    x=linspace(0,s_horizontal,10000);
elseif (vox <0 && ax<=0) %flip if ax is negative(to the left)
    x=linspace(s_horizontal,0,10000);
    y=flip(y);
end

plot(x,y);title('Projectile Trajectory');
xlabel('{\it Range (meters)}');
ylabel('{\it Height (meters)}');
grid on;
grid minor;