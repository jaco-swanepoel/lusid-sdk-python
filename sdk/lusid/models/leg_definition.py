# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5299
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


class LegDefinition(object):
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
        'convention_name': 'FlowConventionName',
        'conventions': 'FlowConventions',
        'index_convention': 'IndexConvention',
        'index_convention_name': 'FlowConventionName',
        'notional_exchange_type': 'str',
        'pay_receive': 'str',
        'rate_or_spread': 'float',
        'reset_convention': 'str',
        'stub_type': 'str',
        'compounding': 'Compounding',
        'amortisation': 'StepSchedule'
    }

    attribute_map = {
        'convention_name': 'conventionName',
        'conventions': 'conventions',
        'index_convention': 'indexConvention',
        'index_convention_name': 'indexConventionName',
        'notional_exchange_type': 'notionalExchangeType',
        'pay_receive': 'payReceive',
        'rate_or_spread': 'rateOrSpread',
        'reset_convention': 'resetConvention',
        'stub_type': 'stubType',
        'compounding': 'compounding',
        'amortisation': 'amortisation'
    }

    required_map = {
        'convention_name': 'optional',
        'conventions': 'optional',
        'index_convention': 'optional',
        'index_convention_name': 'optional',
        'notional_exchange_type': 'required',
        'pay_receive': 'required',
        'rate_or_spread': 'required',
        'reset_convention': 'optional',
        'stub_type': 'required',
        'compounding': 'optional',
        'amortisation': 'optional'
    }

    def __init__(self, convention_name=None, conventions=None, index_convention=None, index_convention_name=None, notional_exchange_type=None, pay_receive=None, rate_or_spread=None, reset_convention=None, stub_type=None, compounding=None, amortisation=None, local_vars_configuration=None):  # noqa: E501
        """LegDefinition - a model defined in OpenAPI"
        
        :param convention_name: 
        :type convention_name: lusid.FlowConventionName
        :param conventions: 
        :type conventions: lusid.FlowConventions
        :param index_convention: 
        :type index_convention: lusid.IndexConvention
        :param index_convention_name: 
        :type index_convention_name: lusid.FlowConventionName
        :param notional_exchange_type:  what type of notional exchange does the leg have    Supported string (enumeration) values are: [None, Initial, Final, Both]. (required)
        :type notional_exchange_type: str
        :param pay_receive:  Is the leg to be paid or received    Supported string (enumeration) values are: [Pay, Receive]. (required)
        :type pay_receive: str
        :param rate_or_spread:  Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg. (required)
        :type rate_or_spread: float
        :param reset_convention:  Control how resets are generated relative to swap payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].
        :type reset_convention: str
        :param stub_type:  If a stub is required should it be at the front or back of the leg.    Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both]. (required)
        :type stub_type: str
        :param compounding: 
        :type compounding: lusid.Compounding
        :param amortisation: 
        :type amortisation: lusid.StepSchedule

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._convention_name = None
        self._conventions = None
        self._index_convention = None
        self._index_convention_name = None
        self._notional_exchange_type = None
        self._pay_receive = None
        self._rate_or_spread = None
        self._reset_convention = None
        self._stub_type = None
        self._compounding = None
        self._amortisation = None
        self.discriminator = None

        if convention_name is not None:
            self.convention_name = convention_name
        if conventions is not None:
            self.conventions = conventions
        if index_convention is not None:
            self.index_convention = index_convention
        if index_convention_name is not None:
            self.index_convention_name = index_convention_name
        self.notional_exchange_type = notional_exchange_type
        self.pay_receive = pay_receive
        self.rate_or_spread = rate_or_spread
        self.reset_convention = reset_convention
        self.stub_type = stub_type
        if compounding is not None:
            self.compounding = compounding
        if amortisation is not None:
            self.amortisation = amortisation

    @property
    def convention_name(self):
        """Gets the convention_name of this LegDefinition.  # noqa: E501


        :return: The convention_name of this LegDefinition.  # noqa: E501
        :rtype: lusid.FlowConventionName
        """
        return self._convention_name

    @convention_name.setter
    def convention_name(self, convention_name):
        """Sets the convention_name of this LegDefinition.


        :param convention_name: The convention_name of this LegDefinition.  # noqa: E501
        :type convention_name: lusid.FlowConventionName
        """

        self._convention_name = convention_name

    @property
    def conventions(self):
        """Gets the conventions of this LegDefinition.  # noqa: E501


        :return: The conventions of this LegDefinition.  # noqa: E501
        :rtype: lusid.FlowConventions
        """
        return self._conventions

    @conventions.setter
    def conventions(self, conventions):
        """Sets the conventions of this LegDefinition.


        :param conventions: The conventions of this LegDefinition.  # noqa: E501
        :type conventions: lusid.FlowConventions
        """

        self._conventions = conventions

    @property
    def index_convention(self):
        """Gets the index_convention of this LegDefinition.  # noqa: E501


        :return: The index_convention of this LegDefinition.  # noqa: E501
        :rtype: lusid.IndexConvention
        """
        return self._index_convention

    @index_convention.setter
    def index_convention(self, index_convention):
        """Sets the index_convention of this LegDefinition.


        :param index_convention: The index_convention of this LegDefinition.  # noqa: E501
        :type index_convention: lusid.IndexConvention
        """

        self._index_convention = index_convention

    @property
    def index_convention_name(self):
        """Gets the index_convention_name of this LegDefinition.  # noqa: E501


        :return: The index_convention_name of this LegDefinition.  # noqa: E501
        :rtype: lusid.FlowConventionName
        """
        return self._index_convention_name

    @index_convention_name.setter
    def index_convention_name(self, index_convention_name):
        """Sets the index_convention_name of this LegDefinition.


        :param index_convention_name: The index_convention_name of this LegDefinition.  # noqa: E501
        :type index_convention_name: lusid.FlowConventionName
        """

        self._index_convention_name = index_convention_name

    @property
    def notional_exchange_type(self):
        """Gets the notional_exchange_type of this LegDefinition.  # noqa: E501

        what type of notional exchange does the leg have    Supported string (enumeration) values are: [None, Initial, Final, Both].  # noqa: E501

        :return: The notional_exchange_type of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._notional_exchange_type

    @notional_exchange_type.setter
    def notional_exchange_type(self, notional_exchange_type):
        """Sets the notional_exchange_type of this LegDefinition.

        what type of notional exchange does the leg have    Supported string (enumeration) values are: [None, Initial, Final, Both].  # noqa: E501

        :param notional_exchange_type: The notional_exchange_type of this LegDefinition.  # noqa: E501
        :type notional_exchange_type: str
        """
        if self.local_vars_configuration.client_side_validation and notional_exchange_type is None:  # noqa: E501
            raise ValueError("Invalid value for `notional_exchange_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                notional_exchange_type is not None and len(notional_exchange_type) < 1):
            raise ValueError("Invalid value for `notional_exchange_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._notional_exchange_type = notional_exchange_type

    @property
    def pay_receive(self):
        """Gets the pay_receive of this LegDefinition.  # noqa: E501

        Is the leg to be paid or received    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :return: The pay_receive of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._pay_receive

    @pay_receive.setter
    def pay_receive(self, pay_receive):
        """Sets the pay_receive of this LegDefinition.

        Is the leg to be paid or received    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :param pay_receive: The pay_receive of this LegDefinition.  # noqa: E501
        :type pay_receive: str
        """
        if self.local_vars_configuration.client_side_validation and pay_receive is None:  # noqa: E501
            raise ValueError("Invalid value for `pay_receive`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pay_receive is not None and len(pay_receive) < 1):
            raise ValueError("Invalid value for `pay_receive`, length must be greater than or equal to `1`")  # noqa: E501

        self._pay_receive = pay_receive

    @property
    def rate_or_spread(self):
        """Gets the rate_or_spread of this LegDefinition.  # noqa: E501

        Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg.  # noqa: E501

        :return: The rate_or_spread of this LegDefinition.  # noqa: E501
        :rtype: float
        """
        return self._rate_or_spread

    @rate_or_spread.setter
    def rate_or_spread(self, rate_or_spread):
        """Sets the rate_or_spread of this LegDefinition.

        Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg.  # noqa: E501

        :param rate_or_spread: The rate_or_spread of this LegDefinition.  # noqa: E501
        :type rate_or_spread: float
        """
        if self.local_vars_configuration.client_side_validation and rate_or_spread is None:  # noqa: E501
            raise ValueError("Invalid value for `rate_or_spread`, must not be `None`")  # noqa: E501

        self._rate_or_spread = rate_or_spread

    @property
    def reset_convention(self):
        """Gets the reset_convention of this LegDefinition.  # noqa: E501

        Control how resets are generated relative to swap payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].  # noqa: E501

        :return: The reset_convention of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._reset_convention

    @reset_convention.setter
    def reset_convention(self, reset_convention):
        """Sets the reset_convention of this LegDefinition.

        Control how resets are generated relative to swap payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].  # noqa: E501

        :param reset_convention: The reset_convention of this LegDefinition.  # noqa: E501
        :type reset_convention: str
        """

        self._reset_convention = reset_convention

    @property
    def stub_type(self):
        """Gets the stub_type of this LegDefinition.  # noqa: E501

        If a stub is required should it be at the front or back of the leg.    Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both].  # noqa: E501

        :return: The stub_type of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._stub_type

    @stub_type.setter
    def stub_type(self, stub_type):
        """Sets the stub_type of this LegDefinition.

        If a stub is required should it be at the front or back of the leg.    Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both].  # noqa: E501

        :param stub_type: The stub_type of this LegDefinition.  # noqa: E501
        :type stub_type: str
        """
        if self.local_vars_configuration.client_side_validation and stub_type is None:  # noqa: E501
            raise ValueError("Invalid value for `stub_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                stub_type is not None and len(stub_type) < 1):
            raise ValueError("Invalid value for `stub_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._stub_type = stub_type

    @property
    def compounding(self):
        """Gets the compounding of this LegDefinition.  # noqa: E501


        :return: The compounding of this LegDefinition.  # noqa: E501
        :rtype: lusid.Compounding
        """
        return self._compounding

    @compounding.setter
    def compounding(self, compounding):
        """Sets the compounding of this LegDefinition.


        :param compounding: The compounding of this LegDefinition.  # noqa: E501
        :type compounding: lusid.Compounding
        """

        self._compounding = compounding

    @property
    def amortisation(self):
        """Gets the amortisation of this LegDefinition.  # noqa: E501


        :return: The amortisation of this LegDefinition.  # noqa: E501
        :rtype: lusid.StepSchedule
        """
        return self._amortisation

    @amortisation.setter
    def amortisation(self, amortisation):
        """Sets the amortisation of this LegDefinition.


        :param amortisation: The amortisation of this LegDefinition.  # noqa: E501
        :type amortisation: lusid.StepSchedule
        """

        self._amortisation = amortisation

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
        if not isinstance(other, LegDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LegDefinition):
            return True

        return self.to_dict() != other.to_dict()
