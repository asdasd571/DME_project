# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestIndividualDataOfferController(BaseTestCase):
    """IndividualDataOfferController integration test stubs"""

    def test_offers_data_offer_id_delete(self):
        """Test case for offers_data_offer_id_delete

        
        """
        response = self.client.open(
            '/offers/{dataOfferId}'.format(data_offer_id='data_offer_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
