#!/usr/bin/python
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError


def meteor_version(version):
    if version.find('-') != -1:
        release, label = version.split('-')
    else:
        release = version
        label = ""
    if len(release.split('.')) == 2:
        release = release + '.0'
    if label:
        release = release + '-' + label
    return release


class FilterModule(object):
    '''Meteor version filter '''

    def filters(self):
        return {
            'meteor_version': meteor_version
        }
