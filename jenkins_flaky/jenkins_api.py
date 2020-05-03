from functools import lru_cache

import jenkins
from jenkins_flaky.flaky import get_flaky_builds, get_flaky_tests, merge_flaky_tests

from jenkins_flaky.build import parse_build
from jenkins_flaky.job import parse_job, Job
from jenkins_flaky.test_report import parse_failed_tests


class JenkinsClient:
    def __init__(self, host, username, password):
        self.jenkins = jenkins.Jenkins(host, username=username, password=password)

    def get_all_jobs(self, condition, key: str):
        data = self.jenkins.get_all_jobs()
        for elem in data:
            if condition(elem):
                yield self.get_job(elem[key])

    @lru_cache()
    def get_build(self, job_name: str, build_count: int):
        data = self.jenkins.get_build_info(job_name, build_count)
        return parse_build(data)

    def get_job(self, job_name: str):
        data = self.jenkins.get_job_info(job_name)
        return parse_job(data)

    def get_build_failed_tests(self, job_name: str, build_count: int):
        build = self.get_build(job_name, build_count)
        test_report = self.jenkins.get_build_test_report(job_name, build_count)
        return parse_failed_tests(build, test_report)

    def get_job_flaky_tests(self, job: Job = None, job_name: str = ''):
        flaky_tests: list = []

        if not job and not job_name:
            raise Exception('One of job or job_name is needed')

        if not job:
            job = self.get_job(job_name)

        print(f'Processing {job}')
        builds = []
        for build in range(1, job.build_count + 1):
            builds.append(self.get_build(job.full_name, build))

        flaky_builds_groups = get_flaky_builds(builds)
        if not flaky_builds_groups:
            return flaky_tests

        print(f'Flaky build groups found {flaky_builds_groups}')

        for flaky_build_group in flaky_builds_groups:
            failed_group_tests: list = []

            for build in flaky_build_group:
                print(f'Getting failed tests for {build.job_name}/{build.number}')
                failed_group_tests.append(self.get_build_failed_tests(job.full_name, build.number))

            flaky_tests_for_the_build = get_flaky_tests(failed_group_tests)
            flaky_tests = merge_flaky_tests(flaky_tests, flaky_tests_for_the_build)

        return flaky_tests
