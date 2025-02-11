# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DataJobInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_access_method: str=None, data_request: object=None, data_access_uri: str=None):  # noqa: E501
        """DataJobInfo - a model defined in Swagger

        :param data_access_method: The data_access_method of this DataJobInfo.  # noqa: E501
        :type data_access_method: str
        :param data_request: The data_request of this DataJobInfo.  # noqa: E501
        :type data_request: object
        :param data_access_uri: The data_access_uri of this DataJobInfo.  # noqa: E501
        :type data_access_uri: str
        """
        self.swagger_types = {
            'data_access_method': str,
            'data_request': object,
            'data_access_uri': str
        }

        self.attribute_map = {
            'data_access_method': 'dataAccessMethod',
            'data_request': 'dataRequest',
            'data_access_uri': 'dataAccessUri'
        }
        self._data_access_method = data_access_method
        self._data_request = data_request
        self._data_access_uri = data_access_uri

    @classmethod
    def from_dict(cls, dikt) -> 'DataJobInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataJobInfo of this DataJobInfo.  # noqa: E501
        :rtype: DataJobInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_access_method(self) -> str:
        """Gets the data_access_method of this DataJobInfo.

        Method used for data access  # noqa: E501

        :return: The data_access_method of this DataJobInfo.
        :rtype: str
        """
        return self._data_access_method

    @data_access_method.setter
    def data_access_method(self, data_access_method: str):
        """Sets the data_access_method of this DataJobInfo.

        Method used for data access  # noqa: E501

        :param data_access_method: The data_access_method of this DataJobInfo.
        :type data_access_method: str
        """

        self._data_access_method = data_access_method

    @property
    def data_request(self) -> object:
        """Gets the data_request of this DataJobInfo.

        Data requested  # noqa: E501

        :return: The data_request of this DataJobInfo.
        :rtype: object
        """
        return self._data_request

    @data_request.setter
    def data_request(self, data_request: object):
        """Sets the data_request of this DataJobInfo.

        Data requested  # noqa: E501

        :param data_request: The data_request of this DataJobInfo.
        :type data_request: object
        """

        self._data_request = data_request

    @property
    def data_access_uri(self) -> str:
        """Gets the data_access_uri of this DataJobInfo.

        URI to access the data  # noqa: E501

        :return: The data_access_uri of this DataJobInfo.
        :rtype: str
        """
        return self._data_access_uri

    @data_access_uri.setter
    def data_access_uri(self, data_access_uri: str):
        """Sets the data_access_uri of this DataJobInfo.

        URI to access the data  # noqa: E501

        :param data_access_uri: The data_access_uri of this DataJobInfo.
        :type data_access_uri: str
        """

        self._data_access_uri = data_access_uri
