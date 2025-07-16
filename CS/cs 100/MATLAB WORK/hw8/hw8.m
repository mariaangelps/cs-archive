
%Maria Angel Palacios 

%Create a program to determine test grades based on the score and 
%assuming a single input. 
%The grades should be based on the following criteria.

 A=90:1:100;
 B=80:1:89;
 C=70:1:79;
 D=60:1:69;
 E=0:1:59;
  
grade= input('Enter your score=')

%Create a condition for each grade using the 
%command if, elseif.

if grade>=90 & grade<=100 
disp('Your  Score is A.')

elseif grade>=80 &grade<=89
    disp("Your Score is B")

elseif grade>=70 &grade<=79
    disp("Your Score is C")

elseif grade>=60 &grade<=69
    disp("Your Score is D")


elseif grade<60
    disp("Your Score is E")

end




   