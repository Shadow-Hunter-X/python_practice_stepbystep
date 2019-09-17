#!/usr/bin/env python
import sys
import string
import hashlib

while True:
    line = sys.stdin.readline()
    if not line:
        break

    line = string.strip(line, "\n ")
    sepal_length, sepal_width, petal_length , petal_width , species = string.split(line, "\t")
    sum_value = sepal_length + sepal_width + petal_length + petal_width
    print hashlib.md5(sum_value).hexdigest()