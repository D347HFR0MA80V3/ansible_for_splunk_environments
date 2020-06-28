import takeltest
import testinfra.utils.ansible_runner


testinfra_hosts = takeltest.hosts()


def test_user_config_settings(host, testvars):
  # splunk_user already tested in test_detect_splunk.py
  v = testvars['splunk_all_user_home']
  assert v == '/home/splunk'
  assert host.user('splunk').home == '/home/splunk'
  v = testvars['splunk_all_user_shell']
  assert v == '/bin/bash'
  assert host.user('splunk').shell == '/bin/bash'


def test_user_config_templates(host, testvars):
  # user_home var already tested above
  # splunk_user var already tested in test_detect_splunk.py
  v = testvars['splunk_all_splunk_group']
  assert v == 'splunk'
  assert host.user('splunk').group == 'splunk'
  v = testvars['splunk_all_file_mode']
  assert v == '0644'
  assert host.file('/home/splunk/.bashrc').exists
  assert host.file('/home/splunk/.bashrc').group == 'splunk'
  assert host.file('/home/splunk/.bashrc').user == 'splunk'
  assert host.file('/home/splunk/.bash_logout').exists
  assert host.file('/home/splunk/.bash_logout').group == 'splunk'
  assert host.file('/home/splunk/.bash_logout').user == 'splunk'
