import logging
logger = logging.getLogger('logger.log')
logging.basicConfig(filename='logger.log')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
