import takeltest


testinfra_hosts = takeltest.hosts()


def test_admin_login(host, testvars):
    v = testvars['splunk_all_general_p4sk']
    assert v == 'changeme'
