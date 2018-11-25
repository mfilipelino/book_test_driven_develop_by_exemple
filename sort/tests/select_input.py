import sys

from sort.selection import selection
import logging


def start_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


if __name__ == '__main__':

    start_logging()
    if len(sys.argv) < 2:
        logging.info(sys.argv)
        logging.error('python {}.py <number>'.format(sys.argv[0]))
        exit()

    logging.info('start')
    size = int(sys.argv[1])
    vector = list(range(size, 0, -1))
    selection(vector)
    logging.info(vector[:5])
    logging.info('finish')