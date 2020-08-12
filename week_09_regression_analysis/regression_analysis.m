% By
% ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
% ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
%    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
%    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
%    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
%    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

% Email: ttuan.ho@outlook.com                                                         


% Following week 9 lecture 


% ========================
%  get regression analyssi summary
% ========================
lm=fitlm(x,y)

% ========================
% Check the assumptions
% ========================
plotResiduals(lm,'fitted')

% ========================
% Get 95% CI
% ========================
coefCI

% ========================
% Get 99% CI
% ========================
% tCrit %
t=tinv(0.995, 18) % 18 is the # error degree of freedom

% %
slope + se * tCrit * [-1 1]
% where slope is in the row 'x1', column 'estimate'  of fitlm %
% where se is in the row 'x1', column 'se' of fitlm %
