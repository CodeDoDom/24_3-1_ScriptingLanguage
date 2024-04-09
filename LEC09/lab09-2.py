# Logging
import logging

logging.basicConfig(
    filename='log.txt',
    # level=logging.INFO,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

for i in range(10):
    # print(i)
    logging.info(f'{i=}')
    logging.debug(f'{i=}')  # print 대신하여 사용, 이후에 CRITICAL로 바꾸면 됨... 뭔가가...
    logging.warning(f'{i=}')
    logging.error(f'{i=}')
    logging.critical(f'{i=}')
