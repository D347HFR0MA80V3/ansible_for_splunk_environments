# Ansible for Splunk Environments

[![Build Status](https://travis-ci.org/D347HFR0MA80V3/ansible_for_splunk_environments.svg?branch=master)](https://travis-ci.org/D347HFR0MA80V3/ansible_for_splunk_environments)
[![Ansible Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://docs.ansible.com/ansible/latest/)
[![Molecule Docs](https://readthedocs.org/projects/molecule/badge/?version=latest)](https://molecule.readthedocs.io/en/latest/)
[![Testinfra Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://testinfra.readthedocs.io/en/latest)

Description
===========

A collection of molecule initalized roles for instantiating and maintaining Splunk environments. Designed by sharks for professional services engagements. Serves as a structured framework to make ansible easily approachable.

Dependencies
============

This project utilizes several Ansible centric open source efforts...

- Molecule
- Testinfra
- Pytest
- Takeltest

Roles
=====

- [splunk_all](../roles/splunk_all/README.md)
: Role containing tasks that apply to all Splunk environment nodes.
- [splunk_ds](../roles/splunk_ds/README.md)
: Role containing tasks that apply to Splunk Deployment Servers.
- [splunk_idx](../roles/splunk_idx/README.md)
: Role containing tasks that apply to Splunk Indexers. Whether clustered or not.
- [splunk_sh](../roles/splunk_sh/README.md)
: Role containing tasks that apply to Splunk Search Heads. Whether clustered or not. 


How to use
==========

