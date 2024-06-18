from django.db import models

# Create your models here.

class BlogPost(models.Model):
    img=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=50)

    class Meta:
        db_table = 'post_table'
        managed = True
        verbose_name = 'Posts_table'
        verbose_name_plural = 'Posts_table'
