from django.db import models

# Create your models here.
class Person(models.Model): 
    # model 필드 추가해줄때마다 migrate 작업을 해주어야 함
    # python manage.py makemigrations
    # python manage.py migrate
    name = models.CharField(max_length=20)
    birth = models.DateField(auto_now=False)
    age = models.IntegerField()
    department = models.CharField(max_length=20)
    fav = models.TextField(blank=True)

    # def __str__(self): #model 객체들의 이름으로 return을 하겠다.
    #     return self.name, self.age #object들의 이름이 data내의 name 변수 이름으로 바뀌어서 표출. ,를 통해 여러개 변수를 추가할 수 있음