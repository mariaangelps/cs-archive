
%Maria Angel Palacios

%Question2:
%Create a program that prompts the user to enter his or her year in school 
%Freshman, sophomore, junior or senior. 
%The input will be a string. 
%Monday for freshmen, Tuesday for sophomores, Wednesday for juniors and Thursday for seniors.
x1= menu ("Final Exams Dates", ...
    ["Freshman","Sophomores","Juniors","Seniors"])

switch x1
    case 1
    fprintf("For Freshman students, the exam will be held on Monday.")
    case 2
    fprintf("For Sophomores students, the exam will be held on Tuesday.")
    case 3
    fprintf("For Juniors, the exam will be held on Wednesday.")        
    otherwise
    fprintf("Seniors will be having the exam on Thursday.")

end