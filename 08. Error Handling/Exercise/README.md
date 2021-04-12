## **01. Numbers Dictionary -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/17.%20Error%20Handling%20-%20Exercise/01_numbers_dictionary.py)
You are provided with the following code:

    numbers_dictionary = {}
    
    line = input()
    
    while line != "Search":
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    
    line = input()
    
    while line != "Remove":
        searched = line
        print(numbers_dictionary[searched])
        
    line = input()
    
    while line != "End":
        searched = line
        del numbers_dictionary[searched]
    
    print(numbers_dictionary)


•	On the first several lines, until you receive the command "Search", you will receive on separate lines the number as text and the number as integer  
•	When you receive "Search" on the next several lines until you receive the command "Remove", you will be given the searched number as text and you need to print it on the console  
•	When you receive "Remove" on the next several lines until you receive "End" you will be given the searched number as text and you need to remove it from the dictionary  
•	At the end you need to print what is left from the dictionary  

There is some missing code in the solution and there are some errors that may occur. Complete the code so the following errors are handled:  
•	Passing non-integer type to the variable number  
•	Searching for a non-existent number  
•	Removing a non-existent number  

Print appropriate messages when an error has occurred. The messages should be:  
•	"The variable number must be an integer"  
•	"Number does not exist in dictionary" - for non-existing keys  

*Note:* Use ONE try and many except statements for the different errors that may occur  

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|one<br>1<br>two<br>2<br>Search<br>one<br>Remove<br>two<br>End  |1<br>{'one': 1}         |
|one<br>two<br>Search<br>Remove<br>End                  |The variable number must be an integer<br>{}                  |
|one<br>1<br>Search<br>one<br>Remove<br>two<br>End      |1<br>Number does not exist in dictionary<br>{'one': 1}        | 



## **02. Email Validator -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/17.%20Error%20Handling%20-%20Exercise/02_email_validator.py)
You will be given some emails until you receive the command "End". Create the following custom exceptions to validate the emails:  
•	NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")  
•	MustContainAtSymbolError - raise it when there is no "@" in the email  
•	InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)

When an error is encountered, raise it with an appropriate message:  
•	NameTooShortError - "Name must be more than 4 characters"  
•	MustContainAtSymbolError - "Email must contain @"  
•	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"

*Hint:* use the following syntax to add message to the Exception: MyException("Exception Message")

If the current email is valid, print "Email is valid" and read the next one

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|abc@abv.bg          |Traceback (most recent call last):<br>  File ".\email_validator.py", line 20, in <module><br>    raise NameTooShort("Name must be more than 4 characters")<br>__main__.NameTooShort: Name must be more than 4 characters     |
|peter@gmail.com<br>petergmail.com                  |Email is valid<br>Traceback (most recent call last):<br>  File ".\email_validator.py", line 18, in <module><br>    raise MustContainAtSymbolError("Email must contain @")<br>__main__.MustContainAtSymbolError: Email must contain @     |
|peter@gmail.hotmail    |Traceback (most recent call last):<br>  File ".\email_validator.py", line 22, in <module><br>    raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")<br>__main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net     | 
