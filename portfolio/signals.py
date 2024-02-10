from portfolio.models import ContactMessage
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


@receiver(post_save, sender=ContactMessage)
def SendConatctMessageEmail(sender, **kwargs):
    print(sender.email)
    print(kwargs['instance'].email)
    
    send_mail(
    "Thank you form contacting",
    "We will contact you shortly",
    "from@example.com",
    [kwargs['instance'].email,'therodfighter@gmail.com'],
    fail_silently=True,
    )

