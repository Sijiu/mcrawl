# coding=utf8

import random
from string import lowercase, digits


random = random.SystemRandom()


def random_string(length = 16):
    """
    length: 随机数长度
    """
    chars = lowercase + digits
    return ''.join([random.choice(chars) for i in xrange(length)])


if __name__ == "__main__":
    print random_string()
