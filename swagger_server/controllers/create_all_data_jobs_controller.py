import connexion
import six

from swagger_server import util


from flask import jsonify
from swagger_server.models import DataJobInfo  # DataJobInfo 모델을 가져오는 가정

def data_jobs_post(body):  # noqa: E501
    """data_jobs_post

    To create a data job.

    :param body: The data job details provided in the request body.
    :type body: dict | bytes

    :rtype: DataJobInfo
    """
    if connexion.request.is_json:
        body = DataJobInfo.from_dict(connexion.request.get_json())  # JSON을 DataJobInfo 객체로 변환
        
        # 데이터 작업을 생성하는 로직 (여기서 실제 데이터 작업을 처리하고 저장해야 함)
        # 예: db.create_data_job(body) 또는 관련 로직 추가
        
        # 예시로 반환하는 DataJobInfo 객체를 JSON 형식으로 반환
        return jsonify(body.to_dict()), 201  # HTTP 201 Created 응답과 함께 DataJobInfo 반환

    # JSON 형식이 아닐 경우 잘못된 요청 처리
    return jsonify({"error": "Invalid input, JSON expected"}), 400
