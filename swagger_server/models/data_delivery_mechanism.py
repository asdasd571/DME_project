# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.kafka_delivery_configuration import KafkaDeliveryConfiguration  # noqa: F401,E501
from swagger_server import util


class DataDeliveryMechanism(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_delivery_method: object=None, kafka_delivery_configuration: KafkaDeliveryConfiguration=None):  # noqa: E501
        """DataDeliveryMechanism - a model defined in Swagger

        :param data_delivery_method: The data_delivery_method of this DataDeliveryMechanism.  # noqa: E501
        :type data_delivery_method: object
        :param kafka_delivery_configuration: The kafka_delivery_configuration of this DataDeliveryMechanism.  # noqa: E501
        :type kafka_delivery_configuration: KafkaDeliveryConfiguration
        """
        self.swagger_types = {
            'data_delivery_method': object,
            'kafka_delivery_configuration': KafkaDeliveryConfiguration
        }

        self.attribute_map = {
            'data_delivery_method': 'dataDeliveryMethod',
            'kafka_delivery_configuration': 'kafkaDeliveryConfiguration'
        }
        self._data_delivery_method = data_delivery_method
        self._kafka_delivery_configuration = kafka_delivery_configuration

    @classmethod
    def from_dict(cls, dikt) -> 'DataDeliveryMechanism':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataDeliveryMechanism of this DataDeliveryMechanism.  # noqa: E501
        :rtype: DataDeliveryMechanism
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_delivery_method(self) -> object:
        """Gets the data_delivery_method of this DataDeliveryMechanism.

        Delivery Method supported  # noqa: E501

        :return: The data_delivery_method of this DataDeliveryMechanism.
        :rtype: object
        """
        return self._data_delivery_method

    @data_delivery_method.setter
    def data_delivery_method(self, data_delivery_method: object):
        """Sets the data_delivery_method of this DataDeliveryMechanism.

        Delivery Method supported  # noqa: E501

        :param data_delivery_method: The data_delivery_method of this DataDeliveryMechanism.
        :type data_delivery_method: object
        """
        if data_delivery_method is None:
            raise ValueError("Invalid value for `data_delivery_method`, must not be `None`")  # noqa: E501

        self._data_delivery_method = data_delivery_method

    @property
    def kafka_delivery_configuration(self) -> KafkaDeliveryConfiguration:
        """Gets the kafka_delivery_configuration of this DataDeliveryMechanism.


        :return: The kafka_delivery_configuration of this DataDeliveryMechanism.
        :rtype: KafkaDeliveryConfiguration
        """
        return self._kafka_delivery_configuration

    @kafka_delivery_configuration.setter
    def kafka_delivery_configuration(self, kafka_delivery_configuration: KafkaDeliveryConfiguration):
        """Sets the kafka_delivery_configuration of this DataDeliveryMechanism.


        :param kafka_delivery_configuration: The kafka_delivery_configuration of this DataDeliveryMechanism.
        :type kafka_delivery_configuration: KafkaDeliveryConfiguration
        """

        self._kafka_delivery_configuration = kafka_delivery_configuration
