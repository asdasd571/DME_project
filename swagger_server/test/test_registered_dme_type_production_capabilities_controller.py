# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRegisteredDMETypeProductionCapabilitiesController(BaseTestCase):
    """RegisteredDMETypeProductionCapabilitiesController integration test stubs"""

    def test_production_capabilities_post(self):
        """Test case for production_capabilities_post

        
        """
        body = DmeTypeRelatedCapabilities()
        response = self.client.open(
            '/production-capabilities',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
