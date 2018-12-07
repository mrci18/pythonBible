#!/bin/python3

import math
import os
import random
import re
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

# Complete the rotLeft function below.
def rotLeft(a, d):
    logging.debug(a)
    logging.debug(d)
    first = a.pop(0)
    logging.debug(first)
    logging.debug(a)
    for i in range(d):
        first = a.pop(0)
        a.append(first)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

