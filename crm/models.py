from django.db import models
from articles.models import Article
from django.utils import timezone
from django.db.models.signals import pre_delete, post_save, pre_save
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from django.db.models.query import QuerySet

#creiamo un tabella con lo scopo di bindare una ses_key ad un id incrementale univoco, questo per ridurre a 0 la possibilità
#di avere due session_key uguali ( non per forza nello stesso momento, ma anche nel tempo: Django, anche se
#improbabile, potrebbe assegnare un session_key che è già stata assegnata in passato ad un altro user
class SessionBind(models.Model):
    django_session_key = models.ForeignKey(Session)
    start = models.DateTimeField(default=None)
    end = models.DateTimeField(default=None)

#TODO FK da qualche parte ??
class ArticleHit(models.Model):
    article = models.ForeignKey(Article)
    ip = models.CharField(max_length=40)
    custom_session_key = models.ForeignKey(SessionBind)
    created = models.DateTimeField(default=timezone.now())


@receiver(post_save, sender=Session)
def sessionstart_handler(sender, instance, **kwargs):
    print(instance.session_key)
    #custom_session = SessionBind( django_session_key=kwargs.get('instance'))
    #custom_session.save()

    custom_session = SessionBind( django_session_key=instance)
    custom_session.save()







# def sessionend_handler(sender, **kwargs):
#    # SessionBind.objects.filter(django_session_key=kwargs.get('instance').session_key)
#     custom_session = SessionBind.objects.get(django_session_key=kwargs.get('instance').session_key)
#     custom_session.end=timezone.now()


#post_save.connect(sessionstart_handler, sender=Session)
# pre_delete.connect(sessionend_handler, sender=Session)

'''
#quando riceve il signal che un tupla session sta per venire cancellata, cancella anche le tuple nella table ArticleHit
def sessionend_handler(sender, **kwargs):
    ArticleHit.objects.filter(session=kwargs.get('instance').session_key).delete()


pre_delete.connect(sessionend_handler, sender=Session)
'''