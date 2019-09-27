"""
    SoftLayer.autoscale
    ~~~~~~~~~~~~
    Autoscale manager

    :license: MIT, see LICENSE for more details.
"""


class AutoScaleManager(object):
    """Manager for interacting with Autoscale instances."""

    def __init__(self, client):
        self.client = client

    def list(self, mask=None):
        """Calls SoftLayer_Account getScaleGroups()_

        :param mask: optional SoftLayer_Scale_Group objectMask
        .. getScaleGroups(): https://sldn.softlayer.com/reference/services/SoftLayer_Account/getScaleGroups/
        """
        if not mask:
            mask = "mask[status,virtualGuestMemberCount]"

        return self.client.call('SoftLayer_Account', 'getScaleGroups', mask=mask, iter=True)

    def details(self, identifier, mask=None):
        """Calls SoftLayer_Scale_Group getObject()_

        :param identifier: SoftLayer_Scale_Group id
        :param mask: optional SoftLayer_Scale_Group objectMask
        .. _getObject(): https://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/getObject/
        """
        if not mask:
            mask = """mask[virtualGuestMembers[id,virtualGuest[hostname,domain,provisionDate]], terminationPolicy,
                   virtualGuestMemberCount, virtualGuestMemberTemplate[sshKeys],
                   policies[id,name,createDate,cooldown,actions,triggers,scaleActions],
                   networkVlans[networkVlanId,networkVlan[networkSpace,primaryRouter[hostname]]],
                   loadBalancers, regionalGroup[locations]]"""
        return self.client.call('SoftLayer_Scale_Group', 'getObject', id=identifier, mask=mask)

    def get_policy(self, identifier, mask=None):
        """Calls SoftLayer_Scale_Policy getObject()_

        :param identifier: SoftLayer_Scale_Policy id
        :param mask: optional SoftLayer_Scale_Policy objectMask
        .. _getObject(): https://sldn.softlayer.com/reference/services/SoftLayer_Scale_Policy/getObject/
        """
        if not mask:
            mask = """mask[cooldown, createDate, id, name, actions, triggers[type]

            ]"""

        return self.client.call('SoftLayer_Scale_Policy', 'getObject', id=identifier, mask=mask)

    def scale(self, identifier, amount):
        """Calls SoftLayer_Scale_Group scale()_

        :param identifier: SoftLayer_Scale_Group Id
        :param amount: positive or negative number to scale the group by

        .. _scale(): https://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/scale/
        """
        return self.client.call('SoftLayer_Scale_Group', 'scale', amount, id=identifier)

    def scale_to(self, identifier, amount):
        """Calls SoftLayer_Scale_Group scaleTo()_

        :param identifier: SoftLayer_Scale_Group Id
        :param amount: number to scale the group to.
        .. _scaleTo(): https://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/scaleTo/
        """
        return self.client.call('SoftLayer_Scale_Group', 'scaleTo', amount, id=identifier)

    def get_logs(self, identifier, mask=None, object_filter=None):
        """Calls SoftLayer_Scale_Group getLogs()_

        :param identifier: SoftLayer_Scale_Group Id
        :param mask: optional SoftLayer_Scale_Group_Log objectMask
        :param object_filter: optional SoftLayer_Scale_Group_Log objectFilter
        .. getLogs(): https://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/getLogs/
        """
        return self.client.call('SoftLayer_Scale_Group', 'getLogs', id=identifier, mask=mask, filter=object_filter,
                                iter=True)
