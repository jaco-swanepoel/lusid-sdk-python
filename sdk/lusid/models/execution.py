# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5111
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


class Execution(object):
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
        'placement_id': 'ResourceId',
        'properties': 'dict(str, PerpetualProperty)',
        'instrument_identifiers': 'dict(str, str)',
        'lusid_instrument_id': 'str',
        'quantity': 'float',
        'state': 'str',
        'side': 'str',
        'type': 'str',
        'created_date': 'datetime',
        'settlement_date': 'datetime',
        'price': 'CurrencyAndAmount',
        'settlement_currency': 'str',
        'settlement_currency_fx_rate': 'float',
        'counterparty': 'str',
        'average_price': 'float',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'placement_id': 'placementId',
        'properties': 'properties',
        'instrument_identifiers': 'instrumentIdentifiers',
        'lusid_instrument_id': 'lusidInstrumentId',
        'quantity': 'quantity',
        'state': 'state',
        'side': 'side',
        'type': 'type',
        'created_date': 'createdDate',
        'settlement_date': 'settlementDate',
        'price': 'price',
        'settlement_currency': 'settlementCurrency',
        'settlement_currency_fx_rate': 'settlementCurrencyFxRate',
        'counterparty': 'counterparty',
        'average_price': 'averagePrice',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'placement_id': 'required',
        'properties': 'optional',
        'instrument_identifiers': 'required',
        'lusid_instrument_id': 'required',
        'quantity': 'required',
        'state': 'required',
        'side': 'required',
        'type': 'required',
        'created_date': 'required',
        'settlement_date': 'optional',
        'price': 'required',
        'settlement_currency': 'required',
        'settlement_currency_fx_rate': 'required',
        'counterparty': 'required',
        'average_price': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, placement_id=None, properties=None, instrument_identifiers=None, lusid_instrument_id=None, quantity=None, state=None, side=None, type=None, created_date=None, settlement_date=None, price=None, settlement_currency=None, settlement_currency_fx_rate=None, counterparty=None, average_price=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Execution - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param placement_id:  (required)
        :type placement_id: lusid.ResourceId
        :param properties:  Client-defined properties associated with this execution.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param instrument_identifiers:  The instrument ordered. (required)
        :type instrument_identifiers: dict(str, str)
        :param lusid_instrument_id:  The LUSID instrument id for the instrument execution. (required)
        :type lusid_instrument_id: str
        :param quantity:  The quantity of given instrument ordered. (required)
        :type quantity: float
        :param state:  The state of this execution (typically a FIX state; Open, Filled, etc). (required)
        :type state: str
        :param side:  The side (Buy, Sell, ...) of this execution. (required)
        :type side: str
        :param type:  The type of this execution (Market, Limit, etc). (required)
        :type type: str
        :param created_date:  The active date of this execution. (required)
        :type created_date: datetime
        :param settlement_date:  The (optional) settlement date for this execution
        :type settlement_date: datetime
        :param price:  (required)
        :type price: lusid.CurrencyAndAmount
        :param settlement_currency:  The execution's settlement currency. (required)
        :type settlement_currency: str
        :param settlement_currency_fx_rate:  The exectuion's settlement currency rate. (required)
        :type settlement_currency_fx_rate: float
        :param counterparty:  The market entity this placement is placed with. (required)
        :type counterparty: str
        :param average_price:  The average price of all executions for a given placement at the time of upsert
        :type average_price: float
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._placement_id = None
        self._properties = None
        self._instrument_identifiers = None
        self._lusid_instrument_id = None
        self._quantity = None
        self._state = None
        self._side = None
        self._type = None
        self._created_date = None
        self._settlement_date = None
        self._price = None
        self._settlement_currency = None
        self._settlement_currency_fx_rate = None
        self._counterparty = None
        self._average_price = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.placement_id = placement_id
        self.properties = properties
        self.instrument_identifiers = instrument_identifiers
        self.lusid_instrument_id = lusid_instrument_id
        self.quantity = quantity
        self.state = state
        self.side = side
        self.type = type
        self.created_date = created_date
        self.settlement_date = settlement_date
        self.price = price
        self.settlement_currency = settlement_currency
        self.settlement_currency_fx_rate = settlement_currency_fx_rate
        self.counterparty = counterparty
        self.average_price = average_price
        if version is not None:
            self.version = version
        self.links = links

    @property
    def id(self):
        """Gets the id of this Execution.  # noqa: E501


        :return: The id of this Execution.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Execution.


        :param id: The id of this Execution.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def placement_id(self):
        """Gets the placement_id of this Execution.  # noqa: E501


        :return: The placement_id of this Execution.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._placement_id

    @placement_id.setter
    def placement_id(self, placement_id):
        """Sets the placement_id of this Execution.


        :param placement_id: The placement_id of this Execution.  # noqa: E501
        :type placement_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and placement_id is None:  # noqa: E501
            raise ValueError("Invalid value for `placement_id`, must not be `None`")  # noqa: E501

        self._placement_id = placement_id

    @property
    def properties(self):
        """Gets the properties of this Execution.  # noqa: E501

        Client-defined properties associated with this execution.  # noqa: E501

        :return: The properties of this Execution.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Execution.

        Client-defined properties associated with this execution.  # noqa: E501

        :param properties: The properties of this Execution.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this Execution.  # noqa: E501

        The instrument ordered.  # noqa: E501

        :return: The instrument_identifiers of this Execution.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this Execution.

        The instrument ordered.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this Execution.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def lusid_instrument_id(self):
        """Gets the lusid_instrument_id of this Execution.  # noqa: E501

        The LUSID instrument id for the instrument execution.  # noqa: E501

        :return: The lusid_instrument_id of this Execution.  # noqa: E501
        :rtype: str
        """
        return self._lusid_instrument_id

    @lusid_instrument_id.setter
    def lusid_instrument_id(self, lusid_instrument_id):
        """Sets the lusid_instrument_id of this Execution.

        The LUSID instrument id for the instrument execution.  # noqa: E501

        :param lusid_instrument_id: The lusid_instrument_id of this Execution.  # noqa: E501
        :type lusid_instrument_id: str
        """
        if self.local_vars_configuration.client_side_validation and lusid_instrument_id is None:  # noqa: E501
            raise ValueError("Invalid value for `lusid_instrument_id`, must not be `None`")  # noqa: E501

        self._lusid_instrument_id = lusid_instrument_id

    @property
    def quantity(self):
        """Gets the quantity of this Execution.  # noqa: E501

        The quantity of given instrument ordered.  # noqa: E501

        :return: The quantity of this Execution.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Execution.

        The quantity of given instrument ordered.  # noqa: E501

        :param quantity: The quantity of this Execution.  # noqa: E501
        :type quantity: float
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def state(self):
        """Gets the state of this Execution.  # noqa: E501

        The state of this execution (typically a FIX state; Open, Filled, etc).  # noqa: E501

        :return: The state of this Execution.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Execution.

        The state of this execution (typically a FIX state; Open, Filled, etc).  # noqa: E501

        :param state: The state of this Execution.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def side(self):
        """Gets the side of this Execution.  # noqa: E501

        The side (Buy, Sell, ...) of this execution.  # noqa: E501

        :return: The side of this Execution.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Execution.

        The side (Buy, Sell, ...) of this execution.  # noqa: E501

        :param side: The side of this Execution.  # noqa: E501
        :type side: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def type(self):
        """Gets the type of this Execution.  # noqa: E501

        The type of this execution (Market, Limit, etc).  # noqa: E501

        :return: The type of this Execution.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Execution.

        The type of this execution (Market, Limit, etc).  # noqa: E501

        :param type: The type of this Execution.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def created_date(self):
        """Gets the created_date of this Execution.  # noqa: E501

        The active date of this execution.  # noqa: E501

        :return: The created_date of this Execution.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Execution.

        The active date of this execution.  # noqa: E501

        :param created_date: The created_date of this Execution.  # noqa: E501
        :type created_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_date is None:  # noqa: E501
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this Execution.  # noqa: E501

        The (optional) settlement date for this execution  # noqa: E501

        :return: The settlement_date of this Execution.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this Execution.

        The (optional) settlement date for this execution  # noqa: E501

        :param settlement_date: The settlement_date of this Execution.  # noqa: E501
        :type settlement_date: datetime
        """

        self._settlement_date = settlement_date

    @property
    def price(self):
        """Gets the price of this Execution.  # noqa: E501


        :return: The price of this Execution.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Execution.


        :param price: The price of this Execution.  # noqa: E501
        :type price: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def settlement_currency(self):
        """Gets the settlement_currency of this Execution.  # noqa: E501

        The execution's settlement currency.  # noqa: E501

        :return: The settlement_currency of this Execution.  # noqa: E501
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """Sets the settlement_currency of this Execution.

        The execution's settlement currency.  # noqa: E501

        :param settlement_currency: The settlement_currency of this Execution.  # noqa: E501
        :type settlement_currency: str
        """
        if self.local_vars_configuration.client_side_validation and settlement_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `settlement_currency`, must not be `None`")  # noqa: E501

        self._settlement_currency = settlement_currency

    @property
    def settlement_currency_fx_rate(self):
        """Gets the settlement_currency_fx_rate of this Execution.  # noqa: E501

        The exectuion's settlement currency rate.  # noqa: E501

        :return: The settlement_currency_fx_rate of this Execution.  # noqa: E501
        :rtype: float
        """
        return self._settlement_currency_fx_rate

    @settlement_currency_fx_rate.setter
    def settlement_currency_fx_rate(self, settlement_currency_fx_rate):
        """Sets the settlement_currency_fx_rate of this Execution.

        The exectuion's settlement currency rate.  # noqa: E501

        :param settlement_currency_fx_rate: The settlement_currency_fx_rate of this Execution.  # noqa: E501
        :type settlement_currency_fx_rate: float
        """
        if self.local_vars_configuration.client_side_validation and settlement_currency_fx_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `settlement_currency_fx_rate`, must not be `None`")  # noqa: E501

        self._settlement_currency_fx_rate = settlement_currency_fx_rate

    @property
    def counterparty(self):
        """Gets the counterparty of this Execution.  # noqa: E501

        The market entity this placement is placed with.  # noqa: E501

        :return: The counterparty of this Execution.  # noqa: E501
        :rtype: str
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty):
        """Sets the counterparty of this Execution.

        The market entity this placement is placed with.  # noqa: E501

        :param counterparty: The counterparty of this Execution.  # noqa: E501
        :type counterparty: str
        """
        if self.local_vars_configuration.client_side_validation and counterparty is None:  # noqa: E501
            raise ValueError("Invalid value for `counterparty`, must not be `None`")  # noqa: E501

        self._counterparty = counterparty

    @property
    def average_price(self):
        """Gets the average_price of this Execution.  # noqa: E501

        The average price of all executions for a given placement at the time of upsert  # noqa: E501

        :return: The average_price of this Execution.  # noqa: E501
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this Execution.

        The average price of all executions for a given placement at the time of upsert  # noqa: E501

        :param average_price: The average_price of this Execution.  # noqa: E501
        :type average_price: float
        """

        self._average_price = average_price

    @property
    def version(self):
        """Gets the version of this Execution.  # noqa: E501


        :return: The version of this Execution.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Execution.


        :param version: The version of this Execution.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this Execution.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this Execution.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Execution.

        Collection of links.  # noqa: E501

        :param links: The links of this Execution.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, Execution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Execution):
            return True

        return self.to_dict() != other.to_dict()
