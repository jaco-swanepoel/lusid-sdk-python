# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.258
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


class InflationLinkedBond(object):
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
        'maturity_date': 'datetime',
        'flow_conventions': 'FlowConventions',
        'coupon_rate': 'float',
        'identifiers': 'dict(str, str)',
        'dom_ccy': 'str',
        'base_cpi': 'float',
        'base_cpi_date': 'datetime',
        'calculation_type': 'str',
        'ex_dividend_days': 'int',
        'index_precision': 'int',
        'inflation_index_name': 'str',
        'inflation_interpolation': 'str',
        'inflation_roll_day': 'int',
        'observation_lag': 'str',
        'principal': 'float',
        'principal_protection': 'bool',
        'stub_type': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'flow_conventions': 'flowConventions',
        'coupon_rate': 'couponRate',
        'identifiers': 'identifiers',
        'dom_ccy': 'domCcy',
        'base_cpi': 'baseCPI',
        'base_cpi_date': 'baseCPIDate',
        'calculation_type': 'calculationType',
        'ex_dividend_days': 'exDividendDays',
        'index_precision': 'indexPrecision',
        'inflation_index_name': 'inflationIndexName',
        'inflation_interpolation': 'inflationInterpolation',
        'inflation_roll_day': 'inflationRollDay',
        'observation_lag': 'observationLag',
        'principal': 'principal',
        'principal_protection': 'principalProtection',
        'stub_type': 'stubType',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'flow_conventions': 'required',
        'coupon_rate': 'required',
        'identifiers': 'optional',
        'dom_ccy': 'required',
        'base_cpi': 'optional',
        'base_cpi_date': 'optional',
        'calculation_type': 'optional',
        'ex_dividend_days': 'optional',
        'index_precision': 'optional',
        'inflation_index_name': 'required',
        'inflation_interpolation': 'optional',
        'inflation_roll_day': 'optional',
        'observation_lag': 'optional',
        'principal': 'required',
        'principal_protection': 'optional',
        'stub_type': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, flow_conventions=None, coupon_rate=None, identifiers=None, dom_ccy=None, base_cpi=None, base_cpi_date=None, calculation_type=None, ex_dividend_days=None, index_precision=None, inflation_index_name=None, inflation_interpolation=None, inflation_roll_day=None, observation_lag=None, principal=None, principal_protection=None, stub_type=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """InflationLinkedBond - a model defined in OpenAPI"
        
        :param start_date:  The start date of the bond. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. (required)
        :type maturity_date: datetime
        :param flow_conventions:  (required)
        :type flow_conventions: lusid.FlowConventions
        :param coupon_rate:  Simple coupon rate. (required)
        :type coupon_rate: float
        :param identifiers:  External market codes and identifiers for the bond, e.g. ISIN.
        :type identifiers: dict(str, str)
        :param dom_ccy:  The domestic currency of the instrument. (required)
        :type dom_ccy: str
        :param base_cpi:  BaseCPI value. This is optional, if not provided the BaseCPI value will be calculated from the BaseCPIDate,  if that too is not present the StartDate will be used.                If provided then this value will always set the BaseCPI on this bond.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the BaseCPIDate.
        :type base_cpi: float
        :param base_cpi_date:  BaseCPIDate. This is optional. Gives the date that the BaseCPI is calculated for.                Note this is an un-lagged date (similar to StartDate) so the Bond ObservationLag will  be applied to this date when calculating the CPI.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the actual BaseCPI.
        :type base_cpi_date: datetime
        :param calculation_type:  The calculation type applied to the bond coupon and principal amount.  The default CalculationType is `Standard`.    Supported string (enumeration) values are: [Standard, Quarterly, Ratio].
        :type calculation_type: str
        :param ex_dividend_days:  Number of Good Business Days before the next coupon payment, in which the bond goes ex-dividend.  This is not common in inflation linked bonds but has been seen with (for example) bonds issued by  the Bank of Thailand.
        :type ex_dividend_days: int
        :param index_precision:  Number of decimal places used to round IndexRatio. This defaults to 5 if not set.
        :type index_precision: int
        :param inflation_index_name:  Name of the index, e.g. UKRPI. (required)
        :type inflation_index_name: str
        :param inflation_interpolation:  Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat].
        :type inflation_interpolation: str
        :param inflation_roll_day:  Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th).
        :type inflation_roll_day: int
        :param observation_lag:  Observation lag. This is a Tenor that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid.
        :type observation_lag: str
        :param principal:  The face-value or principal for the bond at outset. (required)
        :type principal: float
        :param principal_protection:  If true then the principal is protected in that the redemption amount will be at least the face value (Principal).  This is typically set to true for inflation linked bonds issued by the United States and France (for example).  This is typically set to false for inflation linked bonds issued by the United Kingdom (post 2005).  For other sovereigns this can vary from issue to issue.  If not set this property defaults to true.  This is sometimes referred to as Deflation protection or an inflation floor of 0%.
        :type principal_protection: bool
        :param stub_type:  StubType. Most Inflation linked bonds have a ShortFront stub type so this is the default, however in some cases  with a long front stub LongFront should be selected.  StubType Both is not supported for InflationLinkedBonds.    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both].
        :type stub_type: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._flow_conventions = None
        self._coupon_rate = None
        self._identifiers = None
        self._dom_ccy = None
        self._base_cpi = None
        self._base_cpi_date = None
        self._calculation_type = None
        self._ex_dividend_days = None
        self._index_precision = None
        self._inflation_index_name = None
        self._inflation_interpolation = None
        self._inflation_roll_day = None
        self._observation_lag = None
        self._principal = None
        self._principal_protection = None
        self._stub_type = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.flow_conventions = flow_conventions
        self.coupon_rate = coupon_rate
        self.identifiers = identifiers
        self.dom_ccy = dom_ccy
        self.base_cpi = base_cpi
        self.base_cpi_date = base_cpi_date
        self.calculation_type = calculation_type
        self.ex_dividend_days = ex_dividend_days
        if index_precision is not None:
            self.index_precision = index_precision
        self.inflation_index_name = inflation_index_name
        self.inflation_interpolation = inflation_interpolation
        if inflation_roll_day is not None:
            self.inflation_roll_day = inflation_roll_day
        self.observation_lag = observation_lag
        self.principal = principal
        if principal_protection is not None:
            self.principal_protection = principal_protection
        self.stub_type = stub_type
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this InflationLinkedBond.  # noqa: E501

        The start date of the bond.  # noqa: E501

        :return: The start_date of this InflationLinkedBond.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InflationLinkedBond.

        The start date of the bond.  # noqa: E501

        :param start_date: The start_date of this InflationLinkedBond.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this InflationLinkedBond.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :return: The maturity_date of this InflationLinkedBond.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this InflationLinkedBond.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :param maturity_date: The maturity_date of this InflationLinkedBond.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def flow_conventions(self):
        """Gets the flow_conventions of this InflationLinkedBond.  # noqa: E501


        :return: The flow_conventions of this InflationLinkedBond.  # noqa: E501
        :rtype: lusid.FlowConventions
        """
        return self._flow_conventions

    @flow_conventions.setter
    def flow_conventions(self, flow_conventions):
        """Sets the flow_conventions of this InflationLinkedBond.


        :param flow_conventions: The flow_conventions of this InflationLinkedBond.  # noqa: E501
        :type flow_conventions: lusid.FlowConventions
        """
        if self.local_vars_configuration.client_side_validation and flow_conventions is None:  # noqa: E501
            raise ValueError("Invalid value for `flow_conventions`, must not be `None`")  # noqa: E501

        self._flow_conventions = flow_conventions

    @property
    def coupon_rate(self):
        """Gets the coupon_rate of this InflationLinkedBond.  # noqa: E501

        Simple coupon rate.  # noqa: E501

        :return: The coupon_rate of this InflationLinkedBond.  # noqa: E501
        :rtype: float
        """
        return self._coupon_rate

    @coupon_rate.setter
    def coupon_rate(self, coupon_rate):
        """Sets the coupon_rate of this InflationLinkedBond.

        Simple coupon rate.  # noqa: E501

        :param coupon_rate: The coupon_rate of this InflationLinkedBond.  # noqa: E501
        :type coupon_rate: float
        """
        if self.local_vars_configuration.client_side_validation and coupon_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_rate`, must not be `None`")  # noqa: E501

        self._coupon_rate = coupon_rate

    @property
    def identifiers(self):
        """Gets the identifiers of this InflationLinkedBond.  # noqa: E501

        External market codes and identifiers for the bond, e.g. ISIN.  # noqa: E501

        :return: The identifiers of this InflationLinkedBond.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this InflationLinkedBond.

        External market codes and identifiers for the bond, e.g. ISIN.  # noqa: E501

        :param identifiers: The identifiers of this InflationLinkedBond.  # noqa: E501
        :type identifiers: dict(str, str)
        """

        self._identifiers = identifiers

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this InflationLinkedBond.  # noqa: E501

        The domestic currency of the instrument.  # noqa: E501

        :return: The dom_ccy of this InflationLinkedBond.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this InflationLinkedBond.

        The domestic currency of the instrument.  # noqa: E501

        :param dom_ccy: The dom_ccy of this InflationLinkedBond.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def base_cpi(self):
        """Gets the base_cpi of this InflationLinkedBond.  # noqa: E501

        BaseCPI value. This is optional, if not provided the BaseCPI value will be calculated from the BaseCPIDate,  if that too is not present the StartDate will be used.                If provided then this value will always set the BaseCPI on this bond.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the BaseCPIDate.  # noqa: E501

        :return: The base_cpi of this InflationLinkedBond.  # noqa: E501
        :rtype: float
        """
        return self._base_cpi

    @base_cpi.setter
    def base_cpi(self, base_cpi):
        """Sets the base_cpi of this InflationLinkedBond.

        BaseCPI value. This is optional, if not provided the BaseCPI value will be calculated from the BaseCPIDate,  if that too is not present the StartDate will be used.                If provided then this value will always set the BaseCPI on this bond.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the BaseCPIDate.  # noqa: E501

        :param base_cpi: The base_cpi of this InflationLinkedBond.  # noqa: E501
        :type base_cpi: float
        """

        self._base_cpi = base_cpi

    @property
    def base_cpi_date(self):
        """Gets the base_cpi_date of this InflationLinkedBond.  # noqa: E501

        BaseCPIDate. This is optional. Gives the date that the BaseCPI is calculated for.                Note this is an un-lagged date (similar to StartDate) so the Bond ObservationLag will  be applied to this date when calculating the CPI.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the actual BaseCPI.  # noqa: E501

        :return: The base_cpi_date of this InflationLinkedBond.  # noqa: E501
        :rtype: datetime
        """
        return self._base_cpi_date

    @base_cpi_date.setter
    def base_cpi_date(self, base_cpi_date):
        """Sets the base_cpi_date of this InflationLinkedBond.

        BaseCPIDate. This is optional. Gives the date that the BaseCPI is calculated for.                Note this is an un-lagged date (similar to StartDate) so the Bond ObservationLag will  be applied to this date when calculating the CPI.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the actual BaseCPI.  # noqa: E501

        :param base_cpi_date: The base_cpi_date of this InflationLinkedBond.  # noqa: E501
        :type base_cpi_date: datetime
        """

        self._base_cpi_date = base_cpi_date

    @property
    def calculation_type(self):
        """Gets the calculation_type of this InflationLinkedBond.  # noqa: E501

        The calculation type applied to the bond coupon and principal amount.  The default CalculationType is `Standard`.    Supported string (enumeration) values are: [Standard, Quarterly, Ratio].  # noqa: E501

        :return: The calculation_type of this InflationLinkedBond.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this InflationLinkedBond.

        The calculation type applied to the bond coupon and principal amount.  The default CalculationType is `Standard`.    Supported string (enumeration) values are: [Standard, Quarterly, Ratio].  # noqa: E501

        :param calculation_type: The calculation_type of this InflationLinkedBond.  # noqa: E501
        :type calculation_type: str
        """

        self._calculation_type = calculation_type

    @property
    def ex_dividend_days(self):
        """Gets the ex_dividend_days of this InflationLinkedBond.  # noqa: E501

        Number of Good Business Days before the next coupon payment, in which the bond goes ex-dividend.  This is not common in inflation linked bonds but has been seen with (for example) bonds issued by  the Bank of Thailand.  # noqa: E501

        :return: The ex_dividend_days of this InflationLinkedBond.  # noqa: E501
        :rtype: int
        """
        return self._ex_dividend_days

    @ex_dividend_days.setter
    def ex_dividend_days(self, ex_dividend_days):
        """Sets the ex_dividend_days of this InflationLinkedBond.

        Number of Good Business Days before the next coupon payment, in which the bond goes ex-dividend.  This is not common in inflation linked bonds but has been seen with (for example) bonds issued by  the Bank of Thailand.  # noqa: E501

        :param ex_dividend_days: The ex_dividend_days of this InflationLinkedBond.  # noqa: E501
        :type ex_dividend_days: int
        """

        self._ex_dividend_days = ex_dividend_days

    @property
    def index_precision(self):
        """Gets the index_precision of this InflationLinkedBond.  # noqa: E501

        Number of decimal places used to round IndexRatio. This defaults to 5 if not set.  # noqa: E501

        :return: The index_precision of this InflationLinkedBond.  # noqa: E501
        :rtype: int
        """
        return self._index_precision

    @index_precision.setter
    def index_precision(self, index_precision):
        """Sets the index_precision of this InflationLinkedBond.

        Number of decimal places used to round IndexRatio. This defaults to 5 if not set.  # noqa: E501

        :param index_precision: The index_precision of this InflationLinkedBond.  # noqa: E501
        :type index_precision: int
        """

        self._index_precision = index_precision

    @property
    def inflation_index_name(self):
        """Gets the inflation_index_name of this InflationLinkedBond.  # noqa: E501

        Name of the index, e.g. UKRPI.  # noqa: E501

        :return: The inflation_index_name of this InflationLinkedBond.  # noqa: E501
        :rtype: str
        """
        return self._inflation_index_name

    @inflation_index_name.setter
    def inflation_index_name(self, inflation_index_name):
        """Sets the inflation_index_name of this InflationLinkedBond.

        Name of the index, e.g. UKRPI.  # noqa: E501

        :param inflation_index_name: The inflation_index_name of this InflationLinkedBond.  # noqa: E501
        :type inflation_index_name: str
        """
        if self.local_vars_configuration.client_side_validation and inflation_index_name is None:  # noqa: E501
            raise ValueError("Invalid value for `inflation_index_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inflation_index_name is not None and len(inflation_index_name) < 1):
            raise ValueError("Invalid value for `inflation_index_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._inflation_index_name = inflation_index_name

    @property
    def inflation_interpolation(self):
        """Gets the inflation_interpolation of this InflationLinkedBond.  # noqa: E501

        Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat].  # noqa: E501

        :return: The inflation_interpolation of this InflationLinkedBond.  # noqa: E501
        :rtype: str
        """
        return self._inflation_interpolation

    @inflation_interpolation.setter
    def inflation_interpolation(self, inflation_interpolation):
        """Sets the inflation_interpolation of this InflationLinkedBond.

        Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat].  # noqa: E501

        :param inflation_interpolation: The inflation_interpolation of this InflationLinkedBond.  # noqa: E501
        :type inflation_interpolation: str
        """

        self._inflation_interpolation = inflation_interpolation

    @property
    def inflation_roll_day(self):
        """Gets the inflation_roll_day of this InflationLinkedBond.  # noqa: E501

        Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th).  # noqa: E501

        :return: The inflation_roll_day of this InflationLinkedBond.  # noqa: E501
        :rtype: int
        """
        return self._inflation_roll_day

    @inflation_roll_day.setter
    def inflation_roll_day(self, inflation_roll_day):
        """Sets the inflation_roll_day of this InflationLinkedBond.

        Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th).  # noqa: E501

        :param inflation_roll_day: The inflation_roll_day of this InflationLinkedBond.  # noqa: E501
        :type inflation_roll_day: int
        """

        self._inflation_roll_day = inflation_roll_day

    @property
    def observation_lag(self):
        """Gets the observation_lag of this InflationLinkedBond.  # noqa: E501

        Observation lag. This is a Tenor that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid.  # noqa: E501

        :return: The observation_lag of this InflationLinkedBond.  # noqa: E501
        :rtype: str
        """
        return self._observation_lag

    @observation_lag.setter
    def observation_lag(self, observation_lag):
        """Sets the observation_lag of this InflationLinkedBond.

        Observation lag. This is a Tenor that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid.  # noqa: E501

        :param observation_lag: The observation_lag of this InflationLinkedBond.  # noqa: E501
        :type observation_lag: str
        """

        self._observation_lag = observation_lag

    @property
    def principal(self):
        """Gets the principal of this InflationLinkedBond.  # noqa: E501

        The face-value or principal for the bond at outset.  # noqa: E501

        :return: The principal of this InflationLinkedBond.  # noqa: E501
        :rtype: float
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this InflationLinkedBond.

        The face-value or principal for the bond at outset.  # noqa: E501

        :param principal: The principal of this InflationLinkedBond.  # noqa: E501
        :type principal: float
        """
        if self.local_vars_configuration.client_side_validation and principal is None:  # noqa: E501
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

    @property
    def principal_protection(self):
        """Gets the principal_protection of this InflationLinkedBond.  # noqa: E501

        If true then the principal is protected in that the redemption amount will be at least the face value (Principal).  This is typically set to true for inflation linked bonds issued by the United States and France (for example).  This is typically set to false for inflation linked bonds issued by the United Kingdom (post 2005).  For other sovereigns this can vary from issue to issue.  If not set this property defaults to true.  This is sometimes referred to as Deflation protection or an inflation floor of 0%.  # noqa: E501

        :return: The principal_protection of this InflationLinkedBond.  # noqa: E501
        :rtype: bool
        """
        return self._principal_protection

    @principal_protection.setter
    def principal_protection(self, principal_protection):
        """Sets the principal_protection of this InflationLinkedBond.

        If true then the principal is protected in that the redemption amount will be at least the face value (Principal).  This is typically set to true for inflation linked bonds issued by the United States and France (for example).  This is typically set to false for inflation linked bonds issued by the United Kingdom (post 2005).  For other sovereigns this can vary from issue to issue.  If not set this property defaults to true.  This is sometimes referred to as Deflation protection or an inflation floor of 0%.  # noqa: E501

        :param principal_protection: The principal_protection of this InflationLinkedBond.  # noqa: E501
        :type principal_protection: bool
        """

        self._principal_protection = principal_protection

    @property
    def stub_type(self):
        """Gets the stub_type of this InflationLinkedBond.  # noqa: E501

        StubType. Most Inflation linked bonds have a ShortFront stub type so this is the default, however in some cases  with a long front stub LongFront should be selected.  StubType Both is not supported for InflationLinkedBonds.    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both].  # noqa: E501

        :return: The stub_type of this InflationLinkedBond.  # noqa: E501
        :rtype: str
        """
        return self._stub_type

    @stub_type.setter
    def stub_type(self, stub_type):
        """Sets the stub_type of this InflationLinkedBond.

        StubType. Most Inflation linked bonds have a ShortFront stub type so this is the default, however in some cases  with a long front stub LongFront should be selected.  StubType Both is not supported for InflationLinkedBonds.    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both].  # noqa: E501

        :param stub_type: The stub_type of this InflationLinkedBond.  # noqa: E501
        :type stub_type: str
        """

        self._stub_type = stub_type

    @property
    def instrument_type(self):
        """Gets the instrument_type of this InflationLinkedBond.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :return: The instrument_type of this InflationLinkedBond.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this InflationLinkedBond.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :param instrument_type: The instrument_type of this InflationLinkedBond.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap", "SimpleCashFlowLoan"]  # noqa: E501
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
        if not isinstance(other, InflationLinkedBond):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InflationLinkedBond):
            return True

        return self.to_dict() != other.to_dict()
