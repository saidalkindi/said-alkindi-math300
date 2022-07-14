%variables
l = 10; %length of interval
N = 10; %number of space steps

h = l/N;
f(1) = 0;
f = zeros(1,N+1);

%code
for n = l:N
    f(n+1) = f(n) + h*(n^2 + n + 1);
end

x = linspace(0,l,N+1);
plot(x,f);



