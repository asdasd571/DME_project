import connexion
import six

from swagger_server.models.data_job_info import DataJobInfo  # noqa: E501
from swagger_server import util


def data_jobs_post(body):  # noqa: E501
    """data_jobs_post

    To create a data job # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataJobInfo
    """
    if connexion.request.is_json:
        body = DataJobInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
