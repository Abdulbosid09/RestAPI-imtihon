from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models her
class User(AbstractUser):
   pass


class Kurs(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
    

class Dars(models.Model):
    name = models.CharField(max_length=255)
    izoh = models.TextField()
    kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE,related_name="kurs_dars")
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    dars_videosi = models.FileField(upload_to='videos/', blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'MVB'])
    ])

    def __str__(self) :
        return self.name
    
class Izoh(models.Model):
    dars = models.ForeignKey(Dars, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    

    def __str__(self):
        return f'Comment by {self.author} on {self.dars}'

class LikeBosish(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dars_like = models.ForeignKey(Dars, on_delete=models.CASCADE)
    like_or_dislike = models.BooleanField()
    created_by = models.DateTimeField(auto_now_add=True)


    