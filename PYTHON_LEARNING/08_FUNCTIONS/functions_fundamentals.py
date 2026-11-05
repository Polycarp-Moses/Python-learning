#CHAPTER 8: FUNCTIONS
# A function is a small resubable block of code that does one specific job
#Its like a machine that can take an input and return something back/output.

#Why functions? 
# -In projects you write python codes (logic) to solve problems. In big projects, you find that you copy and paste these logics over and over, multiple times throughout your code. This creates a problem in case there is a bug or requirements change; making changes to this repeated logic becomes a problem. 
# -To solve this problem, we use functions. Instead of repeating your logic over and over, you take it and put it in a function. So whenever you need to use the logic in your code, you simply CALL the function.
#Benefits: if there is bug or requirements change, you just go to your function and change it only once, which automatically updates all other areas where you have called the function. So changes become easy, faster and safer. Your code also becomes smaller and readable. Collaborations in projects also become easier where one person can work on the functions while the other works on the rest of the code. Functions also introduce code modularity, which means breaking big, complex projects into smaller manageable pieces. 

#Sources of functions:
#1. Built in functions - print(), len(), str(), input(), type(), bool(), etc
#2. Standard library - written by python team. You must import their module in order to use them. Modules: math, datetime, random etc
#3. External library- written by the community, eg, developers or companies. To use them you must install the external library and import the functions. Examples of external libraries are Pandas-which does data cleaning and analysis, Matplotlib- which does data visualizations, Numpy- which works on numbers and arrays. 
#4. User-defined functions - written by you. Here you define the function yourself and then use it.

#How to choose between sources: 
# GOLDEN RULE - before writing any new code like a function from scratch, always check if it already exists. So don't reinvent the wheel. First check the bulit in functions, then check the libraries; if the don's exist, use user defined functions. 