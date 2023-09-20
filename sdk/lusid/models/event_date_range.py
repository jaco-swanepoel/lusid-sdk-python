# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.534
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class EventDateRange(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'start': 'datetime',
        'end': 'datetime'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end'
    }

    required_map = {
        'start': 'optional',
        'end': 'optional'
    }

    def __init__(self, start=None, end=None, local_vars_configuration=None):  # noqa: E501
        """EventDateRange - a model defined in OpenAPI"
        
        :param start: 
        :type start: datetime
        :param end: 
        :type end: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start = None
        self._end = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def start(self):
        """Gets the start of this EventDateRange.  # noqa: E501


        :return: The start of this EventDateRange.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this EventDateRange.


        :param start: The start of this EventDateRange.  # noqa: E501
        :type start: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this EventDateRange.  # noqa: E501


        :return: The end of this EventDateRange.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this EventDateRange.


        :param end: The end of this EventDateRange.  # noqa: E501
        :type end: datetime
        """

        self._end = end

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
        if not isinstance(other, EventDateRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventDateRange):
            return True

        return self.to_dict() != other.to_dict()
