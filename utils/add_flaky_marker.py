#!/usr/bin/env python

import argparse
import os


def is_duplicated(thing, lines):
    count = 0
    for line in lines:
        if thing in line:
            count += 1

    return count > 1


def get_index(lines, function_name):
    for index, line in enumerate(lines):
        if not line:
            last_blank_line = index

        if function_name in line:
            return last_blank_line

    raise Exception(f'{function_name} is not defined')


def test_in_file(lines, function_name):
    found = False
    for line in lines:
        if function_name in line:
            found = True
            break

    return found


def add_flaky_marker(file_content, function_name, class_name=None, comment=''):
    lines = file_content.splitlines()
    new_file_lines = []

    if not test_in_file(lines, function_name):
        raise Exception(f'{function_name} is not defined')

    if is_duplicated(function_name, lines):
        raise Exception(f'{function_name} is defined more than once')

    line_to_add_marker = get_index(lines, function_name)

    if class_name:
        whitespaces = 4
    else:
        whitespaces = 0

    for index, line in enumerate(lines):
        new_file_lines.append(line)

        if index == line_to_add_marker:
            marker = f"{' ' * whitespaces}@pytest.mark.flaky"
            if comment:
                marker += f' # {comment}'

            new_file_lines.append(marker)

    return '\n'.join(new_file_lines)


def is_test_within_class(test_name):
    return test_name.count('::') == 2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add flaky marker to new flaky tests')
    parser.add_argument('project_root')
    parser.add_argument('new_flaky_tests_file', type=argparse.FileType('r'))
    parser.add_argument('--comment', required=False)
    args = parser.parse_args()

    flaky_tests = args.new_flaky_tests_file.read().splitlines()

    for flaky_test in flaky_tests:
        print(f'Processing {flaky_test}')
        class_name = None
        if is_test_within_class(flaky_test):
            filename, class_name, function_name = flaky_test.split('::')
        else:
            filename, function_name = flaky_test.split('::')

        file_path = os.path.join(args.project_root, filename)

        try:
            with open(file_path, 'r') as original_file:
                file_content = original_file.read()
        except FileNotFoundError:
            print(f'Failed processing {flaky_test}')
            continue

        try:
            new_file_content = add_flaky_marker(file_content, function_name.strip(), class_name, args.comment) + '\n'
        except Exception as e:
            print(f'Failed processing {flaky_test}')
            print(e)
            continue

        with open(file_path, 'w') as new_file:
            file_content = new_file.write(new_file_content)
