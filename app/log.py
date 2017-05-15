import logging
from config import CONFIG_LOCAL_LOGFILE

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)-2s %(message)s',
                datefmt='%d %b %Y %H:%M:%S',
                filename=CONFIG_LOCAL_LOGFILE,
                filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(filename)s[line:%(lineno)d]%(levelname)-2s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)



