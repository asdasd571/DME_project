import connexion
import six

#임시 저장소
from .registered_dme_type_production_capabilities_controller import capabilities_db


from swagger_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.registration_id import RegistrationId  # noqa: E501
from swagger_server import util

def delete_production_capabilities_by_id(registration_id):
    """등록된 registration_id로 생산 능력 데이터를 삭제"""
    if registration_id in capabilities_db:
        del capabilities_db[registration_id]  # 해당 ID의 데이터를 삭제
        return True
    return False

def production_capabilities_registration_id_delete(registration_id):  # noqa: E501
    """production_capabilities_registration_id_delete

    To deregister DME type production capabilities

    :param registration_id: 
    :type registration_id: str

    :rtype: None
    """
    #  if connexion.request.is_json:
    #     registration_id = RegistrationId.from_dict(connexion.request.get_json())  # noqa: E501
    ############################# -> dict로 보내면 오류 남 not hashable
    try:
        # 실제 삭제 작업 수행
        deleted = delete_production_capabilities_by_id(registration_id)
        if deleted:
            return {"message": "Production capabilities deleted successfully"}, 200
        else:
            return {"error": "Not found"}, 404
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}, 500




def get_production_capabilities_by_id(registration_id):
    """등록된 registration_id로 생산 능력 데이터를 조회"""
    # capabilities_db에서 registration_id로 데이터를 조회
    return capabilities_db.get(registration_id)

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
            # DmeTypeRelatedCapabilities 객체로 변환 후 반환
            return production_capability, 200
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

