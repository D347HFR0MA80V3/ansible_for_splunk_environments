import os
import pytest
import takeltest
import testinfra.utils.ansible_runner


testinfra_hosts = takeltest.hosts()


def test_detect_splunk(host, testvars):
    v = testvars['splunk_all_splunk_user']
    assert host.user('splunk').exists
    assert host.user(v).name == "splunk"
