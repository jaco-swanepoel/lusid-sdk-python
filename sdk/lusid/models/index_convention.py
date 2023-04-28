# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.119
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


class IndexConvention(object):
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
        'fixing_reference': 'str',
        'publication_day_lag': 'int',
        'payment_tenor': 'str',
        'day_count_convention': 'str',
        'currency': 'str',
        'index_name': 'str',
        'scope': 'str',
        'code': 'str'
    }

    attribute_map = {
        'fixing_reference': 'fixingReference',
        'publication_day_lag': 'publicationDayLag',
        'payment_tenor': 'paymentTenor',
        'day_count_convention': 'dayCountConvention',
        'currency': 'currency',
        'index_name': 'indexName',
        'scope': 'scope',
        'code': 'code'
    }

    required_map = {
        'fixing_reference': 'required',
        'publication_day_lag': 'required',
        'payment_tenor': 'required',
        'day_count_convention': 'required',
        'currency': 'required',
        'index_name': 'optional',
        'scope': 'optional',
        'code': 'optional'
    }

    def __init__(self, fixing_reference=None, publication_day_lag=None, payment_tenor=None, day_count_convention=None, currency=None, index_name=None, scope=None, code=None, local_vars_configuration=None):  # noqa: E501
        """IndexConvention - a model defined in OpenAPI"
        
        :param fixing_reference:  The reference rate name for fixings. (required)
        :type fixing_reference: str
        :param publication_day_lag:  Number of days between spot and publication of the rate. (required)
        :type publication_day_lag: int
        :param payment_tenor:  The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year. (required)
        :type payment_tenor: str
        :param day_count_convention:  when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365]. (required)
        :type day_count_convention: str
        :param currency:  Currency of the index convention. (required)
        :type currency: str
        :param index_name:  The name of the index for which this represents the conventions of.  For instance, \"SOFR\", \"LIBOR\", \"EURIBOR\", etc.  Defaults to \"INDEX\" if not specified.
        :type index_name: str
        :param scope:  The scope used when updating or inserting the convention.
        :type scope: str
        :param code:  The code of the convention.
        :type code: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._fixing_reference = None
        self._publication_day_lag = None
        self._payment_tenor = None
        self._day_count_convention = None
        self._currency = None
        self._index_name = None
        self._scope = None
        self._code = None
        self.discriminator = None

        self.fixing_reference = fixing_reference
        self.publication_day_lag = publication_day_lag
        self.payment_tenor = payment_tenor
        self.day_count_convention = day_count_convention
        self.currency = currency
        self.index_name = index_name
        self.scope = scope
        self.code = code

    @property
    def fixing_reference(self):
        """Gets the fixing_reference of this IndexConvention.  # noqa: E501

        The reference rate name for fixings.  # noqa: E501

        :return: The fixing_reference of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._fixing_reference

    @fixing_reference.setter
    def fixing_reference(self, fixing_reference):
        """Sets the fixing_reference of this IndexConvention.

        The reference rate name for fixings.  # noqa: E501

        :param fixing_reference: The fixing_reference of this IndexConvention.  # noqa: E501
        :type fixing_reference: str
        """
        if self.local_vars_configuration.client_side_validation and fixing_reference is None:  # noqa: E501
            raise ValueError("Invalid value for `fixing_reference`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fixing_reference is not None and len(fixing_reference) > 64):
            raise ValueError("Invalid value for `fixing_reference`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fixing_reference is not None and len(fixing_reference) < 0):
            raise ValueError("Invalid value for `fixing_reference`, length must be greater than or equal to `0`")  # noqa: E501

        self._fixing_reference = fixing_reference

    @property
    def publication_day_lag(self):
        """Gets the publication_day_lag of this IndexConvention.  # noqa: E501

        Number of days between spot and publication of the rate.  # noqa: E501

        :return: The publication_day_lag of this IndexConvention.  # noqa: E501
        :rtype: int
        """
        return self._publication_day_lag

    @publication_day_lag.setter
    def publication_day_lag(self, publication_day_lag):
        """Sets the publication_day_lag of this IndexConvention.

        Number of days between spot and publication of the rate.  # noqa: E501

        :param publication_day_lag: The publication_day_lag of this IndexConvention.  # noqa: E501
        :type publication_day_lag: int
        """
        if self.local_vars_configuration.client_side_validation and publication_day_lag is None:  # noqa: E501
            raise ValueError("Invalid value for `publication_day_lag`, must not be `None`")  # noqa: E501

        self._publication_day_lag = publication_day_lag

    @property
    def payment_tenor(self):
        """Gets the payment_tenor of this IndexConvention.  # noqa: E501

        The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year.  # noqa: E501

        :return: The payment_tenor of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._payment_tenor

    @payment_tenor.setter
    def payment_tenor(self, payment_tenor):
        """Sets the payment_tenor of this IndexConvention.

        The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year.  # noqa: E501

        :param payment_tenor: The payment_tenor of this IndexConvention.  # noqa: E501
        :type payment_tenor: str
        """
        if self.local_vars_configuration.client_side_validation and payment_tenor is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_tenor`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                payment_tenor is not None and len(payment_tenor) > 32):
            raise ValueError("Invalid value for `payment_tenor`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                payment_tenor is not None and len(payment_tenor) < 0):
            raise ValueError("Invalid value for `payment_tenor`, length must be greater than or equal to `0`")  # noqa: E501

        self._payment_tenor = payment_tenor

    @property
    def day_count_convention(self):
        """Gets the day_count_convention of this IndexConvention.  # noqa: E501

        when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365].  # noqa: E501

        :return: The day_count_convention of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._day_count_convention

    @day_count_convention.setter
    def day_count_convention(self, day_count_convention):
        """Sets the day_count_convention of this IndexConvention.

        when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365].  # noqa: E501

        :param day_count_convention: The day_count_convention of this IndexConvention.  # noqa: E501
        :type day_count_convention: str
        """
        if self.local_vars_configuration.client_side_validation and day_count_convention is None:  # noqa: E501
            raise ValueError("Invalid value for `day_count_convention`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                day_count_convention is not None and len(day_count_convention) > 32):
            raise ValueError("Invalid value for `day_count_convention`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                day_count_convention is not None and len(day_count_convention) < 0):
            raise ValueError("Invalid value for `day_count_convention`, length must be greater than or equal to `0`")  # noqa: E501

        self._day_count_convention = day_count_convention

    @property
    def currency(self):
        """Gets the currency of this IndexConvention.  # noqa: E501

        Currency of the index convention.  # noqa: E501

        :return: The currency of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IndexConvention.

        Currency of the index convention.  # noqa: E501

        :param currency: The currency of this IndexConvention.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def index_name(self):
        """Gets the index_name of this IndexConvention.  # noqa: E501

        The name of the index for which this represents the conventions of.  For instance, \"SOFR\", \"LIBOR\", \"EURIBOR\", etc.  Defaults to \"INDEX\" if not specified.  # noqa: E501

        :return: The index_name of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this IndexConvention.

        The name of the index for which this represents the conventions of.  For instance, \"SOFR\", \"LIBOR\", \"EURIBOR\", etc.  Defaults to \"INDEX\" if not specified.  # noqa: E501

        :param index_name: The index_name of this IndexConvention.  # noqa: E501
        :type index_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                index_name is not None and len(index_name) > 16):
            raise ValueError("Invalid value for `index_name`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                index_name is not None and len(index_name) < 0):
            raise ValueError("Invalid value for `index_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._index_name = index_name

    @property
    def scope(self):
        """Gets the scope of this IndexConvention.  # noqa: E501

        The scope used when updating or inserting the convention.  # noqa: E501

        :return: The scope of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this IndexConvention.

        The scope used when updating or inserting the convention.  # noqa: E501

        :param scope: The scope of this IndexConvention.  # noqa: E501
        :type scope: str
        """
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) > 256):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this IndexConvention.  # noqa: E501

        The code of the convention.  # noqa: E501

        :return: The code of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this IndexConvention.

        The code of the convention.  # noqa: E501

        :param code: The code of this IndexConvention.  # noqa: E501
        :type code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 256):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, IndexConvention):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndexConvention):
            return True

        return self.to_dict() != other.to_dict()
