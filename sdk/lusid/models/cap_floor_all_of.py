# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5060
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


class CapFloorAllOf(object):
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
        'cap_floor_type': 'str',
        'cap_strike': 'float',
        'floor_strike': 'float',
        'include_first_caplet': 'bool',
        'underlying_floating_leg': 'FloatingLeg',
        'instrument_type': 'str'
    }

    attribute_map = {
        'cap_floor_type': 'capFloorType',
        'cap_strike': 'capStrike',
        'floor_strike': 'floorStrike',
        'include_first_caplet': 'includeFirstCaplet',
        'underlying_floating_leg': 'underlyingFloatingLeg',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'cap_floor_type': 'required',
        'cap_strike': 'required',
        'floor_strike': 'required',
        'include_first_caplet': 'required',
        'underlying_floating_leg': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, cap_floor_type=None, cap_strike=None, floor_strike=None, include_first_caplet=None, underlying_floating_leg=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """CapFloorAllOf - a model defined in OpenAPI"
        
        :param cap_floor_type:  Determine if it's CAP, FLOOR, or COLLAR.    Supported string (enumeration) values are: [Cap, Floor, Collar]. (required)
        :type cap_floor_type: str
        :param cap_strike:  Strike rate of the Cap. (required)
        :type cap_strike: float
        :param floor_strike:  Strike rate of the Floor. (required)
        :type floor_strike: float
        :param include_first_caplet:  Include first caplet flag. (required)
        :type include_first_caplet: bool
        :param underlying_floating_leg:  (required)
        :type underlying_floating_leg: lusid.FloatingLeg
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cap_floor_type = None
        self._cap_strike = None
        self._floor_strike = None
        self._include_first_caplet = None
        self._underlying_floating_leg = None
        self._instrument_type = None
        self.discriminator = None

        self.cap_floor_type = cap_floor_type
        self.cap_strike = cap_strike
        self.floor_strike = floor_strike
        self.include_first_caplet = include_first_caplet
        self.underlying_floating_leg = underlying_floating_leg
        self.instrument_type = instrument_type

    @property
    def cap_floor_type(self):
        """Gets the cap_floor_type of this CapFloorAllOf.  # noqa: E501

        Determine if it's CAP, FLOOR, or COLLAR.    Supported string (enumeration) values are: [Cap, Floor, Collar].  # noqa: E501

        :return: The cap_floor_type of this CapFloorAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cap_floor_type

    @cap_floor_type.setter
    def cap_floor_type(self, cap_floor_type):
        """Sets the cap_floor_type of this CapFloorAllOf.

        Determine if it's CAP, FLOOR, or COLLAR.    Supported string (enumeration) values are: [Cap, Floor, Collar].  # noqa: E501

        :param cap_floor_type: The cap_floor_type of this CapFloorAllOf.  # noqa: E501
        :type cap_floor_type: str
        """
        if self.local_vars_configuration.client_side_validation and cap_floor_type is None:  # noqa: E501
            raise ValueError("Invalid value for `cap_floor_type`, must not be `None`")  # noqa: E501

        self._cap_floor_type = cap_floor_type

    @property
    def cap_strike(self):
        """Gets the cap_strike of this CapFloorAllOf.  # noqa: E501

        Strike rate of the Cap.  # noqa: E501

        :return: The cap_strike of this CapFloorAllOf.  # noqa: E501
        :rtype: float
        """
        return self._cap_strike

    @cap_strike.setter
    def cap_strike(self, cap_strike):
        """Sets the cap_strike of this CapFloorAllOf.

        Strike rate of the Cap.  # noqa: E501

        :param cap_strike: The cap_strike of this CapFloorAllOf.  # noqa: E501
        :type cap_strike: float
        """
        if self.local_vars_configuration.client_side_validation and cap_strike is None:  # noqa: E501
            raise ValueError("Invalid value for `cap_strike`, must not be `None`")  # noqa: E501

        self._cap_strike = cap_strike

    @property
    def floor_strike(self):
        """Gets the floor_strike of this CapFloorAllOf.  # noqa: E501

        Strike rate of the Floor.  # noqa: E501

        :return: The floor_strike of this CapFloorAllOf.  # noqa: E501
        :rtype: float
        """
        return self._floor_strike

    @floor_strike.setter
    def floor_strike(self, floor_strike):
        """Sets the floor_strike of this CapFloorAllOf.

        Strike rate of the Floor.  # noqa: E501

        :param floor_strike: The floor_strike of this CapFloorAllOf.  # noqa: E501
        :type floor_strike: float
        """
        if self.local_vars_configuration.client_side_validation and floor_strike is None:  # noqa: E501
            raise ValueError("Invalid value for `floor_strike`, must not be `None`")  # noqa: E501

        self._floor_strike = floor_strike

    @property
    def include_first_caplet(self):
        """Gets the include_first_caplet of this CapFloorAllOf.  # noqa: E501

        Include first caplet flag.  # noqa: E501

        :return: The include_first_caplet of this CapFloorAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._include_first_caplet

    @include_first_caplet.setter
    def include_first_caplet(self, include_first_caplet):
        """Sets the include_first_caplet of this CapFloorAllOf.

        Include first caplet flag.  # noqa: E501

        :param include_first_caplet: The include_first_caplet of this CapFloorAllOf.  # noqa: E501
        :type include_first_caplet: bool
        """
        if self.local_vars_configuration.client_side_validation and include_first_caplet is None:  # noqa: E501
            raise ValueError("Invalid value for `include_first_caplet`, must not be `None`")  # noqa: E501

        self._include_first_caplet = include_first_caplet

    @property
    def underlying_floating_leg(self):
        """Gets the underlying_floating_leg of this CapFloorAllOf.  # noqa: E501


        :return: The underlying_floating_leg of this CapFloorAllOf.  # noqa: E501
        :rtype: lusid.FloatingLeg
        """
        return self._underlying_floating_leg

    @underlying_floating_leg.setter
    def underlying_floating_leg(self, underlying_floating_leg):
        """Sets the underlying_floating_leg of this CapFloorAllOf.


        :param underlying_floating_leg: The underlying_floating_leg of this CapFloorAllOf.  # noqa: E501
        :type underlying_floating_leg: lusid.FloatingLeg
        """
        if self.local_vars_configuration.client_side_validation and underlying_floating_leg is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying_floating_leg`, must not be `None`")  # noqa: E501

        self._underlying_floating_leg = underlying_floating_leg

    @property
    def instrument_type(self):
        """Gets the instrument_type of this CapFloorAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :return: The instrument_type of this CapFloorAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this CapFloorAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :param instrument_type: The instrument_type of this CapFloorAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, CapFloorAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CapFloorAllOf):
            return True

        return self.to_dict() != other.to_dict()
