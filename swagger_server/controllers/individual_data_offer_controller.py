import connexion
import json
from flask import request, jsonify
from swagger_server.controllers.all_data_offers_controller import data_offers
# 전역 변수 data_offers 정의

def offers_data_offer_id_delete(data_offer_id):
    """Delete a specific data offer based on offer ID"""
    # data_offers에서 data_offer_id로 오퍼 찾기
    if data_offer_id not in data_offers:
        # 데이터 오퍼가 존재하지 않으면 404 반환
        return jsonify({
            "type": "https://example.com/probs/data-offer-not-found",
            "title": "Data Offer Not Found",
            "status": 404,
            "detail": f"Data offer {data_offer_id} not found."
        }), 404

    # 해당 오퍼 삭제
    del data_offers[data_offer_id]

    # 204 No Content 반환
    return '', 204
