# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2805
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CreateReferencePortfolioRequest(object):
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
        'display_name': 'str',
        'description': 'str',
        'code': 'str',
        'created': 'datetime',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'code': 'code',
        'created': 'created',
        'properties': 'properties'
    }

    required_map = {
        'display_name': 'required',
        'description': 'optional',
        'code': 'required',
        'created': 'optional',
        'properties': 'optional'
    }

    def __init__(self, display_name=None, description=None, code=None, created=None, properties=None):  # noqa: E501
        """
        CreateReferencePortfolioRequest - a model defined in OpenAPI

        :param display_name:  (required)
        :type display_name: str
        :param description: 
        :type description: str
        :param code:  (required)
        :type code: str
        :param created: 
        :type created: datetime
        :param properties:  Portfolio properties to add to the portfolio
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501

        self._display_name = None
        self._description = None
        self._code = None
        self._created = None
        self._properties = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.code = code
        self.created = created
        self.properties = properties

    @property
    def display_name(self):
        """Gets the display_name of this CreateReferencePortfolioRequest.  # noqa: E501


        :return: The display_name of this CreateReferencePortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateReferencePortfolioRequest.


        :param display_name: The display_name of this CreateReferencePortfolioRequest.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CreateReferencePortfolioRequest.  # noqa: E501


        :return: The description of this CreateReferencePortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateReferencePortfolioRequest.


        :param description: The description of this CreateReferencePortfolioRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def code(self):
        """Gets the code of this CreateReferencePortfolioRequest.  # noqa: E501


        :return: The code of this CreateReferencePortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateReferencePortfolioRequest.


        :param code: The code of this CreateReferencePortfolioRequest.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def created(self):
        """Gets the created of this CreateReferencePortfolioRequest.  # noqa: E501


        :return: The created of this CreateReferencePortfolioRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreateReferencePortfolioRequest.


        :param created: The created of this CreateReferencePortfolioRequest.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def properties(self):
        """Gets the properties of this CreateReferencePortfolioRequest.  # noqa: E501

        Portfolio properties to add to the portfolio  # noqa: E501

        :return: The properties of this CreateReferencePortfolioRequest.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateReferencePortfolioRequest.

        Portfolio properties to add to the portfolio  # noqa: E501

        :param properties: The properties of this CreateReferencePortfolioRequest.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._properties = properties

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
        if not isinstance(other, CreateReferencePortfolioRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
