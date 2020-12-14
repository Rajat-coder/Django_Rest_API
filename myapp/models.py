from django.db import models

# Create your models here.

class User(models.Model):
    Employee_id=models.CharField(max_length=10,unique=True)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Rank=models.FloatField()

    def upload_photo(self,filename):
        path='myapp/photo1/{}'.format(filename)
        return path
    Photo=models.ImageField(upload_to=upload_photo,null=True,blank=True)

    def upload_file(self,filename):
        path='myapp/file1/{}'.format(filename)
        return path
    Resume=models.ImageField(upload_to=upload_file,null=True,blank=True)

    def __str__(self):
        return f"{self.Employee_id} - {self.Name}"




