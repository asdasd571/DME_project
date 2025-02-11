import connexion
import six

from swagger_server.models import DataOfferInfo  # noqa: E501
from swagger_server import util


import json
from flask import jsonify

def offers_post(body):  # noqa: E501
    """offers_post

    Allows to create a new data offer

    :param body: 
    :type body: dict | bytes

    :rtype: DataOfferInfo
    """
    if isinstance(body, dict):  # body가 dict 타입일 경우
        try:
            data_offer_info = DataOfferInfo.from_dict(body)
            return jsonify(data_offer_info.to_dict()), 201
        except KeyError as e:
            return jsonify({"error": f"Missing key: {str(e)}"}), 400
    elif isinstance(body, bytes):  # body가 bytes일 경우
        try:
            body = json.loads(body.decode('utf-8'))  # JSON 디코딩
            data_offer_info = DataOfferInfo.from_dict(body)
            return jsonify(data_offer_info.to_dict()), 201
        except (json.JSONDecodeError, KeyError) as e:
            return jsonify({"error": f"Invalid or missing data: {str(e)}"}), 400
    else:
        return jsonify({"error": "Invalid input, JSON required."}), 400

