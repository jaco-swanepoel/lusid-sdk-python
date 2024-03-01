# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional, Union
from pydantic import Field, StrictFloat, StrictInt, StrictStr, constr, validator
from lusid.models.flow_conventions import FlowConventions
from lusid.models.inflation_index_conventions import InflationIndexConventions
from lusid.models.lusid_instrument import LusidInstrument

class InflationLeg(LusidInstrument):
    """
    LUSID representation of an Inflation Leg.  This leg instrument is part of the InflationSwap instrument, but can also be used as a standalone instrument.  The implementation supports the following inflation leg types:  * Zero Coupon inflation leg (CPI Leg), with a single payment at maturity.  * Year on Year inflation leg  * LPI Swap Leg (capped and floored YoY)  # noqa: E501
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    flow_conventions: FlowConventions = Field(..., alias="flowConventions")
    base_cpi: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="baseCPI", description="Optional BaseCPI, if specified it will be used in place of BaseCPI(StartDate).  This should not be required for standard inflation swaps.")
    calculation_type: constr(strict=True, max_length=32, min_length=0) = Field(..., alias="calculationType", description="The calculation type.  ZeroCoupon is used for CPILegs where there is a single payment at maturity of  Notional * (CPI(T) / CPI(T0) - 1)  where CPI(T0) is the BaseCPI of this leg  YearOnYear is used for YoY and LPI swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(t-1) - 1)  If a cap and floor is added to this it becomes an LPI swap leg.  Compounded is used for inflation swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(T0) - 1)  i.e. the BaseCPI is used every year. These swaps are not as common as CPI or    Supported string (enumeration) values are: [ZeroCoupon, YearOnYear, Compounded].")
    cap_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="capRate", description="Optional cap, needed for LPI Legs or CPI Legs with Caps")
    floor_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="floorRate", description="Optional floor, needed for LPI Legs or CPI Legs with Floors.")
    inflation_index_conventions: InflationIndexConventions = Field(..., alias="inflationIndexConventions")
    notional: Union[StrictFloat, StrictInt] = Field(..., description="The notional")
    pay_receive: Optional[constr(strict=True, max_length=32, min_length=0)] = Field(None, alias="payReceive", description="PayReceive flag for the inflation leg.  This field is optional and defaults to Pay.    Supported string (enumeration) values are: [Pay, Receive].")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "flowConventions", "baseCPI", "calculationType", "capRate", "floorRate", "inflationIndexConventions", "notional", "payReceive"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> InflationLeg:
        """Create an instance of InflationLeg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_conventions
        if self.flow_conventions:
            _dict['flowConventions'] = self.flow_conventions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inflation_index_conventions
        if self.inflation_index_conventions:
            _dict['inflationIndexConventions'] = self.inflation_index_conventions.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if base_cpi (nullable) is None
        # and __fields_set__ contains the field
        if self.base_cpi is None and "base_cpi" in self.__fields_set__:
            _dict['baseCPI'] = None

        # set to None if cap_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.cap_rate is None and "cap_rate" in self.__fields_set__:
            _dict['capRate'] = None

        # set to None if floor_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.floor_rate is None and "floor_rate" in self.__fields_set__:
            _dict['floorRate'] = None

        # set to None if pay_receive (nullable) is None
        # and __fields_set__ contains the field
        if self.pay_receive is None and "pay_receive" in self.__fields_set__:
            _dict['payReceive'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InflationLeg:
        """Create an instance of InflationLeg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InflationLeg.parse_obj(obj)

        _obj = InflationLeg.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "flow_conventions": FlowConventions.from_dict(obj.get("flowConventions")) if obj.get("flowConventions") is not None else None,
            "base_cpi": obj.get("baseCPI"),
            "calculation_type": obj.get("calculationType"),
            "cap_rate": obj.get("capRate"),
            "floor_rate": obj.get("floorRate"),
            "inflation_index_conventions": InflationIndexConventions.from_dict(obj.get("inflationIndexConventions")) if obj.get("inflationIndexConventions") is not None else None,
            "notional": obj.get("notional"),
            "pay_receive": obj.get("payReceive")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
