from django.db import models

class stati(models.Model):
    title = models.CharField("Название", max_length= 30)
    content = models.TextField("Текст")
    def __str__(self):
        return self.title
        return self.content
    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural =  "Статьи"
# Create your models here.
