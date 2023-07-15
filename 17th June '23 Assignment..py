#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Ans.1
## The 'else' block in a try-except statement is optional and is used to specify a block of code that should be executed if no exceptions are raised within the 'try' block.

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("The result of the division is:", result)
divide(10, 4)
divide(10, 0)


# In[7]:


#Ans.2\
def process_data(data):
    try:
        result = data / 2
        print("Result of division:", result)
        try:
            element = data[8]
            print("Element at index 8]:", element)
        except IndexError:
            print("Error: Index out of range!")
        
    except TypeError:
        print("Error: Invalid data type!")
process_data(15)
process_data([18, 55, 41])





# In[10]:


#Ans.3
class NegativeNumberError(Exception):
    pass

def process_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers is not allowed.")
    else:
        print("Processing number:", num)

try:
    process_number(45)
    process_number(-8)
except NegativeNumberError as e:
    print(e)
Processing_number: 45


# In[ ]:


#Ans.5
## Logging in python is the process of capturing and storing events and information during program execution. it is important in software development for debugging, troubleshooting, performance analysis, and monitoring purposes logging provides valuable insights aids in error handlin and enables efficient analysis and improvement of applications.


# In[ ]:


#Ans.6
## Log levels in python logging categorize :-

#DEBUG level is used for detailed debugging during development.
#INFO level provides high-level details about normal execution.
#3ERROR level indicates significant errors, while CRITICAL level represents severe issues requiring immediate attentio.


# In[30]:


#Ans.7
## log formatters in python logging allow you to customize the format of log messages. By specifying a format pattern with placeholders, you can include attributes like timestamp, log level, module name, and the log message itself
import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.debug('This is a debug message')
logger.info('This is an info message')


# In[31]:


#Ans.8

import logging

logger = logging.getLogger('module1')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.debug('Debug message from module1')
logger.info('Info message from module1')


# In[32]:


import logging

logger = logging.getLogger('module2')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('module2.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug('Debug message from module2')
logger.info('Info message from module2')


# In[ ]:


#Ans.9
## Logging in python is designed for systematic recording and management of program execution. It offers flexibility in capturing different log levels, customizing message format, and directing output to various destinations logging is recommended for real-world applications due to its maintainability, granularity, suitability for production environments and customization options print statements are more suitable for quick debugging during development.


# In[33]:


#Ans.10
import logging

# Configure logging
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('app.log', mode='a')
logger.addHandler(file_handler)

logger.info('Hello, World!')   # Log the message


# In[36]:


#Ans.11

import logging
import datetime

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger('')
file_handler = logging.FileHandler('errors.log')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
    1 / 0 
except Exception as e:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    error_message = f'Exception: {type(e).__name__}, Timestamp: {timestamp}'
    logger.error(error_message)
    print(error_message)


# In[ ]:




