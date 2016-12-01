from django.db import models
from mongoengine import *
# Create your models here.
# connect('ganji', host='127.0.0.1', port=27017)


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
for i in ItemInfo.objects[:10]:
    print(i)
    print(i.pub_date)
