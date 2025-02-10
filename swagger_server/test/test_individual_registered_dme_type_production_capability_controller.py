# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.registration_id import RegistrationId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIndividualRegisteredDMETypeProductionCapabilityController(BaseTestCase):
    """IndividualRegisteredDMETypeProductionCapabilityController integration test stubs"""

    def test_production_capabilities_registration_id_delete(self):
        """Test case for production_capabilities_registration_id_delete

        
        """
        response = self.client.open(
            '/production-capabilities/{registrationId}'.format(registration_id=RegistrationId()),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_production_capabilities_registration_id_get(self):
        """Test case for production_capabilities_registration_id_get

        
        """
        response = self.client.open(
            '/production-capabilities/{registrationId}'.format(registration_id=RegistrationId()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_production_capabilities_registration_id_put(self):
        """Test case for production_capabilities_registration_id_put

        
        """
        body = DmeTypeRelatedCapabilities()
        response = self.client.open(
            '/production-capabilities/{registrationId}'.format(registration_id=RegistrationId()),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
