import connexion
import six

from swagger_server.models.data_job_id import DataJobId  # noqa: E501
from swagger_server import util


def data_jobs_data_job_id_delete(data_job_id):  # noqa: E501
    """data_jobs_data_job_id_delete

    To delete the created data job # noqa: E501

    :param data_job_id: 
    :type data_job_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_job_id = DataJobId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
