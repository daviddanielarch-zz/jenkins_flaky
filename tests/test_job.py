import pytest

from jenkins_flaky.job import parse_job


@pytest.fixture
def job_data():
    return {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowJob',
            u'actions': [{},
                         {},
                         {},
                         {},
                         {},
                         {},
                         {},
                         {u'_class': u'hudson.plugins.jobConfigHistory.JobConfigHistoryProjectAction'},
                         {},
                         {u'_class': u'jenkins.scm.api.metadata.ContributorMetadataAction'},
                         {},
                         {u'_class': u'jenkins.scm.api.metadata.ObjectMetadataAction'},
                         {},
                         {},
                         {},
                         {u'_class': u'org.jenkinsci.plugins.testresultsanalyzer.TestResultsAnalyzerAction'},
                         {u'_class': u'com.cloudbees.plugins.credentials.ViewCredentialsAction'}],
            u'buildable': True,
            u'builds': [{u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                         u'number': 3,
                         u'url': u'url1'},
                        {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                         u'number': 2,
                         u'url': u'url2'},
                        {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                         u'number': 1,
                         u'url': u'url3'}],
            u'color': u'yellow',
            u'concurrentBuild': True,
            u'description': None,
            u'displayName': u'PR-1377',
            u'displayNameOrNull': None,
            u'firstBuild': {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                            u'number': 1,
                            u'url': u'url1'},
            u'fullDisplayName': u'dilapyname',
            u'fullName': u'fullName',
            u'healthReport': [{u'description': u'Build stability: 1 out of the last 3 builds failed.',
                               u'iconClassName': u'icon-health-60to79',
                               u'iconUrl': u'health-60to79.png',
                               u'score': 66},
                              {u'description': u'Test Result: 3 tests failing out of a total of 21,976 tests.',
                               u'iconClassName': u'icon-health-80plus',
                               u'iconUrl': u'health-80plus.png',
                               u'score': 99}],
            u'inQueue': False,
            u'keepDependencies': False,
            u'lastBuild': {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                           u'number': 3,
                           u'url': u'url3'},
            u'lastCompletedBuild': {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                                    u'number': 3,
                                    u'url': u'url3'},
            u'lastFailedBuild': {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                                 u'number': 1,
                                 u'url': u'url1'},
            u'lastStableBuild': None,
            u'lastSuccessfulBuild': {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                                     u'number': 3,
                                     u'url': u'url3'},
            u'lastUnstableBuild': {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                                   u'number': 3,
                                   u'url': u'url3'},
            u'lastUnsuccessfulBuild': {u'_class': u'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                                       u'number': 3,
                                       u'url': u'url3'},
            u'name': u'PR-1377',
            u'nextBuildNumber': 4,
            u'property': [{u'_class': u'org.jenkinsci.plugins.workflow.multibranch.BranchJobProperty',
                           u'branch': {}},
                          {u'_class': u'com.synopsys.arc.jenkins.plugins.ownership.jobs.JobOwnerJobProperty'}],
            u'queueItem': None,
            u'resumeBlocked': False,
            u'url': u'url'}


def test_parses_job_name(job_data):
    job = parse_job(job_data)
    assert job.name == 'PR-1377'


def test_parses_build_count(job_data):
    job = parse_job(job_data)
    assert job.build_count == 3


def test_parses_full_name(job_data):
    job = parse_job(job_data)
    assert job.full_name == 'fullName'


def test_parses_url(job_data):
    job = parse_job(job_data)
    assert job.url == 'url'
