# Ansible Role: Meteor

An Ansible role that installs or updates [Meteor](https://www.meteor.com/), a full-stack Javascript framework.

## Requirements

None.

## Role Variables

| Variable                 | Description | Default |
|--------------------------|-------------|---------|
| `meteor_group`            | Name of meteor system group | `meteor` |
| `meteor_home`             | Path to meteor user's home  | `/usr/local/meteor` |
| `meteor_install_tmpdir`   | Temporary directory used to fetch meteor releases | `/tmp/meteor` |
| `meteor_release`          | Meteor release to install  | mandatory |
| `meteor_url`              | Where to download Meteor from | `https://static-meteor.netdna-ssl.com/packages-bootstrap/{{ __meteor_release }}/meteor-bootstrap-os.linux.x86_64.tar.gz` |
| `meteor_user`             | Name of meteor system user  | `meteor` |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: wekan
  vars:
    meteor_release: '2.0'
    meteor_url: 'https://nexus.example.org/repository/shared-files/meteor/meteor-{{ meteor_release }}.tar.gz'
  roles:
     - role: deveryware.meteor
```

## License

ISC

## Contributing

[Github pull requests](https://github.com/Deveryware/ansible-role-meteor) are gladly accepted.

## Author Information

Tristan Le Guern <tristan.leguern-presta@deveryware.com> for Deveryware.
