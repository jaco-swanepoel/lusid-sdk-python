# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3236
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Version(object):
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
        'effective_from': 'datetime',
        'as_at_date': 'datetime'
    }

    attribute_map = {
        'effective_from': 'effectiveFrom',
        'as_at_date': 'asAtDate'
    }

    required_map = {
        'effective_from': 'required',
        'as_at_date': 'required'
    }

    def __init__(self, effective_from=None, as_at_date=None):  # noqa: E501
        """
        Version - a model defined in OpenAPI

        :param effective_from:  The effective datetime at which this version became valid. Only applies when a single entity is being interacted with. (required)
        :type effective_from: datetime
        :param as_at_date:  The asAt datetime at which the data was committed to LUSID. (required)
        :type as_at_date: datetime

        """  # noqa: E501

        self._effective_from = None
        self._as_at_date = None
        self.discriminator = None

        self.effective_from = effective_from
        self.as_at_date = as_at_date

    @property
    def effective_from(self):
        """Gets the effective_from of this Version.  # noqa: E501

        The effective datetime at which this version became valid. Only applies when a single entity is being interacted with.  # noqa: E501

        :return: The effective_from of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this Version.

        The effective datetime at which this version became valid. Only applies when a single entity is being interacted with.  # noqa: E501

        :param effective_from: The effective_from of this Version.  # noqa: E501
        :type: datetime
        """
        if effective_from is None:
            raise ValueError("Invalid value for `effective_from`, must not be `None`")  # noqa: E501

        self._effective_from = effective_from

    @property
    def as_at_date(self):
        """Gets the as_at_date of this Version.  # noqa: E501

        The asAt datetime at which the data was committed to LUSID.  # noqa: E501

        :return: The as_at_date of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_date

    @as_at_date.setter
    def as_at_date(self, as_at_date):
        """Sets the as_at_date of this Version.

        The asAt datetime at which the data was committed to LUSID.  # noqa: E501

        :param as_at_date: The as_at_date of this Version.  # noqa: E501
        :type: datetime
        """
        if as_at_date is None:
            raise ValueError("Invalid value for `as_at_date`, must not be `None`")  # noqa: E501

        self._as_at_date = as_at_date

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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
