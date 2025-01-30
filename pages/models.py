from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class AboutModel(models.Model):
    name = models.CharField(max_length=128)
    job = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'

