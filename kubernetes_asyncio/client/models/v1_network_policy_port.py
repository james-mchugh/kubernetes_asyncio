# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.11
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1NetworkPolicyPort(object):
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
        'end_port': 'int',
        'port': 'object',
        'protocol': 'str'
    }

    attribute_map = {
        'end_port': 'endPort',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, end_port=None, port=None, protocol=None, local_vars_configuration=None):  # noqa: E501
        """V1NetworkPolicyPort - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._end_port = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if end_port is not None:
            self.end_port = end_port
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def end_port(self):
        """Gets the end_port of this V1NetworkPolicyPort.  # noqa: E501

        If set, indicates that the range of ports from port to endPort, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port.  # noqa: E501

        :return: The end_port of this V1NetworkPolicyPort.  # noqa: E501
        :rtype: int
        """
        return self._end_port

    @end_port.setter
    def end_port(self, end_port):
        """Sets the end_port of this V1NetworkPolicyPort.

        If set, indicates that the range of ports from port to endPort, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port.  # noqa: E501

        :param end_port: The end_port of this V1NetworkPolicyPort.  # noqa: E501
        :type end_port: int
        """

        self._end_port = end_port

    @property
    def port(self):
        """Gets the port of this V1NetworkPolicyPort.  # noqa: E501

        The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.  # noqa: E501

        :return: The port of this V1NetworkPolicyPort.  # noqa: E501
        :rtype: object
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this V1NetworkPolicyPort.

        The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.  # noqa: E501

        :param port: The port of this V1NetworkPolicyPort.  # noqa: E501
        :type port: object
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this V1NetworkPolicyPort.  # noqa: E501

        The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  # noqa: E501

        :return: The protocol of this V1NetworkPolicyPort.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this V1NetworkPolicyPort.

        The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.  # noqa: E501

        :param protocol: The protocol of this V1NetworkPolicyPort.  # noqa: E501
        :type protocol: str
        """

        self._protocol = protocol

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1NetworkPolicyPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1NetworkPolicyPort):
            return True

        return self.to_dict() != other.to_dict()
