# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_job_info import DataJobInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCreateAllDataJobsController(BaseTestCase):
    """CreateAllDataJobsController integration test stubs"""

    def test_data_jobs_post(self):
        """Test case for data_jobs_post

        
        """
        body = DataJobInfo()
        response = self.client.open(
            '/data-jobs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
