# 1-debug(extra info about steps - trobuleshoot)
# 2-info(infor abut steps)
# 3-warning(step P/F status can be ignore)(default)
# 4-error(Fail)
# 5-critical()
import datetime
import logging

# log = logging.getLogger()
# print(log)#<RootLogger root (WARNING)>
# log.setLevel(logging.DEBUG)
# print(log)
dt=datetime.datetime.now()

# logging.basicConfig(filename=f'./test1_{dt.strftime("%d%b%Y_%H%M%S")}.txt',
#                     filemode="w",
#                     level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(message)s')

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(message)s')

logging.basicConfig(handlers=[logging.FileHandler(filename=f'./test1_{dt.strftime("%d%b%Y_%H%M%S")}.txt', mode='w'),
                              logging.StreamHandler()
                              ],
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')


logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warn")
logging.error("this is error")
logging.critical("this is critical")