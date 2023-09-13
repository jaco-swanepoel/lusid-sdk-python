# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.503
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


class Compounding(object):
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
        'calculation_shift_method': 'str',
        'compounding_method': 'str',
        'reset_frequency': 'str',
        'shift': 'int',
        'spread_compounding_method': 'str'
    }

    attribute_map = {
        'calculation_shift_method': 'calculationShiftMethod',
        'compounding_method': 'compoundingMethod',
        'reset_frequency': 'resetFrequency',
        'shift': 'shift',
        'spread_compounding_method': 'spreadCompoundingMethod'
    }

    required_map = {
        'calculation_shift_method': 'optional',
        'compounding_method': 'required',
        'reset_frequency': 'required',
        'shift': 'optional',
        'spread_compounding_method': 'required'
    }

    def __init__(self, calculation_shift_method=None, compounding_method=None, reset_frequency=None, shift=None, spread_compounding_method=None, local_vars_configuration=None):  # noqa: E501
        """Compounding - a model defined in OpenAPI"
        
        :param calculation_shift_method:  Defines which resets and day counts are used for the rate calculation    Supported string (enumeration) values are: [Lookback, NoShift, ObservationPeriodShift, Lockout].
        :type calculation_shift_method: str
        :param compounding_method:  If the interest rate is simple or compounded.    Supported string (enumeration) values are: [Average, Compounded]. (required)
        :type compounding_method: str
        :param reset_frequency:  The interest payment frequency. (required)
        :type reset_frequency: str
        :param shift:  Defines the number of days to lockout or shift observation period by - should be a non-negative integer
        :type shift: int
        :param spread_compounding_method:  Defines how the computed leg spread is applied to compounded rate.  It applies only when CompoundingMethod = ‘Compounded‘.    Supported string (enumeration) values are: [Straight, IsdaCompounding, NoCompounding, SpreadExclusive, IsdaFlatCompounding, Flat, None]. (required)
        :type spread_compounding_method: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._calculation_shift_method = None
        self._compounding_method = None
        self._reset_frequency = None
        self._shift = None
        self._spread_compounding_method = None
        self.discriminator = None

        self.calculation_shift_method = calculation_shift_method
        self.compounding_method = compounding_method
        self.reset_frequency = reset_frequency
        if shift is not None:
            self.shift = shift
        self.spread_compounding_method = spread_compounding_method

    @property
    def calculation_shift_method(self):
        """Gets the calculation_shift_method of this Compounding.  # noqa: E501

        Defines which resets and day counts are used for the rate calculation    Supported string (enumeration) values are: [Lookback, NoShift, ObservationPeriodShift, Lockout].  # noqa: E501

        :return: The calculation_shift_method of this Compounding.  # noqa: E501
        :rtype: str
        """
        return self._calculation_shift_method

    @calculation_shift_method.setter
    def calculation_shift_method(self, calculation_shift_method):
        """Sets the calculation_shift_method of this Compounding.

        Defines which resets and day counts are used for the rate calculation    Supported string (enumeration) values are: [Lookback, NoShift, ObservationPeriodShift, Lockout].  # noqa: E501

        :param calculation_shift_method: The calculation_shift_method of this Compounding.  # noqa: E501
        :type calculation_shift_method: str
        """

        self._calculation_shift_method = calculation_shift_method

    @property
    def compounding_method(self):
        """Gets the compounding_method of this Compounding.  # noqa: E501

        If the interest rate is simple or compounded.    Supported string (enumeration) values are: [Average, Compounded].  # noqa: E501

        :return: The compounding_method of this Compounding.  # noqa: E501
        :rtype: str
        """
        return self._compounding_method

    @compounding_method.setter
    def compounding_method(self, compounding_method):
        """Sets the compounding_method of this Compounding.

        If the interest rate is simple or compounded.    Supported string (enumeration) values are: [Average, Compounded].  # noqa: E501

        :param compounding_method: The compounding_method of this Compounding.  # noqa: E501
        :type compounding_method: str
        """
        if self.local_vars_configuration.client_side_validation and compounding_method is None:  # noqa: E501
            raise ValueError("Invalid value for `compounding_method`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                compounding_method is not None and len(compounding_method) < 1):
            raise ValueError("Invalid value for `compounding_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._compounding_method = compounding_method

    @property
    def reset_frequency(self):
        """Gets the reset_frequency of this Compounding.  # noqa: E501

        The interest payment frequency.  # noqa: E501

        :return: The reset_frequency of this Compounding.  # noqa: E501
        :rtype: str
        """
        return self._reset_frequency

    @reset_frequency.setter
    def reset_frequency(self, reset_frequency):
        """Sets the reset_frequency of this Compounding.

        The interest payment frequency.  # noqa: E501

        :param reset_frequency: The reset_frequency of this Compounding.  # noqa: E501
        :type reset_frequency: str
        """
        if self.local_vars_configuration.client_side_validation and reset_frequency is None:  # noqa: E501
            raise ValueError("Invalid value for `reset_frequency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reset_frequency is not None and len(reset_frequency) < 1):
            raise ValueError("Invalid value for `reset_frequency`, length must be greater than or equal to `1`")  # noqa: E501

        self._reset_frequency = reset_frequency

    @property
    def shift(self):
        """Gets the shift of this Compounding.  # noqa: E501

        Defines the number of days to lockout or shift observation period by - should be a non-negative integer  # noqa: E501

        :return: The shift of this Compounding.  # noqa: E501
        :rtype: int
        """
        return self._shift

    @shift.setter
    def shift(self, shift):
        """Sets the shift of this Compounding.

        Defines the number of days to lockout or shift observation period by - should be a non-negative integer  # noqa: E501

        :param shift: The shift of this Compounding.  # noqa: E501
        :type shift: int
        """

        self._shift = shift

    @property
    def spread_compounding_method(self):
        """Gets the spread_compounding_method of this Compounding.  # noqa: E501

        Defines how the computed leg spread is applied to compounded rate.  It applies only when CompoundingMethod = ‘Compounded‘.    Supported string (enumeration) values are: [Straight, IsdaCompounding, NoCompounding, SpreadExclusive, IsdaFlatCompounding, Flat, None].  # noqa: E501

        :return: The spread_compounding_method of this Compounding.  # noqa: E501
        :rtype: str
        """
        return self._spread_compounding_method

    @spread_compounding_method.setter
    def spread_compounding_method(self, spread_compounding_method):
        """Sets the spread_compounding_method of this Compounding.

        Defines how the computed leg spread is applied to compounded rate.  It applies only when CompoundingMethod = ‘Compounded‘.    Supported string (enumeration) values are: [Straight, IsdaCompounding, NoCompounding, SpreadExclusive, IsdaFlatCompounding, Flat, None].  # noqa: E501

        :param spread_compounding_method: The spread_compounding_method of this Compounding.  # noqa: E501
        :type spread_compounding_method: str
        """
        if self.local_vars_configuration.client_side_validation and spread_compounding_method is None:  # noqa: E501
            raise ValueError("Invalid value for `spread_compounding_method`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                spread_compounding_method is not None and len(spread_compounding_method) < 1):
            raise ValueError("Invalid value for `spread_compounding_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._spread_compounding_method = spread_compounding_method

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
        if not isinstance(other, Compounding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Compounding):
            return True

        return self.to_dict() != other.to_dict()
