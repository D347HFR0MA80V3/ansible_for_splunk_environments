import takeltest


testinfra_hosts = takeltest.hosts()


def test_web_config_variables(host, testvars):
    v = testvars['splunk_all_web_config_secure_web']
    assert v is False
    v = testvars['splunk_all_web_config_http_port']
    assert v == '8000'
    v = testvars['splunk_all_web_config_start_web']
    assert v == '1'
    v = testvars['splunk_all_web_config_check_update']
    assert v == '0'
    v = testvars['splunk_all_web_config_ssl_enable']
    assert v == 'true'
    v = testvars['splunk_all_web_config_ssl_versions']
    assert v == 'tls1.2'


def test_web_config_results(host, testvars):
    assert host.file("/opt/splunk/etc/apps/z_defaults-web_config").is_directory
    assert host.file('/opt/splunk/etc/apps/z_defaults-web_config/default').is_directory
    assert host.file('/opt/splunk/etc/apps/z_defaults-web_config/metadata').is_directory
    assert host.file('/opt/splunk/etc/apps/z_defaults-web_config/default/app.conf').md5sum == 'd13267f5501fe375d7139d13d594c318'
    assert host.file('/opt/splunk/etc/apps/z_defaults-web_config/default/web.conf').md5sum == '648e9a25f4e5f64e2e37e8c39336bd49'
    assert host.file('/opt/splunk/etc/apps/z_defaults-web_config/metadata/default.meta').md5sum == '73a29e7af6c9973b2f8864fbc7b0161a'
