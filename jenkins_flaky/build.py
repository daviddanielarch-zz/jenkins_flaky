from datetime import datetime


class Build:
    def __init__(
            self,
            job_name: str,
            revision: str,
            number: int,
            timestamp: int,
            duration: int,
            status: str,
            failed_tests: int = 0
    ):
        self.job_name = job_name
        self.number = number
        self.revision = revision
        self.timestamp = timestamp
        self.duration = duration
        self.status = status
        self.failed_tests = failed_tests

    def __repr__(self):
        human_datetime = datetime.fromtimestamp(self.timestamp).isoformat()
        return f'{self.job_name}/{self.number} SHA1{self.revision} {human_datetime}'

    def __eq__(self, other):
        return self.job_name == other.job_name and \
               self.number == other.number and \
               self.revision == other.revision


def parse_build(data):
    failed_tests: int = 0
    revision: str = None
    job_name: str = data['url'].split('/')[-3]
    for action in reversed(data['actions']):
        if 'buildsByBranchName' in action and job_name in action['buildsByBranchName']:
            revision = action['buildsByBranchName'][job_name]['revision']['SHA1']
            break

        if '_class' in action and action['_class'] == 'hudson.tasks.junit.TestResultAction':
            failed_tests = action['failCount']

    revision = revision
    return Build(
        job_name=job_name,
        revision=revision,
        number=data['number'],
        timestamp=data['timestamp'] / 1000,
        duration=data['duration'],
        failed_tests=failed_tests,
        status=data['result'],
    )

# with open('/home/davida/jenkins_flaky/tests/test_report.json', 'r') as data:
#     test_report = json.loads(data.read())
# print(get_failed_tests(test_report))
