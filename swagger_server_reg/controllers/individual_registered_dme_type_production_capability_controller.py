import connexion
import six

#임시 저장소
from .registered_dme_type_production_capabilities_controller import capabilities_db


from swagger_server_reg.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server_reg.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server_reg.models.registration_id import RegistrationId  # noqa: E501
from swagger_server_reg import util

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


def update_production_capabilities_by_id(registration_id, body):
    """등록된 registration_id로 생산 능력 데이터를 업데이트"""
    
    # capabilities_db에서 registration_id로 기존 데이터 조회
    if registration_id not in capabilities_db:
        return None  # 데이터가 없으면 None 반환
    
    existing_data = capabilities_db[registration_id]
    
    # 기존 데이터를 업데이트
    existing_data.update(body)  # 기존 데이터에 새 데이터를 덮어씀
    
    # 업데이트된 데이터를 다시 저장
    capabilities_db[registration_id] = existing_data
    
    return existing_data


def production_capabilities_registration_id_put(registration_id, body):  # noqa: E501
    """production_capabilities_registration_id_put

    To update DME type production capabilities that it has previously registered

    :param registration_id: 
    :type registration_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: dict
    """
    try:
        # 실제 업데이트 작업 수행
        updated = update_production_capabilities_by_id(registration_id, body)
        if updated:
            return updated, 200
        else:
            return {"error": "Not found"}, 404
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}, 500


