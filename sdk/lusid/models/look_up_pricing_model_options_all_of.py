# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.368
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


class LookUpPricingModelOptionsAllOf(object):
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
        'add_accrual': 'bool',
        'apply_index_ratio': 'bool',
        'model_options_type': 'str'
    }

    attribute_map = {
        'add_accrual': 'addAccrual',
        'apply_index_ratio': 'applyIndexRatio',
        'model_options_type': 'modelOptionsType'
    }

    required_map = {
        'add_accrual': 'required',
        'apply_index_ratio': 'required',
        'model_options_type': 'required'
    }

    def __init__(self, add_accrual=None, apply_index_ratio=None, model_options_type=None, local_vars_configuration=None):  # noqa: E501
        """LookUpPricingModelOptionsAllOf - a model defined in OpenAPI"
        
        :param add_accrual:  Add Instrument Accrual to Valuation (required)
        :type add_accrual: bool
        :param apply_index_ratio:  Apply Index Ratio to price before valuation.  Used for InflationLinkedBond (required)
        :type apply_index_ratio: bool
        :param model_options_type:  The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions (required)
        :type model_options_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._add_accrual = None
        self._apply_index_ratio = None
        self._model_options_type = None
        self.discriminator = None

        self.add_accrual = add_accrual
        self.apply_index_ratio = apply_index_ratio
        self.model_options_type = model_options_type

    @property
    def add_accrual(self):
        """Gets the add_accrual of this LookUpPricingModelOptionsAllOf.  # noqa: E501

        Add Instrument Accrual to Valuation  # noqa: E501

        :return: The add_accrual of this LookUpPricingModelOptionsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._add_accrual

    @add_accrual.setter
    def add_accrual(self, add_accrual):
        """Sets the add_accrual of this LookUpPricingModelOptionsAllOf.

        Add Instrument Accrual to Valuation  # noqa: E501

        :param add_accrual: The add_accrual of this LookUpPricingModelOptionsAllOf.  # noqa: E501
        :type add_accrual: bool
        """
        if self.local_vars_configuration.client_side_validation and add_accrual is None:  # noqa: E501
            raise ValueError("Invalid value for `add_accrual`, must not be `None`")  # noqa: E501

        self._add_accrual = add_accrual

    @property
    def apply_index_ratio(self):
        """Gets the apply_index_ratio of this LookUpPricingModelOptionsAllOf.  # noqa: E501

        Apply Index Ratio to price before valuation.  Used for InflationLinkedBond  # noqa: E501

        :return: The apply_index_ratio of this LookUpPricingModelOptionsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._apply_index_ratio

    @apply_index_ratio.setter
    def apply_index_ratio(self, apply_index_ratio):
        """Sets the apply_index_ratio of this LookUpPricingModelOptionsAllOf.

        Apply Index Ratio to price before valuation.  Used for InflationLinkedBond  # noqa: E501

        :param apply_index_ratio: The apply_index_ratio of this LookUpPricingModelOptionsAllOf.  # noqa: E501
        :type apply_index_ratio: bool
        """
        if self.local_vars_configuration.client_side_validation and apply_index_ratio is None:  # noqa: E501
            raise ValueError("Invalid value for `apply_index_ratio`, must not be `None`")  # noqa: E501

        self._apply_index_ratio = apply_index_ratio

    @property
    def model_options_type(self):
        """Gets the model_options_type of this LookUpPricingModelOptionsAllOf.  # noqa: E501

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions  # noqa: E501

        :return: The model_options_type of this LookUpPricingModelOptionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._model_options_type

    @model_options_type.setter
    def model_options_type(self, model_options_type):
        """Sets the model_options_type of this LookUpPricingModelOptionsAllOf.

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions  # noqa: E501

        :param model_options_type: The model_options_type of this LookUpPricingModelOptionsAllOf.  # noqa: E501
        :type model_options_type: str
        """
        if self.local_vars_configuration.client_side_validation and model_options_type is None:  # noqa: E501
            raise ValueError("Invalid value for `model_options_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Invalid", "OpaqueModelOptions", "EmptyModelOptions", "IndexModelOptions", "FxForwardModelOptions", "FundingLegModelOptions", "EquityModelOptions", "LookUpPricingModelOptions"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and model_options_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `model_options_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_options_type, allowed_values)
            )

        self._model_options_type = model_options_type

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
        if not isinstance(other, LookUpPricingModelOptionsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LookUpPricingModelOptionsAllOf):
            return True

        return self.to_dict() != other.to_dict()
