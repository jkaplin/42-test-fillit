#!/bin/bash/python3

import os

def test_fillit(your_binary, test_file, expected_output):
    os.system("./" + your_binary + " " + test_file + " > " + ".your_out")
    os.system("cp " + expected_output + " .true_out")

    your_output_file = open(".your_out", "r")
    true_output_file = open(".true_out", "r")
    if (your_output_file.read() == true_output_file.read()):
        print("\033[1;32;40mSUCCESS\033[0m\n")
        return (0)
    else:
        print("\033[1;31;40mFAILURE\033[0m" + "Here's the difference:\n")
        print("                       YOUR PRINTOUT                          |                  EXPECTED PRINTOUT")
        os.system("diff -y .your_out .true_out")
        return (1)
