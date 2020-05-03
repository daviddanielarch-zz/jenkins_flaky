from jenkins_flaky.build import Build


def build_factory(
        job_name: str = '',
        revision: str = '',
        number: int = 0,
        timestamp: float = 0,
        duration: int = 0,
        status: str = 'FAILURE',
        failed_tests: int = 20
):
    return Build(job_name=job_name,
                 revision=revision,
                 number=number,
                 timestamp=timestamp,
                 duration=duration,
                 status=status,
                 failed_tests=failed_tests)
