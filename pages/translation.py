from modeltranslation.translator import register, TranslationOptions
from pages import models


@register(models.AboutModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name','job','description',)