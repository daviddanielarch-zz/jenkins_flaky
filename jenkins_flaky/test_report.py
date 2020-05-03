class FailedTest:
    def __init__(
            self,
            job_name: str,
            build_number: int,
            name: str,
            traceback: str = '',
            timestamp: int = 0
    ):
        self.job_name = job_name
        self.build_number = build_number
        self.name = name
        self.traceback = traceback
        self.timestamp = timestamp

    def __lt__(self, other):
        if self.timestamp < other.timestamp:
            return True

        return False

    def __repr__(self):
        return f'FailedTest: {self.job_name}/{self.build_number} [{self.name}]'

    def __eq__(self, other):
        return self.name == other.name and self.job_name == other.job_name and self.build_number


def parse_failed_tests(build, test_report):
    """
    Get all failed tests from a Jenkins test report.
    :param build: Build instance
    :type build: Build
    :param test_report: Jenkins test report
    :type test_report: dict
    :return: List of failed tests
    :rtype: List(FailedTest)
    """
    failed_tests = []
    if not test_report:
        return failed_tests

    for suite in test_report['suites']:
        for case in suite['cases']:
            if case['status'] == 'FAILED':
                test = FailedTest(job_name=build.job_name,
                                  build_number=build.number,
                                  timestamp=build.timestamp,
                                  name=get_pytest_name(case['className'], case['name']),
                                  traceback=case['errorStackTrace'])
                failed_tests.append(test)

    return failed_tests


def get_pytest_name(root, name):
    """
    Build a pytest like test name given the test name and the root className from
    a jenkins test report.
    :param root: Testcase className for a Jenkins test report
    :param name: Testcase name for a Jenkins test report
    :return:
    """
    *head, tail = root.split('.')

    if is_class_name(tail):
        path = '/'.join(head)
        return f'{path}.py::{tail}::{name}'
    else:
        return f'{root.replace(".", "/")}.py::{name}'


def is_class_name(class_name):
    """
    Check if the given string is a python class.
    The criteria to use is the convention that Python classes start with uppercase

    :param class_name: The name of class candidate
    :type class_name: str
    :return: True whether the class_name is a python class otherwise False
    """
    return class_name.capitalize()[0] == class_name[0]
