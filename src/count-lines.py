import logging
import sys
import os
import time


def count_lines(filename):
    """
    Count the number of lines in file. If the file can't be
    opened, it should be treated the same as if it was empty
    """

    input_file = None
    try:
        input_file = open(filename, 'r')
        lines = input_file.readlines()
    except TypeError as exp:
        logging.error(exp)
        return 0
    except IOError as exp:
        logging.error(exp)
        return 0
    except UnicodeDecodeError as exp:
        logging.error(exp)
        return 0
    else:
        # print(lines)
        return len(lines)
    finally:
        if input_file:
            input_file.close()


def count_words(filename):
    """
    Count the number of words in file. If the file can't be
    opened, it should be treated the same as if it was empty
    """

    with open(filename, 'r') as input_file:
        words = 0
        lines = input_file.readlines()
        for line in lines:
            words += len(line.split(' '))
        return words


i = 1
while i < len(sys.argv):
    print(os.path.abspath(sys.argv[i]))
    print(time.ctime(os.path.getctime(sys.argv[i])))
    print(count_lines(sys.argv[i]))
    print(count_words(sys.argv[i]))
    i += 1
