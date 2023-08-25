import logging
logging.warning('Watch out!')  # Output: WARNING:root:Watch out!

# Fun Facts
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
# This will write the debug message to the 'example.log' file