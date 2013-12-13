from django.db import models
from django.utils.timezone import utc
import datetime 


class KeyGoal(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class KeyActivity(models.Model):
    name = models.CharField(max_length=255)
    key_goal = models.ForeignKey(KeyGoal)
    interval = models.IntegerField(default=0)
    last_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return ''.join((self.key_goal.name, ': ', self.name))

    def deadline(self):
        return self.last_time.date() + datetime.timedelta(days=self.interval)

    def days_left(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc).date()
        return (self.deadline() - now).days
