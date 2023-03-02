# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5297
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


class CustodianAccount(object):
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
        'custodian_account_id': 'ResourceId',
        'status': 'str',
        'account_number': 'str',
        'account_name': 'str',
        'accounting_method': 'str',
        'currency': 'str',
        'properties': 'dict(str, ModelProperty)',
        'custodian': 'LegalEntity',
        'account_type': 'str'
    }

    attribute_map = {
        'custodian_account_id': 'custodianAccountId',
        'status': 'status',
        'account_number': 'accountNumber',
        'account_name': 'accountName',
        'accounting_method': 'accountingMethod',
        'currency': 'currency',
        'properties': 'properties',
        'custodian': 'custodian',
        'account_type': 'accountType'
    }

    required_map = {
        'custodian_account_id': 'required',
        'status': 'required',
        'account_number': 'required',
        'account_name': 'required',
        'accounting_method': 'required',
        'currency': 'required',
        'properties': 'optional',
        'custodian': 'required',
        'account_type': 'required'
    }

    def __init__(self, custodian_account_id=None, status=None, account_number=None, account_name=None, accounting_method=None, currency=None, properties=None, custodian=None, account_type=None, local_vars_configuration=None):  # noqa: E501
        """CustodianAccount - a model defined in OpenAPI"
        
        :param custodian_account_id:  (required)
        :type custodian_account_id: lusid.ResourceId
        :param status:  The account status. Can be Active, Inactive or Deleted. Defaults to Active. (required)
        :type status: str
        :param account_number:  The Custodian Account Number (required)
        :type account_number: str
        :param account_name:  The identifiable name given to the Custodian Account (required)
        :type account_name: str
        :param accounting_method:  The Accounting method to be used (required)
        :type accounting_method: str
        :param currency:  The Currency for the Account (required)
        :type currency: str
        :param properties:  Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param custodian:  (required)
        :type custodian: lusid.LegalEntity
        :param account_type:  The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin. (required)
        :type account_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._custodian_account_id = None
        self._status = None
        self._account_number = None
        self._account_name = None
        self._accounting_method = None
        self._currency = None
        self._properties = None
        self._custodian = None
        self._account_type = None
        self.discriminator = None

        self.custodian_account_id = custodian_account_id
        self.status = status
        self.account_number = account_number
        self.account_name = account_name
        self.accounting_method = accounting_method
        self.currency = currency
        self.properties = properties
        self.custodian = custodian
        self.account_type = account_type

    @property
    def custodian_account_id(self):
        """Gets the custodian_account_id of this CustodianAccount.  # noqa: E501


        :return: The custodian_account_id of this CustodianAccount.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._custodian_account_id

    @custodian_account_id.setter
    def custodian_account_id(self, custodian_account_id):
        """Sets the custodian_account_id of this CustodianAccount.


        :param custodian_account_id: The custodian_account_id of this CustodianAccount.  # noqa: E501
        :type custodian_account_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and custodian_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `custodian_account_id`, must not be `None`")  # noqa: E501

        self._custodian_account_id = custodian_account_id

    @property
    def status(self):
        """Gets the status of this CustodianAccount.  # noqa: E501

        The account status. Can be Active, Inactive or Deleted. Defaults to Active.  # noqa: E501

        :return: The status of this CustodianAccount.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustodianAccount.

        The account status. Can be Active, Inactive or Deleted. Defaults to Active.  # noqa: E501

        :param status: The status of this CustodianAccount.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def account_number(self):
        """Gets the account_number of this CustodianAccount.  # noqa: E501

        The Custodian Account Number  # noqa: E501

        :return: The account_number of this CustodianAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CustodianAccount.

        The Custodian Account Number  # noqa: E501

        :param account_number: The account_number of this CustodianAccount.  # noqa: E501
        :type account_number: str
        """
        if self.local_vars_configuration.client_side_validation and account_number is None:  # noqa: E501
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_number is not None and len(account_number) > 64):
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_number is not None and len(account_number) < 1):
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_number = account_number

    @property
    def account_name(self):
        """Gets the account_name of this CustodianAccount.  # noqa: E501

        The identifiable name given to the Custodian Account  # noqa: E501

        :return: The account_name of this CustodianAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this CustodianAccount.

        The identifiable name given to the Custodian Account  # noqa: E501

        :param account_name: The account_name of this CustodianAccount.  # noqa: E501
        :type account_name: str
        """
        if self.local_vars_configuration.client_side_validation and account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_name is not None and len(account_name) < 1):
            raise ValueError("Invalid value for `account_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_name = account_name

    @property
    def accounting_method(self):
        """Gets the accounting_method of this CustodianAccount.  # noqa: E501

        The Accounting method to be used  # noqa: E501

        :return: The accounting_method of this CustodianAccount.  # noqa: E501
        :rtype: str
        """
        return self._accounting_method

    @accounting_method.setter
    def accounting_method(self, accounting_method):
        """Sets the accounting_method of this CustodianAccount.

        The Accounting method to be used  # noqa: E501

        :param accounting_method: The accounting_method of this CustodianAccount.  # noqa: E501
        :type accounting_method: str
        """
        if self.local_vars_configuration.client_side_validation and accounting_method is None:  # noqa: E501
            raise ValueError("Invalid value for `accounting_method`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accounting_method is not None and len(accounting_method) < 1):
            raise ValueError("Invalid value for `accounting_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._accounting_method = accounting_method

    @property
    def currency(self):
        """Gets the currency of this CustodianAccount.  # noqa: E501

        The Currency for the Account  # noqa: E501

        :return: The currency of this CustodianAccount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CustodianAccount.

        The Currency for the Account  # noqa: E501

        :param currency: The currency of this CustodianAccount.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def properties(self):
        """Gets the properties of this CustodianAccount.  # noqa: E501

        Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.  # noqa: E501

        :return: The properties of this CustodianAccount.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CustodianAccount.

        Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.  # noqa: E501

        :param properties: The properties of this CustodianAccount.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def custodian(self):
        """Gets the custodian of this CustodianAccount.  # noqa: E501


        :return: The custodian of this CustodianAccount.  # noqa: E501
        :rtype: lusid.LegalEntity
        """
        return self._custodian

    @custodian.setter
    def custodian(self, custodian):
        """Sets the custodian of this CustodianAccount.


        :param custodian: The custodian of this CustodianAccount.  # noqa: E501
        :type custodian: lusid.LegalEntity
        """
        if self.local_vars_configuration.client_side_validation and custodian is None:  # noqa: E501
            raise ValueError("Invalid value for `custodian`, must not be `None`")  # noqa: E501

        self._custodian = custodian

    @property
    def account_type(self):
        """Gets the account_type of this CustodianAccount.  # noqa: E501

        The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.  # noqa: E501

        :return: The account_type of this CustodianAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CustodianAccount.

        The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.  # noqa: E501

        :param account_type: The account_type of this CustodianAccount.  # noqa: E501
        :type account_type: str
        """
        if self.local_vars_configuration.client_side_validation and account_type is None:  # noqa: E501
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_type is not None and len(account_type) < 1):
            raise ValueError("Invalid value for `account_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_type = account_type

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
        if not isinstance(other, CustodianAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustodianAccount):
            return True

        return self.to_dict() != other.to_dict()
