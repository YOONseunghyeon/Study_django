from django.db import models

# Create your models here.
class Products(models.Model) :
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=25)
    price = models.IntegerField()

    # 시험문제
    # class Products():
    #   name = models.CharField(primary_key = True)
    #    primary_key 작성 안할 시 자동으로 id가 들어감 (인덱스)

