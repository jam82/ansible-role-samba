import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture
def get_vars(host):
    all_vars = host.ansible.get_variables()
    return all_vars


def test_dns_ldap(host, get_vars):
    if get_vars['samba_role'] == 'domain controller':
        test = 'host -t SRV _ldap._tcp.' + get_vars['samba_domain'] + '.'
        output = host.check_output(test)
        assert '_ldap._tcp.' + get_vars['samba_domain'] + ' has SRV' in output


# def test_dns_kerberos(host):
#     test = 'host -t SRV _kerberos._udp.ad.homebase.localdomain.'
#     output = host.check_output(test)
#     assert '_kerberos._udp.ad.homebase.localdomain has SRV' in output


# def test_dns_a_record(host):
#     hostname = host.check_output('hostname -s')
#     test = "host -t A " + hostname \
#         + ".ad.homebase.localdomain."
#     output = host.check_output(test)
#     assert hostname \
#         + ".ad.homebase.localdomain has address" in output


# def test_reverse_dns(host):
#     facts = host.ansible("setup")["ansible_facts"]
#     ip = facts["ansible_default_ipv4"]["address"]
#     test = "nslookup " + ip
#     output = host.check_output(test)
#     assert "ad.homebase.localdomain" in output


# def test_dns(host):
#     google = host.addr("google.com")
#     assert google.is_resolvable
