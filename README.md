# ansible-role-samba

**Ansible role for setting up samba.**

The supported roles are:

- standalone server
- domain member
- domain controller

> This role does not support to use an ADDC as Fileserver, see [SambaWiki](https://wiki.samba.org/index.php/Setting_up_Samba_as_an_Active_Directory_Domain_Controller#Using_the_Domain_Controller_as_a_File_Server) why this is not a good idea.\
> Therfore the "shares" section is ignored on DCs.

Furthermore you can manage:

- AD/Samba Users and Groups (AD or local depending on the role)
- Printer configuration
- Shares

> This role uses the default method of the targeted distribution
> to configure `/etc/resolv.conf`.

See the following articles for mor informaton:

- [ArchWiki - resolv.conf](https://wiki.archlinux.de/title/Resolv.conf)
- [Archwiki - OpenResolv](https://wiki.archlinux.org/index.php/Openresolv)
- [Debian - resolv.conf](https://wiki.debian.org/resolv.conf)
- [Debian - NetworkConfiguration: Defining the (DNS) Nameservers](https://wiki.debian.org/NetworkConfiguration#Defining_the_.28DNS.29_Nameservers)
- [Ubuntu - resolv.conf](http://manpages.ubuntu.com/manpages/focal/de/man5/resolv.conf.5.html)
- [Ubuntu - resolvconf](http://manpages.ubuntu.com/manpages/focal/man8/resolvconf.8.html)

## Supported Platforms

- Alpine 3.11
- CentOS 8 (no domain controller)
- Debian 9, 10
- Fedora 31
- OpenSuse Leap 15.x
- Ubuntu 18.04, 20.04

At the time of writing following (rolling-release) distributions are
currently broken because of python 3.8 incompatibilities of samba:

- Archlinux
- OpenSuse Tumbleweed

## Requirements

Ansible 2.9 or higher.

## Variables

Variables and defaults for this role:

| variable | default value in defaults/main.yml | description |
| -------- | ---------------------------------- | ----------- |
| samba_role_enabled | False | determine whether role is enabled (True) or not (False) |

## Dependencies

Unless you want to configure `/etc/hosts` and `/etc/resolv.conf` manually,
the following roles are required:

- ansible-role-hosts
- ansible-role-openresolv
- ansible-role-resolveconf
- ansible-role-systemd-resolved

## Example Playbook

```yaml
---
# role: ansible-role-samba
# file: site.yml

- hosts: samba_systems
  become: True
  vars:
    samba_role_enabled: True
  roles:
    - role: ansible-role-samba
```

## License and Author

- Author:: [jam82](https://github.com/jam82/)
- Copyright:: 2020, [jam82](https://github.com/jam82/)

Licensed under [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/jam82/ansible-role-samba/blob/master/LICENSE) file in repository.

## References

- [ArchWiki - Samba](https://wiki.archlinux.org/index.php/Samba)
- [ArchWiki - Samba/Active Directory domain controller](https://wiki.archlinux.org/index.php/Samba/Active_Directory_domain_controller)
- [SambaWiki - Setting up Samba as an Active Directory Domain Controller](https://wiki.samba.org/index.php/Setting_up_Samba_as_an_Active_Directory_Domain_Controller)
- [SambaWiki - Setting up Samba as a Domain Member](https://wiki.samba.org/index.php/Setting_up_Samba_as_an_Active_Directory_Domain_Controller)
- [SambaWiki - The Samba AD DNS Back Ends](https://wiki.samba.org/index.php/The_Samba_AD_DNS_Back_Ends)
- [oO.o's Fedora 30 Samba AD DC Guide](https://forum.level1techs.com/t/oo-os-fedora-30-samba-ad-dc-guide/149475)
