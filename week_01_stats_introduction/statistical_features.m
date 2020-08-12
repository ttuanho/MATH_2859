A = [9, 6, 29, 79, 98, 12, 43, 52, 56, 51, 45, 81, 63, 45, 26, 57, 100, 90, 43, 44, 50, 7, 44, 2, 88, 29, 48, 33, 80, 98, 90, 29, 75, 95, 85, 15, 97, 92, 96, 63];
V = var(A);
S = std(A);
M = mean(A);
Med = median(A);
Y = prctile(A,[0 25 50 75 100]); %{ five number summary%}
%{interquartile range%}
I = Y(4)-Y(2)
%{minimum to be outlier%}
Y(2)-1.5*I
%{maximum to be outlier%}
Y(4)+1.5*I
