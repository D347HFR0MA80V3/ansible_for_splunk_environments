import glob
import takeltest
import testinfra.utils.ansible_runner


testinfra_hosts = takeltest.hosts()


def test_detect_splunk_user(host, testvars):
    v = testvars['splunk_all_splunk_user']
    assert v == "splunk"
    assert host.user('splunk').exists


def test_detect_splunk_home(host, testvars):
    v = testvars['splunk_all_splunk_home']
    assert v == "/opt/splunk"
    assert host.file('/opt/splunk').is_directory
    assert host.file('/opt/splunk').user == "splunk"
    assert host.file('/opt/splunk').group == "splunk"
    assert host.file('/opt/splunk').mode == 0o755


def test_detect_splunk_install(host, testvars):
    glob.glob('/opt/splunk/splunk-*-manifest')


def test_detect_splunk_status(host, testvars):
    v = testvars['splunk_all_cli_command']
    assert v == "/opt/splunk/bin/splunk"
    assert host.file('/opt/splunk/bin/splunk').exists
