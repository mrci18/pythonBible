import logging
#logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#log to a file instead
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is " + str(i) + ', total is ' + str(total))
    logging.debug("End of factorial (%s)" % (n))
    return total 

print(factorial(5))
logging.debug("End of program")
#logging.disable() a logging level, 
#and it will suppress all log messages at that level or lower
#logging.disable(logging.CRITICAL)
#logging.disable() will disable all messages after it, 
#you will probably want to add it near the import logging line of code in your program

"""
Logging Levels

logging.debug()

The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

INFO

logging.info()

Used to record information on general events in your program or confirm that things are working at their point in the program.

WARNING

logging.warning()

Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

ERROR

logging.error()

Used to record an error that caused the program to fail to do something.

CRITICAL

logging.critical()

The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
"""