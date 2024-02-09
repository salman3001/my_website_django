from portfolio.models import ContactMessage
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=ContactMessage)
def SendConatctMessageEmail(sender, **kwargs):
    print("contact message signal recieved")
