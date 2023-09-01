# logging is a module that allows you to write messages to a file or the console
# line 3 & 4 is the basic configuration for logging
#! DO NOT NAME YOUR FILE logging.py, it will cause an error when you try to import the logging module
import logging
# if you want to write your log to a file, you can add a filename argument before the LEVEL argument to the basicConfig method, i.e. filename='programLog.txt'
logging.basicConfig(filename= 'programlog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# The different levels of logging are: 
# DEBUG, INFO, WARNING, ERROR, and CRITICAL (in order of least to most severe), so calling CRITICAL in the disable method will disable ALL LOGGING messages
# logging.disable(logging.CRITICAL) # this will disable all logging messages

logging.debug('Start of program')

def factorial(n):
  logging.debug('Start of factorial(%s)')
  total = 1
  for i in range(1, n + 1):
    total *= i
    logging.debug(f'''i is {i}, total is {total}''')
  return total

print(factorial(5))

logging.debug('End of program')