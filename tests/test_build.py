import pytest

from jenkins_flaky.build import parse_build


@pytest.fixture
def build_data():
    return {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
            u'actions': [{u'_class': u'hudson.model.CauseAction',
                          u'causes': [{u'_class': u'jenkins.branch.BranchEventCause',
                                       u'shortDescription': u'Branch event'}]},
                         {u'_class': u'jenkins.metrics.impl.TimeInQueueAction',
                          u'blockedDurationMillis': 0,
                          u'blockedTimeMillis': 0,
                          u'buildableDurationMillis': 0,
                          u'buildableTimeMillis': 880,
                          u'buildingDurationMillis': 676304,
                          u'executingTimeMillis': 898526,
                          u'executorUtilization': 1.33,
                          u'subTaskCount': 6,
                          u'waitingDurationMillis': 23,
                          u'waitingTimeMillis': 100},
                         {},
                         {u'_class': u'jenkins.scm.api.SCMRevisionAction'},
                         {},
                         {u'_class': u'hudson.plugins.git.util.BuildData',
                          u'buildsByBranchName': {u'7.37.0': {u'_class': u'hudson.plugins.git.util.Build',
                                                              u'buildNumber': 1,
                                                              u'buildResult': None,
                                                              u'marked': {
                                                                  u'SHA1': u'6d4fd1230d1b76595a78378192e3b4aae90cb611',
                                                                  u'branch': [{
                                                                                  u'SHA1': u'6d4fd1230d1b76595a78378192e3b4aae90cb611',
                                                                                  u'name': u'7.37.0'}]},
                                                              u'revision': {
                                                                  u'SHA1': u'6d4fd1230d1b76595a78378192e3b4aae90cb611',
                                                                  u'branch': [{
                                                                                  u'SHA1': u'6d4fd1230d1b76595a78378192e3b4aae90cb611',
                                                                                  u'name': u'7.37.0'}]}}},
                          u'lastBuiltRevision': {u'SHA1': u'6d4fd1230d1b76595a78378192e3b4aae90cb611',
                                                 u'branch': [{u'SHA1': u'6d4fd1230d1b76595a78378192e3b4aae90cb611',
                                                              u'name': u'7.37.0'}]},
                          u'remoteUrls': [u'https://bitbucket.org/test/test.git'],
                          u'scmName': u''},
                         {u'_class': u'hudson.plugins.git.GitTagAction'},
                         {},
                         {u'_class': u'hudson.plugins.git.util.BuildData',
                          u'buildsByBranchName': {u'1.6.0': {u'_class': u'hudson.plugins.git.util.Build',
                                                             u'buildNumber': 1,
                                                             u'buildResult': None,
                                                             u'marked': {
                                                                 u'SHA1': u'bc61cc7621e9751b2a738d5553b89af17a0e4d06',
                                                                 u'branch': [{
                                                                                 u'SHA1': u'bc61cc7621e9751b2a738d5553b89af17a0e4d06',
                                                                                 u'name': u'1.6.0'}]},
                                                             u'revision': {
                                                                 u'SHA1': u'bc61cc7621e9751b2a738d5553b89af17a0e4d06',
                                                                 u'branch': [{
                                                                                 u'SHA1': u'bc61cc7621e9751b2a738d5553b89af17a0e4d06',
                                                                                 u'name': u'1.6.0'}]}}},
                          u'lastBuiltRevision': {u'SHA1': u'bc61cc7621e9751b2a738d5553b89af17a0e4d06',
                                                 u'branch': [{u'SHA1': u'bc61cc7621e9751b2a738d5553b89af17a0e4d06',
                                                              u'name': u'1.6.0'}]},
                          u'remoteUrls': [u'https://bitbucket.org/test/test2.git'],
                          u'scmName': u''},
                         {u'_class': u'hudson.plugins.git.util.BuildData',
                          u'buildsByBranchName': {u'release': {u'_class': u'hudson.plugins.git.util.Build',
                                                               u'buildNumber': 1,
                                                               u'buildResult': None,
                                                               u'marked': {
                                                                   u'SHA1': u'573ad7327e8e55188422f5bc07cf0cb9920b4878',
                                                                   u'branch': [{
                                                                                   u'SHA1': u'573ad7327e8e55188422f5bc07cf0cb9920b4878',
                                                                                   u'name': u'release'}]},
                                                               u'revision': {
                                                                   u'SHA1': u'573ad7327e8e55188422f5bc07cf0cb9920b4878',
                                                                   u'branch': [{
                                                                                   u'SHA1': u'573ad7327e8e55188422f5bc07cf0cb9920b4878',
                                                                                   u'name': u'release'}]}}},
                          u'lastBuiltRevision': {u'SHA1': u'573ad7327e8e55188422f5bc07cf0cb9920b4878',
                                                 u'branch': [{u'SHA1': u'573ad7327e8e55188422f5bc07cf0cb9920b4878',
                                                              u'name': u'release'}]},
                          u'remoteUrls': [u'https://bitbucket.org/test/asd.git'],
                          u'scmName': u''},
                         {},
                         {u'_class': u'org.jenkinsci.plugins.workflow.cps.EnvActionImpl'},
                         {u'_class': u'hudson.plugins.git.util.BuildData',
                          u'buildsByBranchName': {u'PR-1377': {u'_class': u'hudson.plugins.git.util.Build',
                                                               u'buildNumber': 1,
                                                               u'buildResult': None,
                                                               u'marked': {
                                                                   u'SHA1': u'ad916fe96f7e13a1d192ca5a7595ede65399063f',
                                                                   u'branch': [{
                                                                                   u'SHA1': u'ad916fe96f7e13a1d192ca5a7595ede65399063f',
                                                                                   u'name': u'PR-1377'}]},
                                                               u'revision': {
                                                                   u'SHA1': u'ad916fe96f7e13a1d192ca5a7595ede65399063f',
                                                                   u'branch': [{
                                                                                   u'SHA1': u'ad916fe96f7e13a1d192ca5a7595ede65399063f',
                                                                                   u'name': u'PR-1377'}]}}},
                          u'lastBuiltRevision': {u'SHA1': u'ad916fe96f7e13a1d192ca5a7595ede65399063f',
                                                 u'branch': [{u'SHA1': u'ad916fe96f7e13a1d192ca5a7595ede65399063f',
                                                              u'name': u'PR-1377'}]},
                          u'remoteUrls': [u'https://bitbucket.org/test/test3.git'],
                          u'scmName': u''},
                         {},
                         {},
                         {},
                         {},
                         {},
                         {u'_class': u'hudson.plugins.bandit.BanditResultAction'},
                         {},
                         {},
                         {},
                         {},
                         {},
                         {'_class': 'hudson.tasks.junit.TestResultAction', 'failCount': 3, 'skipCount': 0, 'totalCount': 21976, 'urlName': 'testReport'},
                         {},
                         {},
                         {},
                         {},
                         {
                             u'_class': u'org.jenkinsci.plugins.pipeline.modeldefinition.actions.RestartDeclarativePipelineAction'},
                         {},
                         {u'_class': u'org.jenkinsci.plugins.workflow.job.views.FlowGraphAction'},
                         {},
                         {},
                         {}],
            u'artifacts': [{}],
            u'building': False,
            u'changeSets': [],
            u'culprits': [],
            u'description': None,
            u'displayName': u'#1',
            u'duration': 676304,
            u'estimatedDuration': 1742731,
            u'executor': None,
            u'fullDisplayName': u'fullDisplayName',
            u'id': u'1',
            u'keepLog': False,
            u'nextBuild': {u'number': 2,
                           u'url': u'url'},
            u'number': 1,
            u'previousBuild': None,
            u'queueId': 424809,
            u'result': u'FAILURE',
            u'timestamp': 1587131889595,
            u'url': u'https://jenkis.com/sdasd/PR-1377/1/'}


def test_parses_revision(build_data):
    build = parse_build(build_data)
    assert build.revision == 'ad916fe96f7e13a1d192ca5a7595ede65399063f'


def test_parses_name(build_data):
    build = parse_build(build_data)
    assert build.job_name == 'PR-1377'


def test_parses_number(build_data):
    build = parse_build(build_data)
    assert build.number == 1


def test_parses_timestamp(build_data):
    build = parse_build(build_data)
    assert build.timestamp == 1587131889595/1000


def test_parses_duration(build_data):
    build = parse_build(build_data)
    assert build.duration == 676304


def test_parses_status(build_data):
    build = parse_build(build_data)
    assert build.status == 'FAILURE'


def test_parses_failed_tests(build_data):
    build = parse_build(build_data)
    assert build.failed_tests == 3
