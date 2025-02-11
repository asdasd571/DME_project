# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_job_id import DataJobId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIndividualDataJobController(BaseTestCase):
    """IndividualDataJobController integration test stubs"""

    def test_data_jobs_data_job_id_delete(self):
        """Test case for data_jobs_data_job_id_delete

        
        """
        response = self.client.open(
            '/data-jobs/{dataJobId}'.format(data_job_id=DataJobId()),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
