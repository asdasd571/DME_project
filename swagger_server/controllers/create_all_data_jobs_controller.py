import connexion
import uuid
from swagger_server import util
from flask import jsonify
from swagger_server.models import DataJobInfo  # DataJobInfo 모델을 가져오는 가정

data_job_db = {}

def data_jobs_post(body):  # noqa: E501
    """data_jobs_post

    To create a data job.

    :param body: The data job details provided in the request body.
    :type body: dict | bytes

    :rtype: dict
    """
    # JSON을 DataJobInfo 객체로 변환
    body = DataJobInfo.from_dict(connexion.request.get_json())  
    
    # 새로운 data_job_id 생성 (예: UUID 사용)
    data_job_id = str(uuid.uuid4())  # 고유한 ID 생성

    # body 객체에 data_job_id 추가
    body.data_job_id = data_job_id  # 객체에 ID 추가

    # 임시 저장소에 데이터 저장
    data_job_db[data_job_id] = body.to_dict()  # data_job_id를 키로 사용하여 저장

    # dataJobInfo와 data_job_id를 함께 반환
    return jsonify({
        "dataJobInfo": body.to_dict(),
        "data_job_id": data_job_id
    }), 201  # HTTP 201 Created 응답과 함께 반환
