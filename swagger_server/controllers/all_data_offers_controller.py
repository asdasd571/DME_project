import connexion
import six

from swagger_server.models import DataOfferInfo  # noqa: E501
from swagger_server import util


def offers_post(body):  # noqa: E501
    """offers_post

    Allows to create a new data offer

    :param body: 
    :type body: dict | bytes

    :rtype: DataOfferInfo
    """
    if isinstance(body, dict):  # body가 dict 타입일 경우
        # DataOfferInfo 객체 생성
        try:
            data_offer_info = DataOfferInfo.from_dict(body)
            # 데이터 처리 후 응답 반환
            return jsonify(data_offer_info.to_dict()), 201
        except KeyError as e:
            return jsonify({"error": f"Missing key: {str(e)}"}), 400
    else:
        return jsonify({"error": "Invalid input, JSON required."}), 400
