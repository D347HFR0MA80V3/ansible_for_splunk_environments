import takeltest


testinfra_hosts = takeltest.hosts()


def test_admin_login(host, testvars):
    v = testvars['splunk_all_fips_mode']
    assert v == 'false'
    assert not host.file(
        "/opt/splunk/etc/splunk-launch.conf").contains('SPLUNK_FIPS = true')
