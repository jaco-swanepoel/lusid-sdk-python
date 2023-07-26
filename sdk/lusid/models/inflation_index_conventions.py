# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.383
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


class InflationIndexConventions(object):
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
        'inflation_index_name': 'str',
        'currency': 'str',
        'observation_lag': 'str',
        'inflation_interpolation': 'str',
        'inflation_frequency': 'str',
        'inflation_roll_day': 'int'
    }

    attribute_map = {
        'inflation_index_name': 'inflationIndexName',
        'currency': 'currency',
        'observation_lag': 'observationLag',
        'inflation_interpolation': 'inflationInterpolation',
        'inflation_frequency': 'inflationFrequency',
        'inflation_roll_day': 'inflationRollDay'
    }

    required_map = {
        'inflation_index_name': 'required',
        'currency': 'required',
        'observation_lag': 'required',
        'inflation_interpolation': 'optional',
        'inflation_frequency': 'optional',
        'inflation_roll_day': 'optional'
    }

    def __init__(self, inflation_index_name=None, currency=None, observation_lag=None, inflation_interpolation=None, inflation_frequency=None, inflation_roll_day=None, local_vars_configuration=None):  # noqa: E501
        """InflationIndexConventions - a model defined in OpenAPI"
        
        :param inflation_index_name:  Name of the index, e.g. UKRPI. (required)
        :type inflation_index_name: str
        :param currency:  Currency of the inflation index convention. (required)
        :type currency: str
        :param observation_lag:  Observation lag. This is a string that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds and swaps have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid. (required)
        :type observation_lag: str
        :param inflation_interpolation:  Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat].
        :type inflation_interpolation: str
        :param inflation_frequency:  Frequency of inflation updated. Optional and defaults to Monthly which is the most common.  However both Australian and New Zealand inflation is published Quarterly. Only tenors of 1M or 3M are supported.
        :type inflation_frequency: str
        :param inflation_roll_day:  Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th).
        :type inflation_roll_day: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._inflation_index_name = None
        self._currency = None
        self._observation_lag = None
        self._inflation_interpolation = None
        self._inflation_frequency = None
        self._inflation_roll_day = None
        self.discriminator = None

        self.inflation_index_name = inflation_index_name
        self.currency = currency
        self.observation_lag = observation_lag
        self.inflation_interpolation = inflation_interpolation
        self.inflation_frequency = inflation_frequency
        if inflation_roll_day is not None:
            self.inflation_roll_day = inflation_roll_day

    @property
    def inflation_index_name(self):
        """Gets the inflation_index_name of this InflationIndexConventions.  # noqa: E501

        Name of the index, e.g. UKRPI.  # noqa: E501

        :return: The inflation_index_name of this InflationIndexConventions.  # noqa: E501
        :rtype: str
        """
        return self._inflation_index_name

    @inflation_index_name.setter
    def inflation_index_name(self, inflation_index_name):
        """Sets the inflation_index_name of this InflationIndexConventions.

        Name of the index, e.g. UKRPI.  # noqa: E501

        :param inflation_index_name: The inflation_index_name of this InflationIndexConventions.  # noqa: E501
        :type inflation_index_name: str
        """
        if self.local_vars_configuration.client_side_validation and inflation_index_name is None:  # noqa: E501
            raise ValueError("Invalid value for `inflation_index_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inflation_index_name is not None and len(inflation_index_name) > 50):
            raise ValueError("Invalid value for `inflation_index_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inflation_index_name is not None and len(inflation_index_name) < 0):
            raise ValueError("Invalid value for `inflation_index_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._inflation_index_name = inflation_index_name

    @property
    def currency(self):
        """Gets the currency of this InflationIndexConventions.  # noqa: E501

        Currency of the inflation index convention.  # noqa: E501

        :return: The currency of this InflationIndexConventions.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InflationIndexConventions.

        Currency of the inflation index convention.  # noqa: E501

        :param currency: The currency of this InflationIndexConventions.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def observation_lag(self):
        """Gets the observation_lag of this InflationIndexConventions.  # noqa: E501

        Observation lag. This is a string that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds and swaps have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid.  # noqa: E501

        :return: The observation_lag of this InflationIndexConventions.  # noqa: E501
        :rtype: str
        """
        return self._observation_lag

    @observation_lag.setter
    def observation_lag(self, observation_lag):
        """Sets the observation_lag of this InflationIndexConventions.

        Observation lag. This is a string that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds and swaps have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid.  # noqa: E501

        :param observation_lag: The observation_lag of this InflationIndexConventions.  # noqa: E501
        :type observation_lag: str
        """
        if self.local_vars_configuration.client_side_validation and observation_lag is None:  # noqa: E501
            raise ValueError("Invalid value for `observation_lag`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                observation_lag is not None and len(observation_lag) > 32):
            raise ValueError("Invalid value for `observation_lag`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                observation_lag is not None and len(observation_lag) < 0):
            raise ValueError("Invalid value for `observation_lag`, length must be greater than or equal to `0`")  # noqa: E501

        self._observation_lag = observation_lag

    @property
    def inflation_interpolation(self):
        """Gets the inflation_interpolation of this InflationIndexConventions.  # noqa: E501

        Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat].  # noqa: E501

        :return: The inflation_interpolation of this InflationIndexConventions.  # noqa: E501
        :rtype: str
        """
        return self._inflation_interpolation

    @inflation_interpolation.setter
    def inflation_interpolation(self, inflation_interpolation):
        """Sets the inflation_interpolation of this InflationIndexConventions.

        Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat].  # noqa: E501

        :param inflation_interpolation: The inflation_interpolation of this InflationIndexConventions.  # noqa: E501
        :type inflation_interpolation: str
        """
        if (self.local_vars_configuration.client_side_validation and
                inflation_interpolation is not None and len(inflation_interpolation) > 32):
            raise ValueError("Invalid value for `inflation_interpolation`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inflation_interpolation is not None and len(inflation_interpolation) < 0):
            raise ValueError("Invalid value for `inflation_interpolation`, length must be greater than or equal to `0`")  # noqa: E501

        self._inflation_interpolation = inflation_interpolation

    @property
    def inflation_frequency(self):
        """Gets the inflation_frequency of this InflationIndexConventions.  # noqa: E501

        Frequency of inflation updated. Optional and defaults to Monthly which is the most common.  However both Australian and New Zealand inflation is published Quarterly. Only tenors of 1M or 3M are supported.  # noqa: E501

        :return: The inflation_frequency of this InflationIndexConventions.  # noqa: E501
        :rtype: str
        """
        return self._inflation_frequency

    @inflation_frequency.setter
    def inflation_frequency(self, inflation_frequency):
        """Sets the inflation_frequency of this InflationIndexConventions.

        Frequency of inflation updated. Optional and defaults to Monthly which is the most common.  However both Australian and New Zealand inflation is published Quarterly. Only tenors of 1M or 3M are supported.  # noqa: E501

        :param inflation_frequency: The inflation_frequency of this InflationIndexConventions.  # noqa: E501
        :type inflation_frequency: str
        """
        if (self.local_vars_configuration.client_side_validation and
                inflation_frequency is not None and len(inflation_frequency) > 32):
            raise ValueError("Invalid value for `inflation_frequency`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inflation_frequency is not None and len(inflation_frequency) < 0):
            raise ValueError("Invalid value for `inflation_frequency`, length must be greater than or equal to `0`")  # noqa: E501

        self._inflation_frequency = inflation_frequency

    @property
    def inflation_roll_day(self):
        """Gets the inflation_roll_day of this InflationIndexConventions.  # noqa: E501

        Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th).  # noqa: E501

        :return: The inflation_roll_day of this InflationIndexConventions.  # noqa: E501
        :rtype: int
        """
        return self._inflation_roll_day

    @inflation_roll_day.setter
    def inflation_roll_day(self, inflation_roll_day):
        """Sets the inflation_roll_day of this InflationIndexConventions.

        Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th).  # noqa: E501

        :param inflation_roll_day: The inflation_roll_day of this InflationIndexConventions.  # noqa: E501
        :type inflation_roll_day: int
        """

        self._inflation_roll_day = inflation_roll_day

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
        if not isinstance(other, InflationIndexConventions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InflationIndexConventions):
            return True

        return self.to_dict() != other.to_dict()
