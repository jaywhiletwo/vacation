from django.db import models
from django.utils import timezone
import datetime 


class KeyGoal(models.Model):
    name = models.CharField(max_length=255)
    interval = models.IntegerField(default=3)

    @property
    def last_activity(self):
	return self.keyactivity_set.latest('completed')

    def __unicode__(self):
        return self.name

    def deadline(self):
        return self.last_activity.completed.date() + datetime.timedelta(days=self.interval)

    def days_left(self):
        now = timezone.now().date()
        return (self.deadline() - now).days


class KeyActivity(models.Model):
    name = models.CharField(max_length=255)
    completed = models.DateTimeField(auto_now_add=True)
    key_goal = models.ForeignKey(KeyGoal)

    def __unicode__(self):
        return ' '.join((self.name, 'at', '{:%m/%d}'.format(self.completed)))
