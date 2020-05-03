#!/usr/bin/env python

import argparse


def get_new_flaky_test_names(known_flakys_tests, current_run_flakys_tests):
    return [flaky for flaky in set(current_run_flakys_tests) - set(known_flakys_tests)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Diff two files with flaky tests to get the new ones')
    parser.add_argument('known_flaky_file', type=argparse.FileType('r'))
    parser.add_argument('new_flaky_file', type=argparse.FileType('r'))
    args = parser.parse_args()

    known_flakys = args.known_flaky_file.readlines()
    current_run_flakys = args.new_flaky_file.readlines()
    for flaky_test_name in get_new_flaky_test_names(known_flakys, current_run_flakys):
        print(flaky_test_name)
