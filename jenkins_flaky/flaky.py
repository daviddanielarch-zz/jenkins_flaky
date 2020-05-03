from collections import defaultdict


class FlakyTest:
    def __init__(self, name: str, executions: list = None):
        self.name = name
        self.executions = executions if executions else []

    def __repr__(self):
        return f'FlakyTest: {self.name}'

    def __eq__(self, other):
        return self.name == other.name and sorted(self.executions) == sorted(other.executions)


def get_flaky_builds(builds):
    """
    Get all builds in which the user had to retry the build because of flaky tests
    The criteria used to detect retries is the build revision hash
    :param builds: List of builds
    :type builds: List(List(Build))
    :return: The original list filtered to return only groups of builds which contain flaky tests
    :rtype: List(List(Build))
    """
    flaky_builds = []

    revisions = defaultdict(list)
    for build in builds:
        aborted_build = build.status == 'ABORTED'
        failed_build_without_tests = build.status in ['FAILURE', 'UNSTABLE'] and build.failed_tests == 0
        if aborted_build or failed_build_without_tests:
            continue

        revisions[build.revision].append(build)

    for revision, builds in revisions.items():
        if len(builds) >= 2:
            flaky_builds.append(builds)

    return flaky_builds


def flatten_list(l):
    return [item for sublist in l for item in sublist]


def get_flaky_tests(failed_tests_groups):
    flaky_tests_names = get_flaky_tests_names(failed_tests_groups)

    flaky_tests = {test_name: FlakyTest(name=test_name) for test_name in flaky_tests_names}
    failed_tests = flatten_list(failed_tests_groups)
    for failed_test in failed_tests:
        if failed_test.name in flaky_tests_names:
            flaky_tests[failed_test.name].executions.append(failed_test)

    return flaky_tests.values()


def get_flaky_tests_names(failed_tests_groups):
    failed_test_names_groups = []
    flaky_tests = set()

    for group in failed_tests_groups:
        failed_test_names_groups.append([failed_test.name for failed_test in group])
    head, *tail = [set(x) for x in failed_test_names_groups]
    non_flaky_tests = head.intersection(*tail)
    for test_group in failed_test_names_groups:
        test_group_flaky_tests = set(test_group) - non_flaky_tests
        flaky_tests.update(test_group_flaky_tests)

    return flaky_tests


def merge_flaky_tests(original_tests, new_tests):
    merged_flaky_tests = {}
    for test in original_tests:
        if test.name not in merged_flaky_tests:
            merged_flaky_tests[test.name] = test
        else:
            merged_flaky_tests[test.name].executions += test.executions

    for test in new_tests:
        if test.name not in merged_flaky_tests:
            merged_flaky_tests[test.name] = test
        else:
            merged_flaky_tests[test.name].executions += test.executions

    return merged_flaky_tests.values()
