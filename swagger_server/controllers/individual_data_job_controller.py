import connexion
import six

from swagger_server.models.data_job_id import DataJobId  # noqa: E501
from swagger_server import util

from flask import jsonify
from models import DataJobId  # DataJobId 모델을 가져오는 가정
from database import db  # 데이터베이스 관련 객체 (예시)

def data_jobs_data_job_id_delete(data_job_id):  # noqa: E501
    """data_jobs_data_job_id_delete

    To delete the created data job.

    :param data_job_id: The ID of the data job to delete.
    :type data_job_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # JSON 요청 본문을 DataJobId 객체로 변환
        data_job_id = DataJobId.from_dict(connexion.request.get_json())  # noqa: E501
        
        # 데이터 작업 삭제 로직 (예: 데이터베이스에서 해당 작업을 삭제)
        # db.delete_data_job(data_job_id)  # 실제 삭제 로직을 구현해야 함

        # 예시: 삭제가 성공적으로 이루어졌다면, 204 No Content 응답을 반환
        return '', 204  # HTTP 204 No Content 상태 코드 반환

    # JSON 형식이 아닐 경우 잘못된 요청 처리
    return jsonify({"error": "Invalid input, JSON expected"}), 400
