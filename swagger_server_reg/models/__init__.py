# coding: utf-8

# flake8: noqa
from __future__ import absolute_import
# import models into model package
from swagger_server_reg.models.data_delivery_mechanism import DataDeliveryMechanism
from swagger_server_reg.models.data_delivery_mode import DataDeliveryMode
from swagger_server_reg.models.delivery_schema import DeliverySchema
from swagger_server_reg.models.dme_type_definition import DmeTypeDefinition
from swagger_server_reg.models.dme_type_id_struct import DmeTypeIdStruct
from swagger_server_reg.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities
from swagger_server_reg.models.fqdn import Fqdn
from swagger_server_reg.models.interface_description import InterfaceDescription
from swagger_server_reg.models.ipv4_addr import Ipv4Addr
from swagger_server_reg.models.ipv6_addr import Ipv6Addr
from swagger_server_reg.models.kafka_delivery_configuration import KafkaDeliveryConfiguration
from swagger_server_reg.models.metadata import Metadata
from swagger_server_reg.models.o_auth_grant_type import OAuthGrantType
from swagger_server_reg.models.port import Port
from swagger_server_reg.models.problem_details import ProblemDetails
from swagger_server_reg.models.registration_id import RegistrationId
from swagger_server_reg.models.schema_types import SchemaTypes
from swagger_server_reg.models.security_method import SecurityMethod


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nakgeun:12345@db:5432/mydatabase'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 변경 추적 비활성화

# # Flask-SQLAlchemy 인스턴스를 생성하고 앱에 연결
# db = SQLAlchemy(app)

# # 마이그레이션 인스턴스 생성
# migrate = Migrate(app, db)

# # 마이그레이션 초기화 및 적용
# if __name__ == '__main__':
#     app.run()
