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


class V1PodAntiAffinity(object):
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
        'preferred_during_scheduling_ignored_during_execution': 'list[V1WeightedPodAffinityTerm]',
        'required_during_scheduling_ignored_during_execution': 'list[V1PodAffinityTerm]'
    }

    attribute_map = {
        'preferred_during_scheduling_ignored_during_execution': 'preferredDuringSchedulingIgnoredDuringExecution',
        'required_during_scheduling_ignored_during_execution': 'requiredDuringSchedulingIgnoredDuringExecution'
    }

    def __init__(self, preferred_during_scheduling_ignored_during_execution=None, required_during_scheduling_ignored_during_execution=None, local_vars_configuration=None):  # noqa: E501
        """V1PodAntiAffinity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._preferred_during_scheduling_ignored_during_execution = None
        self._required_during_scheduling_ignored_during_execution = None
        self.discriminator = None

        if preferred_during_scheduling_ignored_during_execution is not None:
            self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

    @property
    def preferred_during_scheduling_ignored_during_execution(self):
        """Gets the preferred_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.  # noqa: E501

        The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.  # noqa: E501

        :return: The preferred_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.  # noqa: E501
        :rtype: list[V1WeightedPodAffinityTerm]
        """
        return self._preferred_during_scheduling_ignored_during_execution

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution):
        """Sets the preferred_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.

        The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.  # noqa: E501

        :param preferred_during_scheduling_ignored_during_execution: The preferred_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.  # noqa: E501
        :type preferred_during_scheduling_ignored_during_execution: list[V1WeightedPodAffinityTerm]
        """

        self._preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    @property
    def required_during_scheduling_ignored_during_execution(self):
        """Gets the required_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.  # noqa: E501

        If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.  # noqa: E501

        :return: The required_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.  # noqa: E501
        :rtype: list[V1PodAffinityTerm]
        """
        return self._required_during_scheduling_ignored_during_execution

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution):
        """Sets the required_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.

        If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.  # noqa: E501

        :param required_during_scheduling_ignored_during_execution: The required_during_scheduling_ignored_during_execution of this V1PodAntiAffinity.  # noqa: E501
        :type required_during_scheduling_ignored_during_execution: list[V1PodAffinityTerm]
        """

        self._required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

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
        if not isinstance(other, V1PodAntiAffinity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodAntiAffinity):
            return True

        return self.to_dict() != other.to_dict()
