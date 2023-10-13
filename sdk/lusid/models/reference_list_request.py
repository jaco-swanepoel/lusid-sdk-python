# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.611
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


class ReferenceListRequest(object):
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
        'id': 'ResourceId',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'reference_list': 'ReferenceList'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'reference_list': 'referenceList'
    }

    required_map = {
        'id': 'required',
        'name': 'required',
        'description': 'optional',
        'tags': 'optional',
        'reference_list': 'required'
    }

    def __init__(self, id=None, name=None, description=None, tags=None, reference_list=None, local_vars_configuration=None):  # noqa: E501
        """ReferenceListRequest - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param name:  The name of the reference list. (required)
        :type name: str
        :param description:  The description of the reference list.
        :type description: str
        :param tags:  The tags associated with the reference list.
        :type tags: list[str]
        :param reference_list:  (required)
        :type reference_list: lusid.ReferenceList

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._tags = None
        self._reference_list = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.tags = tags
        self.reference_list = reference_list

    @property
    def id(self):
        """Gets the id of this ReferenceListRequest.  # noqa: E501


        :return: The id of this ReferenceListRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReferenceListRequest.


        :param id: The id of this ReferenceListRequest.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReferenceListRequest.  # noqa: E501

        The name of the reference list.  # noqa: E501

        :return: The name of this ReferenceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReferenceListRequest.

        The name of the reference list.  # noqa: E501

        :param name: The name of this ReferenceListRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ReferenceListRequest.  # noqa: E501

        The description of the reference list.  # noqa: E501

        :return: The description of this ReferenceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReferenceListRequest.

        The description of the reference list.  # noqa: E501

        :param description: The description of this ReferenceListRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this ReferenceListRequest.  # noqa: E501

        The tags associated with the reference list.  # noqa: E501

        :return: The tags of this ReferenceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReferenceListRequest.

        The tags associated with the reference list.  # noqa: E501

        :param tags: The tags of this ReferenceListRequest.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def reference_list(self):
        """Gets the reference_list of this ReferenceListRequest.  # noqa: E501


        :return: The reference_list of this ReferenceListRequest.  # noqa: E501
        :rtype: lusid.ReferenceList
        """
        return self._reference_list

    @reference_list.setter
    def reference_list(self, reference_list):
        """Sets the reference_list of this ReferenceListRequest.


        :param reference_list: The reference_list of this ReferenceListRequest.  # noqa: E501
        :type reference_list: lusid.ReferenceList
        """
        if self.local_vars_configuration.client_side_validation and reference_list is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_list`, must not be `None`")  # noqa: E501

        self._reference_list = reference_list

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
        if not isinstance(other, ReferenceListRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferenceListRequest):
            return True

        return self.to_dict() != other.to_dict()
