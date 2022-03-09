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


class V1CertificateSigningRequestCondition(object):
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
        'last_transition_time': 'datetime',
        'last_update_time': 'datetime',
        'message': 'str',
        'reason': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'last_transition_time': 'lastTransitionTime',
        'last_update_time': 'lastUpdateTime',
        'message': 'message',
        'reason': 'reason',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, last_transition_time=None, last_update_time=None, message=None, reason=None, status=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1CertificateSigningRequestCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_transition_time = None
        self._last_update_time = None
        self._message = None
        self._reason = None
        self._status = None
        self._type = None
        self.discriminator = None

        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        self.status = status
        self.type = type

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this V1CertificateSigningRequestCondition.  # noqa: E501

        lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time.  # noqa: E501

        :return: The last_transition_time of this V1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this V1CertificateSigningRequestCondition.

        lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time.  # noqa: E501

        :param last_transition_time: The last_transition_time of this V1CertificateSigningRequestCondition.  # noqa: E501
        :type: datetime
        """

        self._last_transition_time = last_transition_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this V1CertificateSigningRequestCondition.  # noqa: E501

        lastUpdateTime is the time of the last update to this condition  # noqa: E501

        :return: The last_update_time of this V1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this V1CertificateSigningRequestCondition.

        lastUpdateTime is the time of the last update to this condition  # noqa: E501

        :param last_update_time: The last_update_time of this V1CertificateSigningRequestCondition.  # noqa: E501
        :type: datetime
        """

        self._last_update_time = last_update_time

    @property
    def message(self):
        """Gets the message of this V1CertificateSigningRequestCondition.  # noqa: E501

        message contains a human readable message with details about the request state  # noqa: E501

        :return: The message of this V1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1CertificateSigningRequestCondition.

        message contains a human readable message with details about the request state  # noqa: E501

        :param message: The message of this V1CertificateSigningRequestCondition.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this V1CertificateSigningRequestCondition.  # noqa: E501

        reason indicates a brief reason for the request state  # noqa: E501

        :return: The reason of this V1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1CertificateSigningRequestCondition.

        reason indicates a brief reason for the request state  # noqa: E501

        :param reason: The reason of this V1CertificateSigningRequestCondition.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this V1CertificateSigningRequestCondition.  # noqa: E501

        status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be \"False\" or \"Unknown\".  # noqa: E501

        :return: The status of this V1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1CertificateSigningRequestCondition.

        status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be \"False\" or \"Unknown\".  # noqa: E501

        :param status: The status of this V1CertificateSigningRequestCondition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this V1CertificateSigningRequestCondition.  # noqa: E501

        type of the condition. Known conditions are \"Approved\", \"Denied\", and \"Failed\".  An \"Approved\" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.  A \"Denied\" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.  A \"Failed\" condition is added via the /status subresource, indicating the signer failed to issue the certificate.  Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.  Only one condition of a given type is allowed.  # noqa: E501

        :return: The type of this V1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1CertificateSigningRequestCondition.

        type of the condition. Known conditions are \"Approved\", \"Denied\", and \"Failed\".  An \"Approved\" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.  A \"Denied\" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.  A \"Failed\" condition is added via the /status subresource, indicating the signer failed to issue the certificate.  Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.  Only one condition of a given type is allowed.  # noqa: E501

        :param type: The type of this V1CertificateSigningRequestCondition.  # noqa: E501
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
        if not isinstance(other, V1CertificateSigningRequestCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CertificateSigningRequestCondition):
            return True

        return self.to_dict() != other.to_dict()
