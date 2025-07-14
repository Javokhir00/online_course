from django.db.models.signals import post_save,post_delete
from django.core.cache import cache
from django.dispatch import receiver
from .models import Subject


@receiver(post_save,sender = Subject)
@receiver(post_delete,sender = Subject)
def subject_list_cache_update(sender,instance,created=None,**kwargs):
    cache_key = 'subject_list'
    cache.delete(cache_key)
    print(f"Cache {cache_key} successfully deleted")