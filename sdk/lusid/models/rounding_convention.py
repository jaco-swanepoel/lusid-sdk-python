# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.475
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


class RoundingConvention(object):
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
        'face_value': 'float',
        'precision': 'int',
        'rounding_target': 'str',
        'rounding_type': 'str'
    }

    attribute_map = {
        'face_value': 'faceValue',
        'precision': 'precision',
        'rounding_target': 'roundingTarget',
        'rounding_type': 'roundingType'
    }

    required_map = {
        'face_value': 'optional',
        'precision': 'optional',
        'rounding_target': 'optional',
        'rounding_type': 'optional'
    }

    def __init__(self, face_value=None, precision=None, rounding_target=None, rounding_type=None, local_vars_configuration=None):  # noqa: E501
        """RoundingConvention - a model defined in OpenAPI"
        
        :param face_value:  The face value to round against.  The number to be rounded is scaled to this face value before being rounded, and then re-scaled to the holding amount.  For example if rounding an accrued interest value using a FaceValue of 1,000, but 10,000 units are held,  then the initial calculated value would be divided by 10,000, then multiplied by 1,000 and rounded per the convention.  The result of this would then be divided by 1,000 and multiplied by 10,000 to get the final value.
        :type face_value: float
        :param precision:  The precision of the rounding.  The decimal places to which the rounding takes place.
        :type precision: int
        :param rounding_target:  The target of the rounding convention.  Accepted values are 'AccruedInterest', 'Cashflows', or 'All'    Supported string (enumeration) values are: [All, AccruedInterest, Cashflows].
        :type rounding_target: str
        :param rounding_type:  The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Floor, Ceiling, Nearest].
        :type rounding_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._face_value = None
        self._precision = None
        self._rounding_target = None
        self._rounding_type = None
        self.discriminator = None

        if face_value is not None:
            self.face_value = face_value
        if precision is not None:
            self.precision = precision
        self.rounding_target = rounding_target
        self.rounding_type = rounding_type

    @property
    def face_value(self):
        """Gets the face_value of this RoundingConvention.  # noqa: E501

        The face value to round against.  The number to be rounded is scaled to this face value before being rounded, and then re-scaled to the holding amount.  For example if rounding an accrued interest value using a FaceValue of 1,000, but 10,000 units are held,  then the initial calculated value would be divided by 10,000, then multiplied by 1,000 and rounded per the convention.  The result of this would then be divided by 1,000 and multiplied by 10,000 to get the final value.  # noqa: E501

        :return: The face_value of this RoundingConvention.  # noqa: E501
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this RoundingConvention.

        The face value to round against.  The number to be rounded is scaled to this face value before being rounded, and then re-scaled to the holding amount.  For example if rounding an accrued interest value using a FaceValue of 1,000, but 10,000 units are held,  then the initial calculated value would be divided by 10,000, then multiplied by 1,000 and rounded per the convention.  The result of this would then be divided by 1,000 and multiplied by 10,000 to get the final value.  # noqa: E501

        :param face_value: The face_value of this RoundingConvention.  # noqa: E501
        :type face_value: float
        """

        self._face_value = face_value

    @property
    def precision(self):
        """Gets the precision of this RoundingConvention.  # noqa: E501

        The precision of the rounding.  The decimal places to which the rounding takes place.  # noqa: E501

        :return: The precision of this RoundingConvention.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this RoundingConvention.

        The precision of the rounding.  The decimal places to which the rounding takes place.  # noqa: E501

        :param precision: The precision of this RoundingConvention.  # noqa: E501
        :type precision: int
        """

        self._precision = precision

    @property
    def rounding_target(self):
        """Gets the rounding_target of this RoundingConvention.  # noqa: E501

        The target of the rounding convention.  Accepted values are 'AccruedInterest', 'Cashflows', or 'All'    Supported string (enumeration) values are: [All, AccruedInterest, Cashflows].  # noqa: E501

        :return: The rounding_target of this RoundingConvention.  # noqa: E501
        :rtype: str
        """
        return self._rounding_target

    @rounding_target.setter
    def rounding_target(self, rounding_target):
        """Sets the rounding_target of this RoundingConvention.

        The target of the rounding convention.  Accepted values are 'AccruedInterest', 'Cashflows', or 'All'    Supported string (enumeration) values are: [All, AccruedInterest, Cashflows].  # noqa: E501

        :param rounding_target: The rounding_target of this RoundingConvention.  # noqa: E501
        :type rounding_target: str
        """

        self._rounding_target = rounding_target

    @property
    def rounding_type(self):
        """Gets the rounding_type of this RoundingConvention.  # noqa: E501

        The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Floor, Ceiling, Nearest].  # noqa: E501

        :return: The rounding_type of this RoundingConvention.  # noqa: E501
        :rtype: str
        """
        return self._rounding_type

    @rounding_type.setter
    def rounding_type(self, rounding_type):
        """Sets the rounding_type of this RoundingConvention.

        The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Floor, Ceiling, Nearest].  # noqa: E501

        :param rounding_type: The rounding_type of this RoundingConvention.  # noqa: E501
        :type rounding_type: str
        """

        self._rounding_type = rounding_type

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
        if not isinstance(other, RoundingConvention):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoundingConvention):
            return True

        return self.to_dict() != other.to_dict()
