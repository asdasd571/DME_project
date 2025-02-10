import connexion
import six

from swagger_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.registration_id import RegistrationId  # noqa: E501
from swagger_server import util


def production_capabilities_registration_id_delete(registration_id):  # noqa: E501
    """production_capabilities_registration_id_delete

    To deregister DME type production capabilities # noqa: E501

    :param registration_id: 
    :type registration_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        registration_id = RegistrationId.from_dict(connexion.request.get_json())  # noqa: E501

    # 실제 삭제 로직 (예시로 데이터베이스에서 삭제하는 경우)
    try:
        # 데이터베이스에서 해당 registration_id로 삭제 작업 수행
        deleted = delete_production_capabilities_by_id(registration_id)
        if deleted:
            return {"message": "Production capabilities deleted successfully"}, 200
        else:
            return {"error": "Not found"}, 404
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}, 500

def production_capabilities_registration_id_get(registration_id):  # noqa: E501
    """production_capabilities_registration_id_get

    To query DME type production capabilities that it has previously registered

    :param registration_id: The ID used for querying production capabilities
    :type registration_id: str

    :rtype: DmeTypeRelatedCapabilities
    """
    try:
        # registration_id가 None 또는 잘못된 형식이면 오류 반환
        if not registration_id:
            return {"error": "Invalid registration_id"}, 400

        # 실제 조회 로직 실행
        production_capability = get_production_capabilities_by_id(registration_id)

        if production_capability:
            return production_capability.to_dict(), 200
        else:
            return {"error": "Not found"}, 404
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}, 500



def production_capabilities_registration_id_put(body, registration_id):  # noqa: E501
    """production_capabilities_registration_id_put

    To update DME type production capabilities that it has previously registered # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param registration_id: 
    :type registration_id: dict | bytes

    :rtype: DmeTypeRelatedCapabilities
    """
    if connexion.request.is_json:
        body = DmeTypeRelatedCapabilities.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        registration_id = RegistrationId.from_dict(connexion.request.get_json())  # noqa: E501

    # 실제 업데이트 로직 (예시로 데이터베이스에서 업데이트하는 경우)
    try:
        updated = update_production_capabilities_by_id(registration_id, body)
        if updated:
            return updated.to_dict(), 200
        else:
            return {"error": "Not found"}, 404
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}, 500

