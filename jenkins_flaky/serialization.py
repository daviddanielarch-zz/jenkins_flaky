from json import JSONEncoder

from jenkins_flaky.flaky import FlakyTest
from jenkins_flaky.test_report import FailedTest


def from_json(json_object):
    object_type = json_object.pop('type')
    if object_type == 'FailedTest':
        instance = FailedTest(**json_object)

    if object_type == 'FlakyTest':
        instance = FlakyTest(json_object['name'])
        for failed_test in json_object['executions']:
            instance.executions.append(failed_test)

    return instance


class FlakyTestEncoder(JSONEncoder):
    def default(self, o):
        encoded = o.__dict__
        encoded['type'] = o.__class__.__name__
        return encoded
