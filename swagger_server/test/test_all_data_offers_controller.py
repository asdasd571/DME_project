# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_offer_info import DataOfferInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAllDataOffersController(BaseTestCase):
    """AllDataOffersController integration test stubs"""

    def test_offers_post(self):
        """Test case for offers_post

        
        """
        body = DataOfferInfo()
        response = self.client.open(
            '/offers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
