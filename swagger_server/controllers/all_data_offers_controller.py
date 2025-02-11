import connexion
import six

from swagger_server.models.data_offer_info import DataOfferInfo  # noqa: E501
from swagger_server import util


def offers_post(body):  # noqa: E501
    """offers_post

    Allows to create a new data offer # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataOfferInfo
    """
    if connexion.request.is_json:
        body = DataOfferInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
