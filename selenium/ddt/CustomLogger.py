import logging
import datetime

dt = datetime.datetime.now()
def logger():
    logging.basicConfig(handlers=[logging.FileHandler(filename=f'./test1_{dt.strftime("%d%b%Y_%H%M%S")}.txt', mode='w'),
                                  logging.StreamHandler()
                                  ],
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')
    return logging