# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.13
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1IPBlock(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cidr': 'str',
        '_except': 'list[str]'
    }

    attribute_map = {
        'cidr': 'cidr',
        '_except': 'except'
    }

    def __init__(self, cidr=None, _except=None, local_vars_configuration=None):  # noqa: E501
        """V1IPBlock - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cidr = None
        self.__except = None
        self.discriminator = None

        self.cidr = cidr
        if _except is not None:
            self._except = _except

    @property
    def cidr(self):
        """Gets the cidr of this V1IPBlock.  # noqa: E501

        CIDR is a string representing the IP Block Valid examples are \"192.168.1.1/24\" or \"2001:db9::/64\"  # noqa: E501

        :return: The cidr of this V1IPBlock.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this V1IPBlock.

        CIDR is a string representing the IP Block Valid examples are \"192.168.1.1/24\" or \"2001:db9::/64\"  # noqa: E501

        :param cidr: The cidr of this V1IPBlock.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cidr is None:  # noqa: E501
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501

        self._cidr = cidr

    @property
    def _except(self):
        """Gets the _except of this V1IPBlock.  # noqa: E501

        Except is a slice of CIDRs that should not be included within an IP Block Valid examples are \"192.168.1.1/24\" or \"2001:db9::/64\" Except values will be rejected if they are outside the CIDR range  # noqa: E501

        :return: The _except of this V1IPBlock.  # noqa: E501
        :rtype: list[str]
        """
        return self.__except

    @_except.setter
    def _except(self, _except):
        """Sets the _except of this V1IPBlock.

        Except is a slice of CIDRs that should not be included within an IP Block Valid examples are \"192.168.1.1/24\" or \"2001:db9::/64\" Except values will be rejected if they are outside the CIDR range  # noqa: E501

        :param _except: The _except of this V1IPBlock.  # noqa: E501
        :type: list[str]
        """

        self.__except = _except

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1IPBlock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1IPBlock):
            return True

        return self.to_dict() != other.to_dict()
