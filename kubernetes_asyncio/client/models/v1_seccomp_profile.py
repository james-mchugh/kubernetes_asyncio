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


class V1SeccompProfile(object):
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
        'localhost_profile': 'str',
        'type': 'str'
    }

    attribute_map = {
        'localhost_profile': 'localhostProfile',
        'type': 'type'
    }

    def __init__(self, localhost_profile=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1SeccompProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._localhost_profile = None
        self._type = None
        self.discriminator = None

        if localhost_profile is not None:
            self.localhost_profile = localhost_profile
        self.type = type

    @property
    def localhost_profile(self):
        """Gets the localhost_profile of this V1SeccompProfile.  # noqa: E501

        localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must only be set if type is \"Localhost\".  # noqa: E501

        :return: The localhost_profile of this V1SeccompProfile.  # noqa: E501
        :rtype: str
        """
        return self._localhost_profile

    @localhost_profile.setter
    def localhost_profile(self, localhost_profile):
        """Sets the localhost_profile of this V1SeccompProfile.

        localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must only be set if type is \"Localhost\".  # noqa: E501

        :param localhost_profile: The localhost_profile of this V1SeccompProfile.  # noqa: E501
        :type: str
        """

        self._localhost_profile = localhost_profile

    @property
    def type(self):
        """Gets the type of this V1SeccompProfile.  # noqa: E501

        type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.  # noqa: E501

        :return: The type of this V1SeccompProfile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1SeccompProfile.

        type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.  # noqa: E501

        :param type: The type of this V1SeccompProfile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V1SeccompProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SeccompProfile):
            return True

        return self.to_dict() != other.to_dict()
