% From https://www.mathworks.com/help/stats/f-statistic-and-t-statistic.html

x=[7 7 7 7 7 5 5 5 5 5 3 3 3 3 3];
y=[7.12 6.63 6.78 6.83 6.93 6.45 6.33 6.67 6.62 6.73 6.61 6.35 6.80 6.56 6.45];

t=fitlm(pH,wear);
anova(t, 'summary');

