import connexion
import six
import json
from flask import jsonify, request
from swagger_server.models import DataOfferInfo  # noqa: E501
from swagger_server import util

data_offers = {} 

def offers_post(body):  # noqa: E501
    """Create an individual data offer"""
    apiConsumerId = request.args.get('apiConsumerId')
    if body is None:
        return jsonify({"error": "Request body is required"}), 400

    try:
        # JSON 변환 (bytes일 경우 처리)
        if isinstance(body, bytes):
            body = json.loads(body.decode('utf-8'))

        if not isinstance(body, dict):
            return jsonify({"error": "Invalid input, JSON object required"}), 400

        # 필수 필드 확인
        required_fields = ["dataOfferId"]
        for field in required_fields:
            if field not in body:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        data_offer_id = body["dataOfferId"]
        data_offer_info = DataOfferInfo.from_dict(body)

        # 저장
        data_offers[data_offer_id] = data_offer_info

        # 리소스 URI 생성
        location_uri = f"/data-offer/v1/{apiConsumerId}/offers/{data_offer_id}"

        # 응답에 dataOfferId 포함
        response_data = data_offer_info.to_dict()
        response_data["dataOfferId"] = data_offer_id  # dataOfferId를 응답에 추가

        response = jsonify(response_data)
        response.status_code = 201
        response.headers['Location'] = location_uri
        return response

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except AttributeError as e:
        return jsonify({"error": f"Unexpected data structure: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500
