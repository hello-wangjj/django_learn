from django.db import models
from mongoengine import *
# Create your models here.
# connect('ganji', host='127.0.0.1', port=27017)


class ArticleInfo(Document):
    desc = StringField()
    title = StringField()
    scores = StringField()
    tags = ListField(StringField())
    meta = {
        'collection': 'article_info'
    }
for i in ArticleInfo.objects:
    print(i)
    print(i.desc, i.title, i.scores, i.tags)
