from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

from products.models import ProductModel,ProductImageModel


@receiver(pre_save, sender=ProductModel)
def calculate_discount_price(sender, instance, **kwargs):
    if instance.discount:
        instance.discount_price = instance.price - (instance.price * instance.discount / 100)
    else:
        instance.discount_price = instance.price

@receiver(post_save, sender=ProductImageModel)
def check_minimum_images(sender, instance, **kwargs):
    image_count = instance.image.count()

    if image_count < 4:
        raise ValidationError("Har bir mahsulot kamida 4 ta rasmga ega bo‘lishi kerak!")