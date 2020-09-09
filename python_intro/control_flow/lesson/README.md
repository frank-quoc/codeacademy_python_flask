# Control Flow 

Great job! We covered a ton of material in this lesson and you’ve increased the number of tools in your Python toolkit by several-fold. Let’s review what you’ve learned this lesson:

  - Boolean expressions are statements that can be either ```True``` or ```False```
  - A boolean variable is a variable that is set to either ```True``` or ```False```.
  - You can create boolean expressions using relational operators:
    * Equals: ```==```
    * Not equals: ```!=```
    * Greater than: ```>```
    * Greater than or equal to: ```>=```
    * Less than: ```<```
    * Less than or equal to: ```<=```
  - ```if``` statements can be used to create control flow in your code.
  - ```else``` statements can be used to execute code when the conditions of an ```if``` statement are not met.
  - ```elif``` statements can be used to build additional checks into your ```if``` statements
  - ```try``` and ```except``` statements can be used to build error control into your code.
Let’s put these skills to the test!

1. The admissions office at Calvin Coolidge’s Cool College has heard about your programming prowess and wants to get a piece of it for themselves. They’ve been inundated with applications and need a way to automate the filtering process. They collect three pieces of information for each applicant:
  i. Their high school GPA, on a 0.0 - 4.0 scale.
  ii. Their personal statement, which is given a score on a 1 - 100 scale.
  iii. The number of extracurricular activities they participate in.
<br />The admissions office has a cutoff point for each category. They want students that have a GPA of 3.0 or higher, a personal statement with a score of 90 or higher, and who participated in 3 or more extracurricular activities.<br />
<br />Write a function called ```applicant_selector``` which takes three inputs, ```gpa```, ```ps_score```, and ```ec_count```. If the applicant meets the cutoff point for all three categories, have the function return the string:<br />
<br />```"This applicant should be accepted."```<br />

2. Great! The admissions office also wants to give students who have a high GPA and a strong personal statement a chance even if they don’t participate in enough extracurricular activities.
<br />If an applicant meets the cutoff point for GPA and personal statement score, but not the extracurricular activity count, the function should return the string:<br />
<br />```"This applicant should be given an in-person interview."```<br />

3. Finally, for all other cases, the function should return the string:
<br />```"This applicant should be rejected."```<br />

## [Answer](answer.py)
