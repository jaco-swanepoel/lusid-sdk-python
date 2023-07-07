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


class ComplianceRuleBreakdown(object):
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
        'group_status': 'str',
        'results_used': 'dict(str, float)',
        'properties_used': 'dict(str, str)',
        'parameters_used': 'dict(str, str)',
        'missing_data_information': 'list[str]'
    }

    attribute_map = {
        'group_status': 'groupStatus',
        'results_used': 'resultsUsed',
        'properties_used': 'propertiesUsed',
        'parameters_used': 'parametersUsed',
        'missing_data_information': 'missingDataInformation'
    }

    required_map = {
        'group_status': 'required',
        'results_used': 'required',
        'properties_used': 'required',
        'parameters_used': 'required',
        'missing_data_information': 'required'
    }

    def __init__(self, group_status=None, results_used=None, properties_used=None, parameters_used=None, missing_data_information=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceRuleBreakdown - a model defined in OpenAPI"
        
        :param group_status:  (required)
        :type group_status: str
        :param results_used:  (required)
        :type results_used: dict(str, float)
        :param properties_used:  (required)
        :type properties_used: dict(str, str)
        :param parameters_used:  (required)
        :type parameters_used: dict(str, str)
        :param missing_data_information:  (required)
        :type missing_data_information: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._group_status = None
        self._results_used = None
        self._properties_used = None
        self._parameters_used = None
        self._missing_data_information = None
        self.discriminator = None

        self.group_status = group_status
        self.results_used = results_used
        self.properties_used = properties_used
        self.parameters_used = parameters_used
        self.missing_data_information = missing_data_information

    @property
    def group_status(self):
        """Gets the group_status of this ComplianceRuleBreakdown.  # noqa: E501


        :return: The group_status of this ComplianceRuleBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._group_status

    @group_status.setter
    def group_status(self, group_status):
        """Sets the group_status of this ComplianceRuleBreakdown.


        :param group_status: The group_status of this ComplianceRuleBreakdown.  # noqa: E501
        :type group_status: str
        """
        if self.local_vars_configuration.client_side_validation and group_status is None:  # noqa: E501
            raise ValueError("Invalid value for `group_status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                group_status is not None and len(group_status) < 1):
            raise ValueError("Invalid value for `group_status`, length must be greater than or equal to `1`")  # noqa: E501

        self._group_status = group_status

    @property
    def results_used(self):
        """Gets the results_used of this ComplianceRuleBreakdown.  # noqa: E501


        :return: The results_used of this ComplianceRuleBreakdown.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._results_used

    @results_used.setter
    def results_used(self, results_used):
        """Sets the results_used of this ComplianceRuleBreakdown.


        :param results_used: The results_used of this ComplianceRuleBreakdown.  # noqa: E501
        :type results_used: dict(str, float)
        """
        if self.local_vars_configuration.client_side_validation and results_used is None:  # noqa: E501
            raise ValueError("Invalid value for `results_used`, must not be `None`")  # noqa: E501

        self._results_used = results_used

    @property
    def properties_used(self):
        """Gets the properties_used of this ComplianceRuleBreakdown.  # noqa: E501


        :return: The properties_used of this ComplianceRuleBreakdown.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties_used

    @properties_used.setter
    def properties_used(self, properties_used):
        """Sets the properties_used of this ComplianceRuleBreakdown.


        :param properties_used: The properties_used of this ComplianceRuleBreakdown.  # noqa: E501
        :type properties_used: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and properties_used is None:  # noqa: E501
            raise ValueError("Invalid value for `properties_used`, must not be `None`")  # noqa: E501

        self._properties_used = properties_used

    @property
    def parameters_used(self):
        """Gets the parameters_used of this ComplianceRuleBreakdown.  # noqa: E501


        :return: The parameters_used of this ComplianceRuleBreakdown.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters_used

    @parameters_used.setter
    def parameters_used(self, parameters_used):
        """Sets the parameters_used of this ComplianceRuleBreakdown.


        :param parameters_used: The parameters_used of this ComplianceRuleBreakdown.  # noqa: E501
        :type parameters_used: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and parameters_used is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters_used`, must not be `None`")  # noqa: E501

        self._parameters_used = parameters_used

    @property
    def missing_data_information(self):
        """Gets the missing_data_information of this ComplianceRuleBreakdown.  # noqa: E501


        :return: The missing_data_information of this ComplianceRuleBreakdown.  # noqa: E501
        :rtype: list[str]
        """
        return self._missing_data_information

    @missing_data_information.setter
    def missing_data_information(self, missing_data_information):
        """Sets the missing_data_information of this ComplianceRuleBreakdown.


        :param missing_data_information: The missing_data_information of this ComplianceRuleBreakdown.  # noqa: E501
        :type missing_data_information: list[str]
        """
        if self.local_vars_configuration.client_side_validation and missing_data_information is None:  # noqa: E501
            raise ValueError("Invalid value for `missing_data_information`, must not be `None`")  # noqa: E501

        self._missing_data_information = missing_data_information

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
        if not isinstance(other, ComplianceRuleBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceRuleBreakdown):
            return True

        return self.to_dict() != other.to_dict()
