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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr

class InflationIndexConventions(BaseModel):
    """
    A set of conventions that describe the conventions for an inflation index.  # noqa: E501
    """
    inflation_index_name: constr(strict=True, max_length=50, min_length=0) = Field(..., alias="inflationIndexName", description="Name of the index, e.g. UKRPI.")
    currency: StrictStr = Field(..., description="Currency of the inflation index convention.")
    observation_lag: constr(strict=True, max_length=32, min_length=0) = Field(..., alias="observationLag", description="Observation lag. This is a string that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds and swaps have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097)")
    inflation_interpolation: Optional[constr(strict=True, max_length=32, min_length=0)] = Field(None, alias="inflationInterpolation", description="Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat].")
    inflation_frequency: Optional[constr(strict=True, max_length=32, min_length=0)] = Field(None, alias="inflationFrequency", description="Frequency of inflation updated. Optional and defaults to Monthly which is the most common.  However both Australian and New Zealand inflation is published Quarterly. Only tenors of 1M or 3M are supported.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097)")
    inflation_roll_day: Optional[StrictInt] = Field(None, alias="inflationRollDay", description="Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th).")
    __properties = ["inflationIndexName", "currency", "observationLag", "inflationInterpolation", "inflationFrequency", "inflationRollDay"]

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
    def from_json(cls, json_str: str) -> InflationIndexConventions:
        """Create an instance of InflationIndexConventions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if inflation_interpolation (nullable) is None
        # and __fields_set__ contains the field
        if self.inflation_interpolation is None and "inflation_interpolation" in self.__fields_set__:
            _dict['inflationInterpolation'] = None

        # set to None if inflation_frequency (nullable) is None
        # and __fields_set__ contains the field
        if self.inflation_frequency is None and "inflation_frequency" in self.__fields_set__:
            _dict['inflationFrequency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InflationIndexConventions:
        """Create an instance of InflationIndexConventions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InflationIndexConventions.parse_obj(obj)

        _obj = InflationIndexConventions.parse_obj({
            "inflation_index_name": obj.get("inflationIndexName"),
            "currency": obj.get("currency"),
            "observation_lag": obj.get("observationLag"),
            "inflation_interpolation": obj.get("inflationInterpolation"),
            "inflation_frequency": obj.get("inflationFrequency"),
            "inflation_roll_day": obj.get("inflationRollDay")
        })
        return _obj
