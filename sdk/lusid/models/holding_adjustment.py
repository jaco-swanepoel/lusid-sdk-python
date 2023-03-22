# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.20
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


class HoldingAdjustment(object):
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
        'instrument_identifiers': 'dict(str, str)',
        'instrument_scope': 'str',
        'instrument_uid': 'str',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'properties': 'dict(str, PerpetualProperty)',
        'tax_lots': 'list[TargetTaxLot]',
        'currency': 'str'
    }

    attribute_map = {
        'instrument_identifiers': 'instrumentIdentifiers',
        'instrument_scope': 'instrumentScope',
        'instrument_uid': 'instrumentUid',
        'sub_holding_keys': 'subHoldingKeys',
        'properties': 'properties',
        'tax_lots': 'taxLots',
        'currency': 'currency'
    }

    required_map = {
        'instrument_identifiers': 'optional',
        'instrument_scope': 'optional',
        'instrument_uid': 'required',
        'sub_holding_keys': 'optional',
        'properties': 'optional',
        'tax_lots': 'required',
        'currency': 'optional'
    }

    def __init__(self, instrument_identifiers=None, instrument_scope=None, instrument_uid=None, sub_holding_keys=None, properties=None, tax_lots=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """HoldingAdjustment - a model defined in OpenAPI"
        
        :param instrument_identifiers:  A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.
        :type instrument_identifiers: dict(str, str)
        :param instrument_scope:  The scope of the instrument that the holding adjustment is in.
        :type instrument_scope: str
        :param instrument_uid:  The unqiue Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in. (required)
        :type instrument_uid: str
        :param sub_holding_keys:  The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the 'Transaction' domain.
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param properties:  The set of unique holding properties and associated values stored with the target holding. Each property will be from the 'Holding' domain.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param tax_lots:  The tax-lots that together make up the target holding. (required)
        :type tax_lots: list[lusid.TargetTaxLot]
        :param currency:  The Holding currency.
        :type currency: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_identifiers = None
        self._instrument_scope = None
        self._instrument_uid = None
        self._sub_holding_keys = None
        self._properties = None
        self._tax_lots = None
        self._currency = None
        self.discriminator = None

        self.instrument_identifiers = instrument_identifiers
        self.instrument_scope = instrument_scope
        self.instrument_uid = instrument_uid
        self.sub_holding_keys = sub_holding_keys
        self.properties = properties
        self.tax_lots = tax_lots
        self.currency = currency

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this HoldingAdjustment.  # noqa: E501

        A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.  # noqa: E501

        :return: The instrument_identifiers of this HoldingAdjustment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this HoldingAdjustment.

        A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this HoldingAdjustment.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """

        self._instrument_identifiers = instrument_identifiers

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this HoldingAdjustment.  # noqa: E501

        The scope of the instrument that the holding adjustment is in.  # noqa: E501

        :return: The instrument_scope of this HoldingAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this HoldingAdjustment.

        The scope of the instrument that the holding adjustment is in.  # noqa: E501

        :param instrument_scope: The instrument_scope of this HoldingAdjustment.  # noqa: E501
        :type instrument_scope: str
        """

        self._instrument_scope = instrument_scope

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this HoldingAdjustment.  # noqa: E501

        The unqiue Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in.  # noqa: E501

        :return: The instrument_uid of this HoldingAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this HoldingAdjustment.

        The unqiue Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in.  # noqa: E501

        :param instrument_uid: The instrument_uid of this HoldingAdjustment.  # noqa: E501
        :type instrument_uid: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_uid is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_uid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_uid is not None and len(instrument_uid) < 1):
            raise ValueError("Invalid value for `instrument_uid`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_uid = instrument_uid

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this HoldingAdjustment.  # noqa: E501

        The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the 'Transaction' domain.  # noqa: E501

        :return: The sub_holding_keys of this HoldingAdjustment.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this HoldingAdjustment.

        The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the 'Transaction' domain.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this HoldingAdjustment.  # noqa: E501
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def properties(self):
        """Gets the properties of this HoldingAdjustment.  # noqa: E501

        The set of unique holding properties and associated values stored with the target holding. Each property will be from the 'Holding' domain.  # noqa: E501

        :return: The properties of this HoldingAdjustment.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this HoldingAdjustment.

        The set of unique holding properties and associated values stored with the target holding. Each property will be from the 'Holding' domain.  # noqa: E501

        :param properties: The properties of this HoldingAdjustment.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def tax_lots(self):
        """Gets the tax_lots of this HoldingAdjustment.  # noqa: E501

        The tax-lots that together make up the target holding.  # noqa: E501

        :return: The tax_lots of this HoldingAdjustment.  # noqa: E501
        :rtype: list[lusid.TargetTaxLot]
        """
        return self._tax_lots

    @tax_lots.setter
    def tax_lots(self, tax_lots):
        """Sets the tax_lots of this HoldingAdjustment.

        The tax-lots that together make up the target holding.  # noqa: E501

        :param tax_lots: The tax_lots of this HoldingAdjustment.  # noqa: E501
        :type tax_lots: list[lusid.TargetTaxLot]
        """
        if self.local_vars_configuration.client_side_validation and tax_lots is None:  # noqa: E501
            raise ValueError("Invalid value for `tax_lots`, must not be `None`")  # noqa: E501

        self._tax_lots = tax_lots

    @property
    def currency(self):
        """Gets the currency of this HoldingAdjustment.  # noqa: E501

        The Holding currency.  # noqa: E501

        :return: The currency of this HoldingAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this HoldingAdjustment.

        The Holding currency.  # noqa: E501

        :param currency: The currency of this HoldingAdjustment.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

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
        if not isinstance(other, HoldingAdjustment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HoldingAdjustment):
            return True

        return self.to_dict() != other.to_dict()
