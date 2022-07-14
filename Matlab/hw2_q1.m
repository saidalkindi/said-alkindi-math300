A = [2 -1 4 ; 9 6 2 ; 1 3 8];
B = ones(3,3);
x = [3 ; 6 ; 8];
y = [5 10 15];

disp(A)
disp(B)
disp(x)
disp(y)

s1 = A * B;
disp(s1)

s2 = A * x;
disp(s2)

s3 = x' * B;
disp(s3)

%s4 = B * y;
%disp(s4)

%s5 = x * A;
%disp(s5)

s6 = x * y;
disp(s6)

s7 = y * x;
disp(s7)

%s8 = x * y';
%disp(s8)

s9 = x .* y;
disp(s9)

s10 = A .* B;
disp(s10)
