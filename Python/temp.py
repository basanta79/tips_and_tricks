import json
import time
from enum import unique
from ledgecore.model.ledgemodel import LedgeModel, ModelDataType, ConversionType
from ledgecore.types.ttypes import TIntEnum
from ledgecore.model import basemodel
class NotificationSpec(basemodel.Model):
    table_name = 'notification_spec'
    fields = {
        'notification_spec_id': basemodel.DataType.INTEGER,
        'notification_type': basemodel.DataType.INTEGER,
        'team_id': basemodel.DataType.INTEGER,
        'project_id': basemodel.DataType.INTEGER,
        'language': basemodel.DataType.INTEGER,
        'delivery_type': basemodel.DataType.INTEGER,
        'template_name': basemodel.DataType.STRING,
        'create_time': basemodel.DataType.INTEGER,
        'active': basemodel.DataType.BOOLEAN
    }
    AUTO_INCREMENT = 'notification_spec_id'
    PRIMARY_KEY = ['notification_spec_id']
    def __init__(self, storage_driver, notification_spec_id=None):
        super().__init__(storage_driver=storage_driver)
        if notification_spec_id is not None:
            self.set_primary_key(key='notification_spec_id', value=notification_spec_id)
    def create(self, notification_type, project_id, language, delivery_type, template_name):
        self.put(puts=dict(notification_type=notification_type, project_id=project_id, language=language,
                           delivery_type=delivery_type, template_name=template_name, create_time=int(time.time())))
@unique
class NotificationStatus(TIntEnum):
    PENDING = 1
    SENT = 2
    ERROR = 3
class Notification(LedgeModel):
    table_name = 'notification'
    fields = {
        'notification_id': ModelDataType.INTEGER,
        'notification_spec_id': ModelDataType.INTEGER,
        'destination': ModelDataType.STRING,
        'status': ModelDataType.INTEGER,
        'error_message': ModelDataType.STRING,
        'create_time': ModelDataType.INTEGER,
        'notification_data_persisted': ModelDataType.OBJECT,
        'active': ModelDataType.BOOLEAN,
        'created': ModelDataType.INTEGER,
        'updated': ModelDataType.INTEGER,
        'sent_at': ModelDataType.INTEGER,
        'asynchronous': ModelDataType.BOOLEAN
    }
    AUTO_INCREMENT = 'notification_id'
    PRIMARY_KEY = ['notification_id']
    def __init__(self, is_creation, notification_id=None, notification_spec_id=None, destination=None,
                 status=None, error_message=None, create_time=None, notification_data=None, sent_at=None, 
                 asynchronous=False):
        super().__init__(is_creation=is_creation)
        if notification_id is not None:
            self._set_primary_key(key='notification_id', value=notification_id)
        if is_creation:
            self.notification_spec_id = notification_spec_id
            self.destination = destination
            self.status = status
            self.error_message = error_message
            self.create_time = create_time
            self.notification_data = notification_data
            self.sent_at = sent_at
            self.asynchronous = asynchronous
            if not asynchronous:
                self.notification_data_persisted = notification_data
            else:
                self.notification_data_persisted = None
    @staticmethod
    def _parse_object(attr_name, attr_value, conversion_type):
        if attr_name != 'notification_data':
            raise NotImplementedError
        if attr_value is None:
            return None
        if conversion_type == ConversionType.FROM_DB_TO_MODEL:
            attr_value = json.loads(attr_value)
        elif conversion_type == ConversionType.FROM_MODEL_TO_DB:
            attr_value = json.dumps(attr_value)
        return attr_value
    @staticmethod
    def create(notification_id, notification_spec_id, notification_data, destination, status, asynchronous):
        return Notification(is_creation=True,
                            notification_id=notification_id,
                            notification_spec_id=notification_spec_id,
                            notification_data=notification_data,
                            destination=destination,
                            status=status,
                            error_message=None,
                            create_time=int(time.time()),
                            sent_at=None,
                            asynchronous=asynchronous)
    @staticmethod
    def retrieve(storage_driver, notification_id):
        instance = Notification(is_creation=False,
                                notification_id=notification_id)
        if instance.load(storage_driver=storage_driver):
            return instance
        else:
            return None
        
        if self.notification_data_persisted is not None:
            self.notification_data = self.notification_data_persisted