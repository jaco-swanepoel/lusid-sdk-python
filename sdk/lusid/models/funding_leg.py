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
from pydantic import Field, StrictFloat, StrictInt, StrictStr, validator
from lusid.models.instrument_leg import InstrumentLeg
from lusid.models.leg_definition import LegDefinition

class FundingLeg(InstrumentLeg):
    """
    LUSID representation of a Funding Leg with variable notional.    This Funding Leg is a hybrid between a single leg swap and a loan facility; the notional is not fixed and can vary within a reset period.                 The model can be used to represent the funding leg of a basket of instruments (e.g. equities) where the contents  of the basket can change over time. The actual notional history is stored in the FundingLegHistory object.     The actual notional history is stored in the FundingLegHistory object.                The main analytic calculated for this instrument is Accrual rather than PV.  # noqa: E501
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date.")
    leg_definition: LegDefinition = Field(..., alias="legDefinition")
    notional: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The initial notional of the Funding Leg instrument.  When \"RequiresFundingLegHistory\" property key is present in transaction key, during a GetValuation endpoint call (for instance),  this field would overriden by the Funding Leg history's notional and this notional field would not be used in the pricing and accrual calculations.  As such, we recommend setting this to 0 or not setting it at all.  Please see the following Notebook example and Knowledge Base article:  Notebook: https://github.com/finbourne/sample-notebooks/blob/master/examples/use-cases/instruments/Funding%20Leg%20Swap.ipynb  Knowledge Base article: https://support.lusid.com/knowledgebase/article/KA-01764/")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "legDefinition", "notional"]

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
    def from_json(cls, json_str: str) -> FundingLeg:
        """Create an instance of FundingLeg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of leg_definition
        if self.leg_definition:
            _dict['legDefinition'] = self.leg_definition.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if notional (nullable) is None
        # and __fields_set__ contains the field
        if self.notional is None and "notional" in self.__fields_set__:
            _dict['notional'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FundingLeg:
        """Create an instance of FundingLeg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FundingLeg.parse_obj(obj)

        _obj = FundingLeg.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "leg_definition": LegDefinition.from_dict(obj.get("legDefinition")) if obj.get("legDefinition") is not None else None,
            "notional": obj.get("notional")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
