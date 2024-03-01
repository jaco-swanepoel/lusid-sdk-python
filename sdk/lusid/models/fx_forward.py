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
from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from lusid.models.lusid_instrument import LusidInstrument

class FxForward(LusidInstrument):
    """
    LUSID representation of an FX Forward.  Including FX Spot and Non-Deliverable Forwards.                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | DomesticLeg | Cash flows in the domestic currency of the forward. |  | 2 | ForeignLeg | Cash flows in the foreign currency of the forward (not present for non-deliverable forwards). |  # noqa: E501
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    dom_amount: Union[StrictFloat, StrictInt] = Field(..., alias="domAmount", description="The amount that is to be paid in the domestic currency on the maturity date.")
    dom_ccy: StrictStr = Field(..., alias="domCcy", description="The domestic currency of the instrument.")
    fgn_amount: Union[StrictFloat, StrictInt] = Field(..., alias="fgnAmount", description="The amount that is to be paid in the foreign currency on the maturity date.")
    fgn_ccy: StrictStr = Field(..., alias="fgnCcy", description="The foreign (other) currency of the instrument. In the NDF case, only payments are made in the domestic currency.  For the outright forward, currencies are exchanged. By domestic is then that of the portfolio.")
    ref_spot_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="refSpotRate", description="The reference Fx Spot rate for currency pair Foreign-Domestic that was seen on the trade start date (time).")
    is_ndf: Optional[StrictBool] = Field(None, alias="isNdf", description="Is the contract an Fx-Forward of \"Non-Deliverable\" type, meaning a single payment in the domestic currency based on the change in fx-rate vs  a reference rate is used.")
    fixing_date: Optional[datetime] = Field(None, alias="fixingDate", description="The fixing date.")
    settlement_ccy: Optional[StrictStr] = Field(None, alias="settlementCcy", description="The settlement currency.  If provided, present value will be calculated in settlement currency, otherwise the domestic currency. Applies only to non-deliverable FX Forwards.")
    booked_as_spot: Optional[StrictBool] = Field(None, alias="bookedAsSpot", description="Boolean flag for FX Forward transactions booked with Spot settlement. This will default to False if not provided.  For information purposes only, this does not impact LUSID valuation, analytics, cashflows or events, but may be used by third party vendors.")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "domAmount", "domCcy", "fgnAmount", "fgnCcy", "refSpotRate", "isNdf", "fixingDate", "settlementCcy", "bookedAsSpot"]

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
    def from_json(cls, json_str: str) -> FxForward:
        """Create an instance of FxForward from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if settlement_ccy (nullable) is None
        # and __fields_set__ contains the field
        if self.settlement_ccy is None and "settlement_ccy" in self.__fields_set__:
            _dict['settlementCcy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FxForward:
        """Create an instance of FxForward from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxForward.parse_obj(obj)

        _obj = FxForward.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "dom_amount": obj.get("domAmount"),
            "dom_ccy": obj.get("domCcy"),
            "fgn_amount": obj.get("fgnAmount"),
            "fgn_ccy": obj.get("fgnCcy"),
            "ref_spot_rate": obj.get("refSpotRate"),
            "is_ndf": obj.get("isNdf"),
            "fixing_date": obj.get("fixingDate"),
            "settlement_ccy": obj.get("settlementCcy"),
            "booked_as_spot": obj.get("bookedAsSpot")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
