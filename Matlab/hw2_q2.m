A = [1 1 1 ; 1 2 3 ; 1 3 6];
b = [1 ; -5 ; 2];

disp(A)
disp(b)

x1 = A\b;
disp(x1)

x2 = inv(A)*b;
disp(x2)

s = det(A);
disp(s)

y = rank(A);
disp(y)
