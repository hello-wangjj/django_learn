from django.db import models
from mongoengine import *
import pymongo
# Create your models here.
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
item_info2_1 = ganji['item_info2_1']
connect('ganji', host='127.0.0.1', port=27017)


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


pipeline = [
    {'$sort': {'pub_date': -1}},
    {'$limit': 1}
]
item_info = item_info2_1.aggregate(pipeline)
last_pub_date = []
for i in item_info:
    last_pub_date.append(i['pub_date'])

# for i in ItemInfo._get_collection().aggregate(pipeline):
#     print(i)



