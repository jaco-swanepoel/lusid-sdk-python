# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.224
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


class ErrorDetail(object):
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
        'id': 'str',
        'type': 'str',
        'detail': 'str',
        'error_details': 'list[dict(str, str)]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'detail': 'detail',
        'error_details': 'errorDetails'
    }

    required_map = {
        'id': 'optional',
        'type': 'optional',
        'detail': 'optional',
        'error_details': 'optional'
    }

    def __init__(self, id=None, type=None, detail=None, error_details=None, local_vars_configuration=None):  # noqa: E501
        """ErrorDetail - a model defined in OpenAPI"
        
        :param id:  The id of the failed item that this error relates to.
        :type id: str
        :param type:  The type of failure that occurred.
        :type type: str
        :param detail:  Description of the failure that occurred.
        :type detail: str
        :param error_details:  Information about the particular instance of the failure (supplied information depends on the type of failure).
        :type error_details: list[dict(str, str)]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._detail = None
        self._error_details = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.detail = detail
        self.error_details = error_details

    @property
    def id(self):
        """Gets the id of this ErrorDetail.  # noqa: E501

        The id of the failed item that this error relates to.  # noqa: E501

        :return: The id of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ErrorDetail.

        The id of the failed item that this error relates to.  # noqa: E501

        :param id: The id of this ErrorDetail.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ErrorDetail.  # noqa: E501

        The type of failure that occurred.  # noqa: E501

        :return: The type of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ErrorDetail.

        The type of failure that occurred.  # noqa: E501

        :param type: The type of this ErrorDetail.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def detail(self):
        """Gets the detail of this ErrorDetail.  # noqa: E501

        Description of the failure that occurred.  # noqa: E501

        :return: The detail of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorDetail.

        Description of the failure that occurred.  # noqa: E501

        :param detail: The detail of this ErrorDetail.  # noqa: E501
        :type detail: str
        """

        self._detail = detail

    @property
    def error_details(self):
        """Gets the error_details of this ErrorDetail.  # noqa: E501

        Information about the particular instance of the failure (supplied information depends on the type of failure).  # noqa: E501

        :return: The error_details of this ErrorDetail.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this ErrorDetail.

        Information about the particular instance of the failure (supplied information depends on the type of failure).  # noqa: E501

        :param error_details: The error_details of this ErrorDetail.  # noqa: E501
        :type error_details: list[dict(str, str)]
        """

        self._error_details = error_details

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
        if not isinstance(other, ErrorDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorDetail):
            return True

        return self.to_dict() != other.to_dict()
