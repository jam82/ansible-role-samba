import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fileserver(host):
    test = 'smbclient -L localhost -U%'
    output = host.check_output(test)
    assert 'Sharename' in output
    assert 'netlogon' in output
    assert 'sysvol' in output
    assert 'IPC$' in output
