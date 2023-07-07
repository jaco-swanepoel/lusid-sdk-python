# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.319
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


class ComplianceParameter(object):
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
        'parameter_type': 'str',
        'value': 'object'
    }

    attribute_map = {
        'parameter_type': 'parameterType',
        'value': 'value'
    }

    required_map = {
        'parameter_type': 'required',
        'value': 'required'
    }

    def __init__(self, parameter_type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceParameter - a model defined in OpenAPI"
        
        :param parameter_type:  The parameter type. (required)
        :type parameter_type: str
        :param value:  The parameter value. (required)
        :type value: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._parameter_type = None
        self._value = None
        self.discriminator = None

        self.parameter_type = parameter_type
        self.value = value

    @property
    def parameter_type(self):
        """Gets the parameter_type of this ComplianceParameter.  # noqa: E501

        The parameter type.  # noqa: E501

        :return: The parameter_type of this ComplianceParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        """Sets the parameter_type of this ComplianceParameter.

        The parameter type.  # noqa: E501

        :param parameter_type: The parameter_type of this ComplianceParameter.  # noqa: E501
        :type parameter_type: str
        """
        if self.local_vars_configuration.client_side_validation and parameter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `parameter_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                parameter_type is not None and len(parameter_type) < 1):
            raise ValueError("Invalid value for `parameter_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._parameter_type = parameter_type

    @property
    def value(self):
        """Gets the value of this ComplianceParameter.  # noqa: E501

        The parameter value.  # noqa: E501

        :return: The value of this ComplianceParameter.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ComplianceParameter.

        The parameter value.  # noqa: E501

        :param value: The value of this ComplianceParameter.  # noqa: E501
        :type value: object
        """

        self._value = value

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
        if not isinstance(other, ComplianceParameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceParameter):
            return True

        return self.to_dict() != other.to_dict()
