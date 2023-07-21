import logging
list = [10,20,30,40]

logging.basicConfig(filename='output.txt', level=logging.DEBUG)
logging.debug(list)