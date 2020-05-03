#!/usr/bin/env python

import argparse
from json import JSONDecoder

from jenkins_flaky.serialization import from_json


parser = argparse.ArgumentParser(description='Diff two files with flaky tests to get the new ones')
parser.add_argument('db_file', type=argparse.FileType('r'))
args = parser.parse_args()


flaky_tests = JSONDecoder(object_hook=from_json).decode(args.db_file.read())
for flaky in flaky_tests:
    print(flaky.name)
    #for execution in flaky.executions:
    #    print(f'\t{execution.job_name}/{execution.build_number}')
