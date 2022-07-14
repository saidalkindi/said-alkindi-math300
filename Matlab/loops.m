n = 100;
sum = 0; 

for i = 1:n
    sum(i+1) = sum(i) + sin(i/n)*(1/n);
end 