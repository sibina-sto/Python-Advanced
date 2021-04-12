## **01. So Many Exceptions -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/16.%20Error%20Handling%20-%20Lab/01_so_many_exceptions.py)
You are provided with the following code:

    numbers_list = input().split(", ")
    result = 0    
    for i in range(numbers_list):
        number = numbers_list[i + 1]
        if number < 5:
            result *= number
        elif number > 5 and number > 10:
            result /= number
    print(result)
    
This code raises many errors. Your job is to fix them.   
 
*Input:*
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

*Output:*
0.003968253968253968



## **02. Value cannot be Negative -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/16.%20Error%20Handling%20-%20Lab/02_value_cannot_be_negative.py)
Create your own exception called ValueCannotBeNegative. Write a program that reads five numbers from the console (on seperate lines). If a negative number occurs, raise the exception.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|1<br>4<br>-5<br>3<br>10          |Traceback (most recent call last):<br>&nbsp;File ".\value_cannot_be_negative.py", line 8, in<module><br>&nbsp;&nbsp; raiseValueCannotBeNegative<br>__main__.ValueCannotBeNegative          |



## **03. Repeat Text -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/16.%20Error%20Handling%20-%20Lab/03_repeat_text.py)
Write a program that receives text on the first line and times (to repeat the text) that must be an integer. If the user passes non-integer type for the times variable, handle the exception and print a message "Variable times must be an integer".

|       Input       |      Output       |
|-------------------|-------------------|
|Hello<br>Bye          |Variable times must be an integer    |
|Hello<br>2            |HelloHello | 
