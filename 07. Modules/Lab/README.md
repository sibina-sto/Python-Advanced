## **01.	Calculate Logarithm -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/13.%20Modules%20-%20Lab/01_calculate_logarithm.py)
Write a program that prints the calculated logarithm of any given number  

*Input*  
•	On the first line you will receive the number (an integer)  
•	On the second line you will receive a number, which is the base of the logarithm. It can be either a number or the word "natural"

The output should be formatted to the 2nd decimal digit

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|10<br>natural          |2.30          |
|10<br>10                  |1.00                 |




## **02.	ASCII Art -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/13.%20Modules%20-%20Lab/02_ascii_art.py)
Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word. Use the pyfiglet module. You can read more about it here - https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/

*Directions*  
1.	First you need to install the module that we will be using. To install it go to Setting --> Project <your_project_name> --> Project Interpreter --> + --> search for pyfiglet --> install package.   
2.	Import the module  
3.	Implement the logic. We will be using the figlet_format method  




## **03.	Triangle -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/13.%20Modules%20-%20Lab/03_triangle.py), [Package](https://github.com/elenaborisova/Python-Advanced/tree/main/13.%20Modules%20-%20Lab/triangle_print)
Create a module for printing a triangle. You will receive an integer number which is the size of the triangle.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|3          |1<br>1 2<br>1 2 3<br>1 2<br>1     |
|4                  |1<br>1 2<br>1 2 3<br>1 2 3 4<br>1 2 3<br>1 2<br>1                  |




## **04.	Mathematical operations -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/13.%20Modules%20-%20Lab/04_mathematical_operations.py), [Package](https://github.com/elenaborisova/Python-Advanced/tree/main/13.%20Modules%20-%20Lab/math_operations)
Create a module that does basic calculations. You will receive 2 numbers and a sign between them all in one string

*Input*  
You will receive a single string in the following format  
"{number1} {sign} {number2}"  
o	number1 - a float number in the range (0.0, 1000.0)  
o	sign - a char that can be  
'/' - divide the first number with the second  
'*' - multiply the 2 numbers  
'-' - subtract the first number with the second  
'+' - add the 2 numbers  
'^' - raise the first number to the second  
o	number2 - an integer number in the range (0, 1000)

*Output*  
Print only the result of the operation  
The result should be formatted to the second decimal point  

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|2.5 * 2          |5.00          |
|6.66 ^ 2                  |44.35                  |
|36.66 / 6                |6.11    |




## **05.	Fibonacci Sequence -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/13.%20Modules%20-%20Lab/05_fibonacci_sequence.py), [Package](https://github.com/elenaborisova/Python-Advanced/tree/main/13.%20Modules%20-%20Lab/tribonacci_sequence)
Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence) and print them, separating them with a single space. The module should also be able to locate a specific number in the sequence.  You can read more about the Fibonacci sequence here: https://en.wikipedia.org/wiki/Fibonacci_number

You will be receiving commands until the "Stop" command. The commands are:  
•	"Create Sequence {count}". Create series of numbers up to a specific count and print them in the following format:  
           "{n1} {n2} … {n}"  

•	"Locate {number}"

Check if the sequence contains the number. If, it finds the number it should print:  
"The number - {number} is at index {index}"  
And if it doesn't find it:  
"The number {number} is not in the sequence"

*Input*  
•	You will be receiving commands until the "Stop" command.  All inputs will be valid.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|Create Sequence 10<br>Locate 13<br>Create Sequence 3<br>Locate 10<br>Stop          |0 1 1 2 3 5 8 13 21 34<br>The number - 13 is at index 7<br>0 1 1<br>The number 10 is not in the sequence          |

