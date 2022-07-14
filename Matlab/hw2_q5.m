t = linspace(1,20,500);
x = 1 + cos(2*t);
y = -1 + 3*sin(4*t);


plot(t,x)
hold on
plot(t,y)

xlabel('t')
ylabel('x,y functions')
legend({'x function','y function'},'Location','southeast')