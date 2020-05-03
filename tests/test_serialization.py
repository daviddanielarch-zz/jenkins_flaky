import json
from json import JSONDecoder

from jenkins_flaky.flaky import FlakyTest
from jenkins_flaky.serialization import from_json, FlakyTestEncoder
from jenkins_flaky.test_report import FailedTest


def test_serialization():
    flaky_test = FlakyTest(name='test', executions=[FailedTest(job_name='job1', build_number=1, name='test1')])
    deserialized_flaky_test = JSONDecoder(object_hook=from_json).decode(json.dumps(flaky_test, cls=FlakyTestEncoder))
    assert flaky_test.name == deserialized_flaky_test.name
    assert flaky_test.executions[0] == deserialized_flaky_test.executions[0]
