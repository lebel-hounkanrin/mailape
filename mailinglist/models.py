import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from mailinglist import emails

class MailingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=140)
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'mailinglist:manage_mailinglist',
            kwargs={'pk':self.id}
        )
    def user_can_use_mailing_list(self, user):
        return user == self.owner   


class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    confirmed  = models.BooleanField(default=False)
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        is_new = self._state.ading or force_insert
        super().save(force_insert=force_insert, force_update=force_update, using=using,
         update_fields=update_fields)
        if is_new:
            self.send_confirmation_email()
    def send_confirmation_email(self):
        emails.send_confirmation_email(self)
    class Meta:
        unique_together = ['email', 'mailing_list']


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    subject = models.CharField(max_length=140)
    body= models.TextField()
    started = models.DateField(default=None, null=True)
    finished = models.DateField(default=None, null=True)

    

    
    