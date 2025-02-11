import connexion
import six

from swagger_server import util


def offers_data_offer_id_delete(data_offer_id):
    """offers_data_offer_id_delete

    To delete the data offer

    :param data_offer_id: The identifier of the data offer to be deleted.
    :type data_offer_id: str

    :rtype: None
    """
    # 데이터 제공이 존재하는지 확인
    if data_offer_id in data_offers:
        # 데이터 제공 삭제
        del data_offers[data_offer_id]
        
        # 204 No Content 응답 코드와 함께 성공적으로 삭제됨
        return '', 204
    else:
        # 데이터 제공이 존재하지 않으면 404 Not Found 응답 코드 반환
        return jsonify({"error": "Data offer not found"}), 404
