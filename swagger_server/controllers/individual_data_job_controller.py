import connexion
from swagger_server import util
from flask import jsonify
from swagger_server.models import DataJobId  # DataJobId 모델을 가져오는 가정
from .create_all_data_jobs_controller import data_job_db  # 데이터 작업을 저장하는 임시 데이터베이스

def delete_data_job_by_id(data_job_id):
    """등록된 registration_id로 생산 능력 데이터를 삭제"""
    if data_job_id in data_job_db:
        del data_job_db[data_job_id]  # 해당 ID의 데이터를 삭제
        return True
    return False

def data_jobs_data_job_id_delete(data_job_id):  # noqa: E501
    """data_jobs_data_job_id_delete

    To delete the created data job.

    :param data_job_id: The ID of the data job to delete.
    :type data_job_id: str

    :rtype: None
    """
    try:
        # 실제 삭제 작업 수행
        deleted = delete_data_job_by_id(data_job_id)
        if deleted:
            return {"message": "Data Job deleted successfully"}, 204
        else:
            return {"error": "Not found"}, 404
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}, 500

    # JSON 요청 본문을 DataJobId 객체로 변환
    data_job_ids = DataJobId.from_dict(connexion.request.get_json())  # JSON에서 ID를 추출하여 객체로 변환
    
    