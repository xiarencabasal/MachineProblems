p1=input('Input point 1 in [x y] form:');
p2=input('Input point 2 in [x y] form:');
p3=input('Input point 3 in [x y] form:');

A=[p1(1) p1(2) 1; p2(1) p2(2) 1; p3(1) p3(2) 1]; %coefficients of x and y
B=[-(p1(1)^2+p1(2)^2); -(p2(1)^2+p2(2)^2); -(p3(1)^2+p3(2)^2)]; %constants at right hand side
C=inv(A)*B; %solution to equations A*[x y]=b; [x y]=b*A^-1;

D=C(1);
E=C(2);
F=C(3);
h=-D/2;k=-E/2; %formula to get h, k values
radius=sqrt((D^2+E^2-4*F)/(4)); % formula to get radius

coefficientsDEF=[D E F]
centerhk=[h k]
radius

%fprintf('D=%f\t',D);
%fprintf('E=%f\t\t',E);
%fprintf('F=%f\n',F);
%fprintf('h=%f\t\t',h);
%fprintf('k=%f\n',k);
%fprintf('r=%f\n',r);