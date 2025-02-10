import connexion
import six

from swagger_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server import util
import uuid

def production_capabilities_post(body):  # noqa: E501
    """production_capabilities_post

    DME 타입의 생산 능력을 등록하는 엔드포인트

    :param body: JSON 형식으로 전달된 생산 능력 데이터
    :type body: dict | bytes

    :rtype: dict (등록된 registration_id 반환)
    """
    if not connexion.request.is_json:
        return {'message': 'Invalid input, JSON expected.'}, 400

    # 클라이언트로부터 받은 JSON 데이터를 객체로 변환
    body = DmeTypeRelatedCapabilities.from_dict(connexion.request.get_json())  # noqa: E501

    # 새로운 registration_id 생성 (예: UUID 사용)
    registration_id = str(uuid.uuid4())  # 고유한 ID 생성

    # body 객체에 registration_id 추가 (DB 저장을 고려)
    body.registration_id = registration_id  # 객체에 ID 추가

    # DB 저장 (예시 코드)
    # db_session.add(body)
    # db_session.commit()

    # 등록된 ID와 함께 응답 반환
    return {
        "registration_id": registration_id,
        "message": "Production capability registered successfully"
    }, 201  # 201 Created
