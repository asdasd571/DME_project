import connexion
import six

from swagger_server.models.dme_type_id import DmeTypeId  # noqa: E501
from swagger_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server import util

from flask import jsonify
from ..models import DmeTypeId, DmeTypeRelatedCapabilities, ProblemDetails  # 모델을 임포트 (가정)

# DME 타입 ID를 조회하는 함수
def dme_types_dme_type_id_get(dme_type_id):  # noqa: E501
    """dme_types_dme_type_id_get

    To obtain information about an individual DME type. # noqa: E501

    :param dme_type_id: DME 타입을 식별하는 ID
    :type dme_type_id: dict | bytes
    :rtype: ProblemDetails
    """
    # 요청이 JSON이라면 JSON을 파싱하여 DmeTypeId 객체로 변환
    if connexion.request.is_json:
        dme_type_id = DmeTypeId.from_dict(connexion.request.get_json())  # noqa: E501

    # 여기서 실제 데이터베이스나 서비스와 연동하여 DME 타입 정보를 가져오기
    # 더미 데이터
    if dme_type_id:
        response = {
            'dmeTypeId': {
                'namespace': 'example_namespace',
                'name': 'example_name',
                'version': '1.0.0'
            },
            'metadata': {
                'rat': ['5G'],
                'dataCategory': ['PM counters']
            },
            'dataDeliveryMechanisms': [{
                'dataDeliveryMethod': 'KAFKA',
                'kafkaDeliveryConfiguration': {
                    'retentionMs': 10000,
                    'compressionType': 'GZIP'
                }
            }]
        }
        return jsonify(response)  # 실제로는 반환할 데이터를 JSON 형식으로 반환
    else:
        # 유효하지 않은 DME 타입 ID에 대해 문제 세부 사항 반환
        problem_details = ProblemDetails(type="https://example.com/problem-type", title="Invalid DME Type ID", status=400)
        return jsonify(problem_details.to_dict()), 400


# DME 타입 목록을 조회하는 함수
def dme_types_get(identity_namespace=None, identity_name=None, data_category=None):  # noqa: E501
    """dme_types_get

    To discover the available DME types # noqa: E501

    :param identity_namespace: Identity namespace to match the “namespace“ part of the “dmeTypeId“ attribute
    :type identity_namespace: str
    :param identity_name: Identity name to match the “name“ part of the “dmeTypeId“ attribute.
    :type identity_name: str
    :param data_category: Set of data category entries, all of which to match entries of the “dataCategory“ attribute.
    :type data_category: List[str]
    :rtype: List[DmeTypeRelatedCapabilities]
    """
    # 여기서 실제로 데이터베이스나 서비스에서 DME 타입 목록을 가져옴
    # 예시로 더미 데이터를 반환합니다.
    dme_types = [
        DmeTypeRelatedCapabilities(
            registrationId="1234",
            dmeTypeDefinition=DmeTypeId(namespace="example_namespace", name="example_name", version="1.0.0"),
            dataAccessEndpoint="http://example.com/api",
            dataDeliveryModes=["ONE_TIME", "CONTINUOUS"]
        ),
        DmeTypeRelatedCapabilities(
            registrationId="5678",
            dmeTypeDefinition=DmeTypeId(namespace="example_namespace2", name="example_name2", version="1.0.1"),
            dataAccessEndpoint="http://example2.com/api",
            dataDeliveryModes=["ONE_TIME"]
        )
    ]
    
    # 필터링 기능을 추가하여 검색을 수행할 수 있습니다.
    if identity_namespace:
        dme_types = [dme_type for dme_type in dme_types if dme_type.dmeTypeDefinition.namespace == identity_namespace]
    if identity_name:
        dme_types = [dme_type for dme_type in dme_types if dme_type.dmeTypeDefinition.name == identity_name]
    if data_category:
        dme_types = [dme_type for dme_type in dme_types if all(category in dme_type.metadata.dataCategory for category in data_category)]

    # 필터링 후 결과 반환
    return jsonify([dme_type.to_dict() for dme_type in dme_types])  # 결과를 JSON 형태로 반환
