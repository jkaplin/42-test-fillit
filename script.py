#!/bin/python3

import os
from test_print import test_fillit

def make_list(folder, name, num):
    tests = []
    i = 0
    while (i < num):
        test = folder + name + str(i) + ".txt"
        tests.append(test)
        i += 1
    return tests

tests = make_list("tests/", "test", 6)
error_tests = make_list("error_tests/", "test_error", 7)

i = 0
total = 0
while (i < len(tests)):
    print("\ntest" + str(i))
    total += test_fillit("fillit", "tests/test" + str(i) + ".txt", "tests/output" + str(i) + ".txt")
    i += 1
if (total == 0):
    print("\n\033[1;32;40m PERFECT\033[0m\n")
else:
    print("\n\033[1;31;40m" + str(total) + " FAILED" + "\033[0m\n")

i = 0
total = 0
while (i < len(error_tests)):
    print("\ntest_error" + str(i))
    total += test_fillit("fillit", "tests/test_error" + str(i) + ".txt", "tests/error_output.txt")
    i += 1
if (total == 0):
    print("\n\033[1;32;40m PERFECT\033[0m\n")
else:
    print("\n\033[1;31;40m" + str(total) + " FAILED" + "\033[0m\n")
