# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3226
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class InstrumentDefinition(object):
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
        'name': 'str',
        'identifiers': 'dict(str, InstrumentIdValue)',
        'properties': 'list[ModelProperty]',
        'look_through_portfolio_id': 'ResourceId',
        'definition': 'LusidInstrument'
    }

    attribute_map = {
        'name': 'name',
        'identifiers': 'identifiers',
        'properties': 'properties',
        'look_through_portfolio_id': 'lookThroughPortfolioId',
        'definition': 'definition'
    }

    required_map = {
        'name': 'required',
        'identifiers': 'required',
        'properties': 'optional',
        'look_through_portfolio_id': 'optional',
        'definition': 'optional'
    }

    def __init__(self, name=None, identifiers=None, properties=None, look_through_portfolio_id=None, definition=None):  # noqa: E501
        """
        InstrumentDefinition - a model defined in OpenAPI

        :param name:  The name of the instrument. (required)
        :type name: str
        :param identifiers:  A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. (required)
        :type identifiers: dict[str, lusid.InstrumentIdValue]
        :param properties:  Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.
        :type properties: list[lusid.ModelProperty]
        :param look_through_portfolio_id: 
        :type look_through_portfolio_id: lusid.ResourceId
        :param definition: 
        :type definition: lusid.LusidInstrument

        """  # noqa: E501

        self._name = None
        self._identifiers = None
        self._properties = None
        self._look_through_portfolio_id = None
        self._definition = None
        self.discriminator = None

        self.name = name
        self.identifiers = identifiers
        self.properties = properties
        if look_through_portfolio_id is not None:
            self.look_through_portfolio_id = look_through_portfolio_id
        if definition is not None:
            self.definition = definition

    @property
    def name(self):
        """Gets the name of this InstrumentDefinition.  # noqa: E501

        The name of the instrument.  # noqa: E501

        :return: The name of this InstrumentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstrumentDefinition.

        The name of the instrument.  # noqa: E501

        :param name: The name of this InstrumentDefinition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def identifiers(self):
        """Gets the identifiers of this InstrumentDefinition.  # noqa: E501

        A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier.  # noqa: E501

        :return: The identifiers of this InstrumentDefinition.  # noqa: E501
        :rtype: dict(str, InstrumentIdValue)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this InstrumentDefinition.

        A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier.  # noqa: E501

        :param identifiers: The identifiers of this InstrumentDefinition.  # noqa: E501
        :type: dict(str, InstrumentIdValue)
        """
        if identifiers is None:
            raise ValueError("Invalid value for `identifiers`, must not be `None`")  # noqa: E501

        self._identifiers = identifiers

    @property
    def properties(self):
        """Gets the properties of this InstrumentDefinition.  # noqa: E501

        Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.  # noqa: E501

        :return: The properties of this InstrumentDefinition.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this InstrumentDefinition.

        Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.  # noqa: E501

        :param properties: The properties of this InstrumentDefinition.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def look_through_portfolio_id(self):
        """Gets the look_through_portfolio_id of this InstrumentDefinition.  # noqa: E501


        :return: The look_through_portfolio_id of this InstrumentDefinition.  # noqa: E501
        :rtype: ResourceId
        """
        return self._look_through_portfolio_id

    @look_through_portfolio_id.setter
    def look_through_portfolio_id(self, look_through_portfolio_id):
        """Sets the look_through_portfolio_id of this InstrumentDefinition.


        :param look_through_portfolio_id: The look_through_portfolio_id of this InstrumentDefinition.  # noqa: E501
        :type: ResourceId
        """

        self._look_through_portfolio_id = look_through_portfolio_id

    @property
    def definition(self):
        """Gets the definition of this InstrumentDefinition.  # noqa: E501


        :return: The definition of this InstrumentDefinition.  # noqa: E501
        :rtype: LusidInstrument
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this InstrumentDefinition.


        :param definition: The definition of this InstrumentDefinition.  # noqa: E501
        :type: LusidInstrument
        """

        self._definition = definition

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstrumentDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
