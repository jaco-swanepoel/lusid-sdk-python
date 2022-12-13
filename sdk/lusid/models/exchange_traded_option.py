# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5064
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


class ExchangeTradedOption(object):
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
        'start_date': 'datetime',
        'contract_details': 'ExchangeTradedOptionContractDetails',
        'contracts': 'float',
        'ref_spot_price': 'float',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'contract_details': 'contractDetails',
        'contracts': 'contracts',
        'ref_spot_price': 'refSpotPrice',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'contract_details': 'required',
        'contracts': 'required',
        'ref_spot_price': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, contract_details=None, contracts=None, ref_spot_price=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """ExchangeTradedOption - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param contract_details:  (required)
        :type contract_details: lusid.ExchangeTradedOptionContractDetails
        :param contracts:  The number of contracts held. (required)
        :type contracts: float
        :param ref_spot_price:  The reference spot price for the option at which the contract was entered into. (required)
        :type ref_spot_price: float
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._contract_details = None
        self._contracts = None
        self._ref_spot_price = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.contract_details = contract_details
        self.contracts = contracts
        self.ref_spot_price = ref_spot_price
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this ExchangeTradedOption.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this ExchangeTradedOption.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ExchangeTradedOption.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this ExchangeTradedOption.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def contract_details(self):
        """Gets the contract_details of this ExchangeTradedOption.  # noqa: E501


        :return: The contract_details of this ExchangeTradedOption.  # noqa: E501
        :rtype: lusid.ExchangeTradedOptionContractDetails
        """
        return self._contract_details

    @contract_details.setter
    def contract_details(self, contract_details):
        """Sets the contract_details of this ExchangeTradedOption.


        :param contract_details: The contract_details of this ExchangeTradedOption.  # noqa: E501
        :type contract_details: lusid.ExchangeTradedOptionContractDetails
        """
        if self.local_vars_configuration.client_side_validation and contract_details is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_details`, must not be `None`")  # noqa: E501

        self._contract_details = contract_details

    @property
    def contracts(self):
        """Gets the contracts of this ExchangeTradedOption.  # noqa: E501

        The number of contracts held.  # noqa: E501

        :return: The contracts of this ExchangeTradedOption.  # noqa: E501
        :rtype: float
        """
        return self._contracts

    @contracts.setter
    def contracts(self, contracts):
        """Sets the contracts of this ExchangeTradedOption.

        The number of contracts held.  # noqa: E501

        :param contracts: The contracts of this ExchangeTradedOption.  # noqa: E501
        :type contracts: float
        """
        if self.local_vars_configuration.client_side_validation and contracts is None:  # noqa: E501
            raise ValueError("Invalid value for `contracts`, must not be `None`")  # noqa: E501

        self._contracts = contracts

    @property
    def ref_spot_price(self):
        """Gets the ref_spot_price of this ExchangeTradedOption.  # noqa: E501

        The reference spot price for the option at which the contract was entered into.  # noqa: E501

        :return: The ref_spot_price of this ExchangeTradedOption.  # noqa: E501
        :rtype: float
        """
        return self._ref_spot_price

    @ref_spot_price.setter
    def ref_spot_price(self, ref_spot_price):
        """Sets the ref_spot_price of this ExchangeTradedOption.

        The reference spot price for the option at which the contract was entered into.  # noqa: E501

        :param ref_spot_price: The ref_spot_price of this ExchangeTradedOption.  # noqa: E501
        :type ref_spot_price: float
        """
        if self.local_vars_configuration.client_side_validation and ref_spot_price is None:  # noqa: E501
            raise ValueError("Invalid value for `ref_spot_price`, must not be `None`")  # noqa: E501

        self._ref_spot_price = ref_spot_price

    @property
    def instrument_type(self):
        """Gets the instrument_type of this ExchangeTradedOption.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :return: The instrument_type of this ExchangeTradedOption.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this ExchangeTradedOption.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :param instrument_type: The instrument_type of this ExchangeTradedOption.  # noqa: E501
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
        if not isinstance(other, ExchangeTradedOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExchangeTradedOption):
            return True

        return self.to_dict() != other.to_dict()
