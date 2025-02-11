# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dme_type_id import DmeTypeId  # noqa: E501
from swagger_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_dme_types_dme_type_id_get(self):
        """Test case for dme_types_dme_type_id_get

        
        """
        response = self.client.open(
            '/dme-types/{dmeTypeId}'.format(dme_type_id=DmeTypeId()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dme_types_get(self):
        """Test case for dme_types_get

        
        """
        query_string = [('identity_namespace', 'identity_namespace_example'),
                        ('identity_name', 'identity_name_example'),
                        ('data_category', 'data_category_example')]
        response = self.client.open(
            '/dme-types',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
