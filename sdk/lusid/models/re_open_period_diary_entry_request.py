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
from pydantic import BaseModel, Field, constr, validator

class ReOpenPeriodDiaryEntryRequest(BaseModel):
    """
    A definition for the period you wish to re open  # noqa: E501
    """
    diary_entry_code: Optional[constr(strict=True, max_length=64, min_length=0)] = Field(None, alias="diaryEntryCode", description="Unique code assigned to a period. When left blank last period will be used.")
    __properties = ["diaryEntryCode"]

    @validator('diary_entry_code')
    def diary_entry_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
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
    def from_json(cls, json_str: str) -> ReOpenPeriodDiaryEntryRequest:
        """Create an instance of ReOpenPeriodDiaryEntryRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if diary_entry_code (nullable) is None
        # and __fields_set__ contains the field
        if self.diary_entry_code is None and "diary_entry_code" in self.__fields_set__:
            _dict['diaryEntryCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReOpenPeriodDiaryEntryRequest:
        """Create an instance of ReOpenPeriodDiaryEntryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReOpenPeriodDiaryEntryRequest.parse_obj(obj)

        _obj = ReOpenPeriodDiaryEntryRequest.parse_obj({
            "diary_entry_code": obj.get("diaryEntryCode")
        })
        return _obj
