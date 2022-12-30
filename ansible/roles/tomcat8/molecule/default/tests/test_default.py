import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_tomcat_service_exists(host):
    assert host.file("/etc/systemd/system/tomcat.service").exists


def test_tomcat_folder_exists(host):
    assert host.file("/opt/tomcat").exists
