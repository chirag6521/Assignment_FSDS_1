#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ans.1
## The try-except block in python is used for exception handling.it protects the program from unexpected errors by catching and handling exceptions the try block contains the code that may raise an exception if an exception occurs the program flow transfers to the corresponding except block for handling the exception.
try:
    except:


# In[ ]:


#Ans.2
## In the try block, you place the code that may raise an exception. If an exception of the specified type occurs, the program flow transfers to the corresponding except block. The except block specifies the type of exception it can handle and contains the code to handle that specific exception. Multiple except blocks can be used for different exception types.


# In[ ]:


#Ans.3
## If an exception occurs inside a try block and there is no matching except block, the exception is not caught. It propagates up the call stack in search of an outer try-except block that can handle it. if no appropriate handler is found the program terminates and the unhandled exception's traceback is displayed.


# In[ ]:


#Ans.4
""""
Using a bare `except` block catches all exceptions, regardless of their type, potentially leading to unintended consequences or masking errors. 
Specifying a specific exception type allows for targeted handling and tailored exception specific logic. 
It provides better visibility and clarity in code as well as more precise error handling. 
It is generally recommended to avoid bare `except` blocks and instead specify the specific exception types to handle.
""""


# In[39]:


#Ans.5

try:
    print("Outer try block")
    
    try:
        print("Inner try block")
        num = int(input("Enter a number: "))  # May raise ValueError
        result = 1000 / num 
        print("Result:", result)
        
    except ValueError:
        print("Inner except block: Invalid input!")
        
    except ZeroDivisionError:
        print("Inner except block: Cannot divide by zero!")
        
    finally:
        print("Inner finally block")
        
except:
    print("Outer except block: Caught exception")
print("Program execution continues...")


# In[41]:


#Ans.6
try:
    x = 50 / 0 
    y = int('abc')
    z = some_undefined_variable  
except ZeroDivisionError:
    print("ZeroDivisionError occurred!")
except ValueError:
    print("ValueError occurred!")
except NameError:
    print("NameError occurred!")
except:
    print("An unknown error occurred!")


# In[ ]:


#Ans.7
""""
EOFError: Raised when attempting to read beyond the end of a file or input stream.
FloatingPointError: Raised when a floating-point operation fails, such as division by zero.
IndexErro: Raised when trying to access an index outside the valid range of a sequence.
MemoryError: Raised when the program runs out of available memory for object allocation.
OverflowError: Raised when a calculation exceeds the maximum limit for a numeric type.
TabError: Raised when indentation errors occur due to inconsistent use of tabs and spaces.
ValueError: Raised when a function receives an argument of the correct type but with an invalid value.
""""


# In[42]:


#Ans.8
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# In[45]:


try:
    num_str = input("Enter a number: ")
    num = int(num_str)
    print("Number:", num)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


# In[47]:


try:
    my_list = [1, 2, 3, 4, 5]
    index = int(input("Enter an index: "))
    element = my_list[index]
    print("Element at index", index, ":", element)
except IndexError:
    print("Error: Index is out of range.")


# In[50]:


try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative numbers not allowed")
    else:
        print("Number:", num)
except ValueError as ve:
    print("ValueError:", ve)


# In[52]:


try:
    num = int(input("Enter a number: "))
    result = 1100 * num
    print("Result:", result)
except Exception as e:
    print("An error occurred:", e)


# In[ ]:





# In[ ]:





# In[ ]:




