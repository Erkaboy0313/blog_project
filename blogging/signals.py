from django.dispatch import receiver,Signal
from django.db.models.signals import pre_save,post_save
from .models import Blog
from django.core.mail import send_mail
from django.conf import settings
from report.models import Subscribe
new_signal = Signal()


@receiver(pre_save,sender = Blog)
def pre_save_blog(sender,instance,**kwargs):
    instance.status = Blog.StatusEnum.DRAFT
    print(instance, 'is being created')

@receiver(post_save,sender = Blog)
def pre_save_blog(sender,instance,created,**kwargs):
    if created:
        subscribers = Subscribe.objects.values_list('email')
        send_mail("Blog saytdan habar",message="Bizda yangi blog qo'yildi",recipient_list=subscribers,from_email=settings.EMAIL_HOST_USER)

