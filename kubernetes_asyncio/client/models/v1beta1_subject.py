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


class V1beta1Subject(object):
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
        'group': 'V1beta1GroupSubject',
        'kind': 'str',
        'service_account': 'V1beta1ServiceAccountSubject',
        'user': 'V1beta1UserSubject'
    }

    attribute_map = {
        'group': 'group',
        'kind': 'kind',
        'service_account': 'serviceAccount',
        'user': 'user'
    }

    def __init__(self, group=None, kind=None, service_account=None, user=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1Subject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._kind = None
        self._service_account = None
        self._user = None
        self.discriminator = None

        if group is not None:
            self.group = group
        self.kind = kind
        if service_account is not None:
            self.service_account = service_account
        if user is not None:
            self.user = user

    @property
    def group(self):
        """Gets the group of this V1beta1Subject.  # noqa: E501


        :return: The group of this V1beta1Subject.  # noqa: E501
        :rtype: V1beta1GroupSubject
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1beta1Subject.


        :param group: The group of this V1beta1Subject.  # noqa: E501
        :type group: V1beta1GroupSubject
        """

        self._group = group

    @property
    def kind(self):
        """Gets the kind of this V1beta1Subject.  # noqa: E501

        `kind` indicates which one of the other fields is non-empty. Required  # noqa: E501

        :return: The kind of this V1beta1Subject.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1beta1Subject.

        `kind` indicates which one of the other fields is non-empty. Required  # noqa: E501

        :param kind: The kind of this V1beta1Subject.  # noqa: E501
        :type kind: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def service_account(self):
        """Gets the service_account of this V1beta1Subject.  # noqa: E501


        :return: The service_account of this V1beta1Subject.  # noqa: E501
        :rtype: V1beta1ServiceAccountSubject
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this V1beta1Subject.


        :param service_account: The service_account of this V1beta1Subject.  # noqa: E501
        :type service_account: V1beta1ServiceAccountSubject
        """

        self._service_account = service_account

    @property
    def user(self):
        """Gets the user of this V1beta1Subject.  # noqa: E501


        :return: The user of this V1beta1Subject.  # noqa: E501
        :rtype: V1beta1UserSubject
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1beta1Subject.


        :param user: The user of this V1beta1Subject.  # noqa: E501
        :type user: V1beta1UserSubject
        """

        self._user = user

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
        if not isinstance(other, V1beta1Subject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1Subject):
            return True

        return self.to_dict() != other.to_dict()
