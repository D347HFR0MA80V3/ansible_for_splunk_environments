splunk_all
==========

[Home](../../docs/README.md)

This role contains tasks that need to be performed on all Splunk Enterprise nodes within an environment. It is all the origin for all default variables that need to be available to other roles. All other roles will have a dependency on at least this role.

Requirements
------------

It is not a requirement but this collection of roles makes use of the Mitogen for Ansible project. Ensure you have the matching version of Mitogen for the Ansible version you are using to execute these roles.

Role Variables
--------------

```yaml
splunk_all_default_prefix: 'z_shark_defaults'
splunk_all_cli_command: '/opt/splunk/bin/splunk'
splunk_all_dir_mode: '0755'
splunk_all_file_mode: '0644'
splunk_all_mgmt_port: '8089'
splunk_all_web_port: '8000'
splunk_all_splunk_user: 'splunk'
splunk_all_splunk_group: 'splunk'
splunk_all_splunk_appspath: '/opt/splunk/etc/apps'
splunk_all_splunk_dappspath: '/opt/splunk/etc/deployment-apps'
splunk_all_splunk_mappspath: '/opt/splunk/etc/master-apps'
splunk_all_splunk_shappspath: '/opt/splunk/etc/shcluster/apps'
```

Dependencies
------------

This role is the base dependency for all other roles. It contains tasks to be run on all nodes in an environment. It also serves as the origin of variables that should be universal in an environment so that they are available for use by other dependent roles.

Launch Playbook
----------------

```yaml
- hosts: "{{ target }}"
  become: yes
  become_method: sudo
  become_user: "{{ splunk_all_splunk_user }}"
  gather_facts: yes
  vars_prompt:
    - name: "target"
      prompt: "Specify target group(s) and / or host(s)"
      private: no
    - name: "splunk_admin_username"
      prompt: "Input an administrator username"
      private: no
    - name: "splunk_admin_password"
      prompt: "Input the administrative user password"
      private: yes
      no_log: yes
  roles:
    - splunk_all
```

License
-------

BSD

Author Information
------------------

Lee Goodrich - ClearShark Sytems Engineer
