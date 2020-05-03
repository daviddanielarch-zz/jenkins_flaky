from operator import attrgetter

from jenkins_flaky.factories import build_factory
from jenkins_flaky.flaky import get_flaky_builds, get_flaky_tests, FlakyTest
from jenkins_flaky.test_report import FailedTest


def test_flaky_builds_empty():
    assert get_flaky_builds([]) == []


def test_no_flaky_builds():
    builds = [build_factory(job_name='PR-100', revision='asd', number=0),
              build_factory(job_name='PR-100', revision='asd1', number=1),
              build_factory(job_name='PR-100', revision='asd2', number=1)]
    assert get_flaky_builds(builds) == []


def test_multiple_flaky():
    builds = [build_factory(job_name='PR-100', revision='asd', number=0),
              build_factory(job_name='PR-100', revision='asd', number=1),
              build_factory(job_name='PR-100', revision='asd1', number=2),
              build_factory(job_name='PR-100', revision='asd2', number=3),
              build_factory(job_name='PR-100', revision='asd3', number=4),
              build_factory(job_name='PR-100', revision='asd3', number=5),
              ]
    flaky_group1 = [build_factory(job_name='PR-100', revision='asd', number=0),
                    build_factory(job_name='PR-100', revision='asd', number=1)]

    flaky_group2 = [build_factory(job_name='PR-100', revision='asd3', number=4),
                    build_factory(job_name='PR-100', revision='asd3', number=5)]

    assert get_flaky_builds(builds) == [flaky_group1, flaky_group2]


def test_get_flaky_tests_two_groups():
    failed_test_group1 = [FailedTest(job_name='job1', build_number=1, name='test1'),
                          FailedTest(job_name='job1', build_number=1, name='test2')]
    failed_test_group2 = [FailedTest(job_name='job1', build_number=2, name='test2'),
                          FailedTest(job_name='job1', build_number=2, name='test3')]

    flaky_tests = get_flaky_tests([failed_test_group1, failed_test_group2])

    assert sorted([test.name for test in flaky_tests]) == ['test1', 'test3']


def test_flaky_tests_executions():
    failed_test_group1 = [FailedTest(job_name='job1', build_number=1, name='test1'),
                          FailedTest(job_name='job1', build_number=1, name='test2')]
    failed_test_group2 = [FailedTest(job_name='job1', build_number=2, name='test2'),
                          FailedTest(job_name='job1', build_number=2, name='test3')]

    flaky1, flaky2 = sorted(get_flaky_tests([failed_test_group1, failed_test_group2]), key=attrgetter('name'))
    assert flaky1.executions == [FailedTest(job_name='job1', build_number=1, name='test1')]
    assert flaky2.executions == [FailedTest(job_name='job1', build_number=2, name='test3')]


def test_get_flaky_tests_more_groups():
    failed_test_group1 = [FailedTest(job_name='job1', build_number=1, name='test1'),
                          FailedTest(job_name='job1', build_number=1, name='test2'),
                          FailedTest(job_name='job1', build_number=1, name='test3')]
    failed_test_group2 = [FailedTest(job_name='job1', build_number=2, name='test2'),
                          FailedTest(job_name='job1', build_number=2, name='test3'),
                          FailedTest(job_name='job1', build_number=2, name='test5')]
    failed_test_group3 = [FailedTest(job_name='job1', build_number=3, name='test4'),
                          FailedTest(job_name='job1', build_number=3, name='test2')]
    failed_test_group4 = [FailedTest(job_name='job1', build_number=3, name='test5'),
                          FailedTest(job_name='job1', build_number=4, name='test3'),
                          FailedTest(job_name='job1', build_number=4, name='test2')]

    flaky_tests = get_flaky_tests([failed_test_group1,
                                   failed_test_group2,
                                   failed_test_group3,
                                   failed_test_group4])

    assert sorted([test.name for test in flaky_tests]) == ['test1', 'test3', 'test4', 'test5']
