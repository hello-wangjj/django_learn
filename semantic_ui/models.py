from django.db import models
from mongoengine import *
# Create your models here.


class ItemInfo(Document):
    pub_date = StringField()
    look = StringField()
    area = ListField(StringField())
    title = StringField()
    url = StringField()
    cates = ListField(StringField())
    price = FloatField()
    time = IntField()
    meta = {
        'collection': 'item_info2_1'
    }
